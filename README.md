# Raspberry Pi External Components Scripts Repository

Welcome to the Raspberry Pi External Components Scripts repository! This repository contains scripts that can be used with Raspberry Pi to interact with various external components. Whether you're a hobbyist or a professional tinkering with Raspberry Pi projects, these scripts can help you integrate external hardware seamlessly.

## Available Scripts

### 1. Sound Detection Script

- **Script Name:** KY_037.py
- **Description:** This script utilizes a KY-037 sound sensor module connected to the Raspberry Pi. It continuously monitors the sound level in the surrounding environment. When a sound above a certain threshold is detected, it outputs a message to the console.
- **Usage:**
  - Connect the KY-037 sound sensor to the Raspberry Pi according to the provided instructions, see [this link](https://sensorkit.joy-it.net/en/sensors/ky-037) (GPIO 24 which is pin 18 is used)
  - Run the script `KY_037.py`.
  - Listen for the console output messages indicating sound detection events.
  - Keep in mind that the sensivity of the KY-037 module can be changed using the rotary potentiometer.

