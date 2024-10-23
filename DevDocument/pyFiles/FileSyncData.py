import schedule
import time
import subprocess


def backup_alfalfa():
    # Replace with your backup command
    subprocess.call(["your_backup_command", "alfalfa_data"])


schedule.every().day.at("01:00").do(backup_alfalfa)

while True:
    schedule.run_pending()
    time.sleep(1)
