import psutil
import logging
from datetime import datetime

logging.basicConfig(
    filename="health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("=== Server Health Monitor ===")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory.percent}%")
print(f"Disk Usage: {disk.percent}%")

for name, usage in [
    ("CPU", cpu),
    ("Memory", memory.percent),
    ("Disk", disk.percent),
]:
    if usage > 80:
        message = f"WARNING: High {name} usage: {usage}%"
        print(message)
        logging.warning(message)
    else:
        message = f"{name} Status: HEALTHY ({usage}%)"
        print(message)
        logging.info(message)
