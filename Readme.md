<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/chater-marzougui-342125299/)

</div>


<br />
<div align="center">
    <h1 style="font-size:35px">Cleaner Tunisia 56 - IEEE SubCom SB  <br></h1>
    <br>
    <p style="font-size:20px" align="center">
        A comprehensive bipolar disorder management app designed to improve mental health and well-being.
    <br>
    <br>
    <a href="https://github.com/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>
<br>
<br>
  

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

1. Robots 3D Simulation:

<div align="center">

[![YouTube Video](https://img.youtube.com/vi/OxUUnQa4V6M/0.jpg)](https://www.youtube.com/watch?v=OxUUnQa4V6M)

</div>

2. Mobile Application Demo: [Watch on YouTube]

<div align="center">

[![YouTube Video](https://img.youtube.com/vi/lcw-HjMQoZ0/0.jpg)](https://www.youtube.com/watch?v=lcw-HjMQoZ0)

</div>

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
- Raspberry Pi 4 Model B with camera
- Servo Motor with linear actuator
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


[contributors-shield]: https://img.shields.io/github/contributors/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location.svg?style=for-the-badge
[contributors-url]: https://github.com/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location.svg?style=for-the-badge
[forks-url]: https://github.com/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location/network/members
[stars-shield]: https://img.shields.io/github/stars/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location.svg?style=for-the-badge
[stars-url]: https://github.com/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location/stargazers
[issues-shield]: https://img.shields.io/github/issues/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location.svg?style=for-the-badge
[issues-url]: https://github.com/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location/issues
[license-shield]: https://img.shields.io/github/license/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location.svg?style=for-the-badge
[license-url]: https://github.com/chater-marzougui/Sup-Bot_HexaBot-Nearby-Location/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/chater-marzougui-342125299/
