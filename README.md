# Smart Water Monitoring System Using IoT

## Project Overview
This project demonstrates a simulated water-flow monitoring system using Python. It detects when water flow starts and stops and displays alerts in the terminal.

The project is part of a broader academic concept exploring IoT-based water monitoring and ANN-based water-supply prediction.

## Features
- Simulates water flow at different time intervals.
- Displays the current flow rate in litres per minute (L/min).
- Detects when water flow starts.
- Detects when water flow stops.
- Displays different alerts for flow-start and flow-stop events.
- Runs continuously until stopped by the user.

## Technologies Used
- Python
- Time module
- Basic conditional logic and functions

## Simulation Logic
- **0–5 seconds:** Water flow is off.
- **5–15 seconds:** Water flow is on at approximately 5.0 L/min.
- **After 15 seconds:** Water flow is off.

The program checks the simulated flow rate every second and displays an alert when the flow status changes.

## How to Run
1. Install Python on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

   ```bash
   python water_flow_monitoring_simulation.py
   ```

5. Press `Ctrl + C` to stop the simulation.

## Project Status
The Python water-flow monitoring simulation is available in this repository. Physical sensor integration with ESP32 and ANN-based water-supply prediction are separate parts of the broader project and are not implemented in this simulation file.

## Future Improvements
- Integrate a physical water-flow sensor with an ESP32.
- Add an actual buzzer for audible alerts.
- Develop an ANN model to predict the next expected water-supply time using suitable historical data.

## Author
Kavinaya K.
