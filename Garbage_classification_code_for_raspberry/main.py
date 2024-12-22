import timm
import torch
from PIL import Image
from torchvision import transforms
from picamera2 import Picamera2
import cv2
import numpy as np
import time
import RPi.GPIO as GPIO

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Servo pins - using GPIO pins that support PWM
SERVO_METAL = 12    # GPIO12 (PIN 32)
SERVO_GLASS = 13    # GPIO13 (PIN 33)
SERVO_CLOTHES = 18  # GPIO18 (PIN 12)

# Setup GPIO pins for servos
GPIO.setup(SERVO_METAL, GPIO.OUT)
GPIO.setup(SERVO_GLASS, GPIO.OUT)
GPIO.setup(SERVO_CLOTHES, GPIO.OUT)

# Create PWM objects for each servo (50Hz frequency)
servo_metal = GPIO.PWM(SERVO_METAL, 50)
servo_glass = GPIO.PWM(SERVO_GLASS, 50)
servo_clothes = GPIO.PWM(SERVO_CLOTHES, 50)

# Start PWM with neutral position
servo_metal.start(7.5)  # Neutral position (no rotation)
servo_glass.start(7.5)
servo_clothes.start(7.5)

def control_servo(servo, direction):
    """
    Control continuous servo rotation
    direction: 1 for clockwise, -1 for counter-clockwise, 0 for stop
    """
    if direction == 1:
        servo.ChangeDutyCycle(10)  # Clockwise rotation
    elif direction == -1:
        servo.ChangeDutyCycle(5)   # Counter-clockwise rotation
    else:
        servo.ChangeDutyCycle(7.5) # Stop

def sort_item(label):
    """
    Control servos based on detected item
    """
    # Reset all servos to neutral
    control_servo(servo_metal, 0)
    control_servo(servo_glass, 0)
    control_servo(servo_clothes, 0)
    
    if label == 'metal':
        print("Sorting metal...")
        control_servo(servo_metal, 1)
        time.sleep(2)  # Run for 2 seconds
        control_servo(servo_metal, 0)
    
    elif label in ['brown-glass', 'green-glass', 'white-glass']:
        print("Sorting glass...")
        control_servo(servo_glass, 1)
        time.sleep(2)
        control_servo(servo_glass, 0)
    
    elif label in ['clothes', 'shoes']:
        print("Sorting clothes...")
        control_servo(servo_clothes, 1)
        time.sleep(2)
        control_servo(servo_clothes, 0)

# Initialize PiCamera2
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

# Set up device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model
checkpoint = torch.load("./model.pth", map_location=torch.device(device))
model = timm.create_model("efficientnet_b0", pretrained=False, num_classes=12)
model.load_state_dict(checkpoint['model_state_dict'])
model = model.to(device)
model.eval()

# Define class labels
class_labels = [
    'battery',
    'biological',
    'brown-glass',
    'cardboard',
    'clothes',
    'green-glass',
    'metal',
    'paper',
    'plastic',
    'shoes',
    'trash',
    'white-glass'
]

# Define image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def predict(image):
    """
    Make prediction on an image
    """
    image = transform(image).unsqueeze(0).to(device)
    with torch.inference_mode():
        output = model(image)
        _, predicted = torch.max(output, 1)
        label = class_labels[predicted.item()]
    return label

# Add a debounce mechanism to prevent rapid servo activation
last_sort_time = 0
SORT_COOLDOWN = 3  # Seconds between sorting actions

try:
    while True:
        # Capture frame
        frame = picam2.capture_array()
        
        # Convert to RGB for PIL
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)
        
        # Make prediction
        label = predict(pil_image)
        
        # Add prediction text to frame
        cv2.putText(frame, f"Prediction: {label}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Display the frame
        cv2.imshow("Garbage Classification", frame)
        
        # Check if we should activate sorting mechanism
        current_time = time.time()
        if current_time - last_sort_time >= SORT_COOLDOWN:
            if label in ['metal', 'brown-glass', 'green-glass', 'white-glass', 'clothes', 'shoes']:
                sort_item(label)
                last_sort_time = current_time
        
        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        # Small delay to prevent overwhelming the Pi
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping the program...")
finally:
    # Cleanup
    print("Cleaning up...")
    servo_metal.stop()
    servo_glass.stop()
    servo_clothes.stop()
    GPIO.cleanup()
    cv2.destroyAllWindows()
    picam2.stop()