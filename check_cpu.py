import psutil


def monitor_cpu(interval=1):
    while True:
        try:
            # Get CPU usage percentage
            cpu_percent = psutil.cpu_percent(interval=interval)

            # Alert if CPU usages is in between 85% to 90%
            if 85 < cpu_percent <= 90:
                print("Alert! CPU usage exceeds threshold: 85%")
            # Alert if CPU usages is above 90%
            if cpu_percent > 90:
                print("Alert! CPU usage exceeds threshold: 90%")
        except KeyboardInterrupt:
            print("Monitoring stopped")
        except Exception as e:
            print(e)
            print("\n Monitoring Stopped")


if __name__ == "__main__":
    print("Starting CPU monitoring")
    monitor_cpu()
