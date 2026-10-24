# Server Health Monitoring System

A beginner-friendly Python project that monitors CPU, memory, and disk usage in a Linux environment.

## Features

- Monitors CPU usage.
- Checks memory utilization.
- Checks disk utilization.
- Displays health status in the terminal.
- Logs health information and warnings with timestamps.
- Uses a configurable threshold of 80% for high resource usage.

## Technologies Used

- Python 3
- psutil
- Linux / Ubuntu
- Git and GitHub

## Requirements

- Python 3.12 or compatible Python 3 version
- pip
- Linux or Ubuntu environment

## Installation

Clone the repository:

```bash
git clone https://github.com/nakotivinay3/server-health-monitor.git
cd server-health-monitor
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python monitor.py
```

The program displays CPU, memory, and disk usage, then reports whether each resource is healthy or above the configured threshold.

## Logging

The program writes timestamped health information and warnings to `health.log`. This generated log file is excluded from Git using `.gitignore`.

## Scope and Limitations

This version monitors the Linux environment in which it runs. When run through WSL, the readings represent the environment visible to the script; they should not be interpreted as complete monitoring of a remote production server.

## Future Improvements

- Add automated tests.
- Make the warning threshold configurable.
- Add email or other alert notifications.
- Add Docker support.
- Integrate monitoring into a CI/CD workflow.

## Author

Vinay — [GitHub](https://github.com/nakotivinay3)
