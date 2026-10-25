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
## Automated Monitoring with Cron

The Server Health Monitor can run automatically every five minutes using a Linux cron job.

### Setup

1. Open the cron scheduler:

   ```bash
   crontab -e
   ```

2. Add the following entry, replacing `vinay` if your Linux username is different:

   ```cron
   */5 * * * * cd /home/vinay/devOps/projects/server-health-monitor && /home/vinay/devOps/projects/server-health-monitor/.venv/bin/python monitor.py >> /home/vinay/devOps/projects/server-health-monitor/cron.log 2>&1
   ```

3. Save and exit the editor.

### Verify

Check the scheduled jobs:

```bash
crontab -l
```

View the output produced by scheduled runs:

```bash
cat ~/devOps/projects/server-health-monitor/cron.log
```

The log records the timestamp and CPU, memory, and disk usage reported by each run.

**Note:** This setup assumes cron is running in the Linux environment and the virtual environment exists at the specified path. In WSL, scheduled jobs may not run while the Linux environment is stopped.
