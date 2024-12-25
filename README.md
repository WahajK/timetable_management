# Timetable Management System

## Overview

The Timetable Management System is a Python-based application built using Tkinter library with a focus on Object Oriented Programming.
## Features

- **Student Management**: Handle student information and their respective schedules.
- **Teacher Management**: Manage teacher profiles and their assigned classes.
- **Room Allocation**: Efficiently assign rooms for classes to prevent scheduling conflicts.
- **Automated Scheduling**: Generate timetables automatically based on predefined constraints.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/WahajK/timetable_management.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd timetable_management
   ```

## Usage

1. **Run the Application**:
   ```bash
   python main.py
   ```
2. **Follow the On-Screen Prompts**: The application will guide you through managing students, teachers, and room allocations. The default password for **Admin** is `admin:admin` which can be changed from the `Admin.py` file.

## File Structure

- `main.py`: Entry point of the application.
- `Student.py`: Module for managing student-related functionalities.
- `Teacher.py`: Module for managing teacher-related functionalities.
- `Admin.py`: Module for administrative tasks.
- `Rooms.txt`: Contains data related to room information.
- `Teacher.txt`: Contains data related to teacher information.
