from flask import Flask
import psutil
import shutil

app = Flask(__name__)

@app.route('/')
def home():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else 'Not Available'
    total, used, free = shutil.disk_usage("/")
    storage_percent = (used / total) * 100
    boot_time = psutil.boot_time()

    return (f"App Status: CPU {cpu}%, Memory {memory}%, "
            f"Storage {storage_percent:.2f}%, Battery {battery_percent}% - "
            f"Boot Time {boot_time}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

