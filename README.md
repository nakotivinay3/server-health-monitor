# Server Health Monitoring System

A Python-based DevOps project that monitors CPU, memory, and disk usage in a Linux environment.

## Features

- CPU, memory, and disk monitoring
- HEALTHY and WARNING status reporting
- Timestamped logging
- Configurable warning threshold
- Docker and Docker Compose support
- Automated tests using pytest
- Scheduled execution using cron

## Technologies

Python 3.12, psutil, pytest, Linux/Ubuntu, Docker, Docker Compose, Git, GitHub, and cron.

## Installation

Clone the repository:

    git clone https://github.com/nakotivinay3/server-health-monitor.git
    cd server-health-monitor

Create and activate a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Run Locally

    python3 monitor.py

## Run Tests

    python3 -m pytest test_monitor.py -v

## Run with Docker

    docker build -t server-health-monitor .
    docker run --rm server-health-monitor

## Run with Docker Compose

    docker compose config
    docker compose run --build --rm server-health-monitor

## Configure the Warning Threshold

The default threshold is 80%, configured in compose.yaml using WARNING_THRESHOLD.

To test with a threshold of 1%:

    docker compose run --rm -e WARNING_THRESHOLD=1 server-health-monitor

Usage above the selected threshold produces a WARNING.

## Logging

The application writes timestamped messages to health.log. Temporary Docker containers may lose their internal logs when removed unless persistent storage is configured.

## Cron Scheduling

Cron can schedule the monitor to run every five minutes. Check configured jobs using:

    crontab -l

Ensure the Linux environment and required services are running for scheduled jobs to execute.

## Scope and Limitations

The monitor reports resource usage visible to the environment in which it runs. WSL or container readings are not a substitute for complete monitoring of a remote production server.

## Future Improvements

- GitHub Actions CI/CD
- Alert notifications
- Cloud deployment
- Kubernetes integration
- Persistent monitoring and dashboards

## Author

Vinay — https://github.com/nakotivinay3
