# Cleaner Tunisia 56

A smart waste management solution submitted for the PEAS RAS SIGHT Challenge in TSYP12. The project consists of two autonomous robots (a mobile collector and a stationary sorter) working together to improve urban cleanliness and waste management efficiency.

## Project Overview

Cleaner Tunisia 56 implements an innovative approach to urban waste management through:
- A mobile collection robot that autonomously patrols streets and gathers litter
- A stationary sorting robot that uses computer vision to classify and sort collected waste
- A mobile application for real-time monitoring and status updates

## Repository Structure

```
├── Collector Robot 3D model/     # 3D design files for the collection robot
├── Sorting Robot 3D model/       # 3D design files for the sorting station
├── Garbage_classification_code_for_raspberry/  # Classification code for Raspberry Pi
├── Mobile App/
│   ├── code/                     # Source code for the mobile application
│   └── app-release.apk          # Compiled Android application
└── Documentation/               # Technical documentation and diagrams
```

## Components

### 1. Collection Robot
- Solar-powered mobile robot for autonomous street cleaning
- Features:
  - GPS navigation with OpenStreetMap integration
  - Obstacle avoidance using ultrasonic sensors
  - Real-time status reporting
  - Solar panel with sun-tracking mechanism
  - Automated waste collection system

### 2. Sorting Robot
- Stationary waste sorting station with:
  - Computer vision-based waste classification
  - Conveyor belt system
  - Automated sorting mechanism
  - Multiple waste category bins
  - Integration with the collection robot

### 3. Mobile Application
- Real-time monitoring of robot status
- Location tracking
- Battery level monitoring
- Container fill level tracking
- Maintenance status updates

## Demo Videos

1. Robots 3D Simulation: [Watch on YouTube]
2. Mobile Application Demo: [Watch on YouTube]

## Technical Implementation

### Waste Classification System
- Implemented on Raspberry Pi
- Uses 3 servo motors for sorting
- AI-powered waste classification
- Supports multiple waste categories

### Mobile Application
- Real-time Firebase integration
- GPS tracking
- Status monitoring
- User-friendly interface

## Technical Requirements

### Collection Robot
- Arduino AtMega microcontroller
- GSM Module (SIM800L)
- GPS Module (Neo-6M)
- Ultrasonic sensors (HC-SR04)
- Solar panel system
- LiPo batteries (11.1V)

### Sorting Robot
- ESP32-CAM
- Arduino Nano
- DC motors with H-Bridge drivers
- Conveyor belt system
- Computer vision system

## Setup Instructions

1. **Raspberry Pi Classification System:**
   - Navigate to the `Garbage_classification_code_for_raspberry` directory
   - Follow the setup instructions in the directory's README
   - Install required dependencies
   - Run the classification system

2. **Mobile Application:**
   - Install the provided APK file from the Mobile App folder
   - Or build from source using the provided code
   - Configure Firebase credentials if building from source

3. **3D Models:**
   - Access the 3D models in their respective folders
   - Use compatible 3D modeling software to view or modify

## Future Development

- Enhanced AI model training for better waste classification
- Integration with city waste management systems
- Extended battery life optimization
- Improved navigation algorithms

## Contributors

[List of team members and contributors]

## License

[Specify license information]

## Contact

For inquiries about this project, please contact [contact information]