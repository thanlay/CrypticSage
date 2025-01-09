import psutil
import time
from core.logging import Logger
from core.notification import NotificationManager
from threading import Thread

class MonitoringManager:
    def __init__(self, email_settings, firebase_server_key, interval=5, threshold=85):
        """Initialize the monitoring manager with given thresholds."""
        self.interval = interval
        self.threshold = threshold
        self.logger = Logger()
        self.notification_manager = NotificationManager(
            email_settings["host"],
            email_settings["port"],
            email_settings["user"],
            email_settings["password"],
            firebase_server_key
        )
        self.monitor_thread = Thread(target=self.log_system_metrics)
        self.monitor_thread.daemon = True

    def start_monitoring(self):
        """Start monitoring system resources in a separate thread."""
        self.monitor_thread.start()

    def log_system_metrics(self):
        """Log system metrics like CPU, memory, disk usage."""
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            self.logger.log_info(
                f"CPU: {cpu_usage}%, Memory: {memory.percent}%, Disk: {disk.percent}%"
            )
            if cpu_usage > self.threshold or memory.percent > self.threshold or disk.percent > self.threshold:
                self.send_alert(f"High usage detected - CPU: {cpu_usage}%, Memory: {memory.percent}%, Disk: {disk.percent}%")
            time.sleep(self.interval)

    def send_alert(self, message):
        """Send an alert if system resources exceed the threshold."""
        # Email alert
        self.notification_manager.send_email(
            recipient="admin@example.com",
            subject="System Resource Alert",
            message=message
        )
        # Optional: Push notification
        # self.notification_manager.send_push_notification(
        #     device_token="admin_device_token",
        #     title="System Resource Alert",
        #     body=message
        # )

    def check_service_health(self, service_name):
        """Check if a service is running using psutil."""
        for proc in psutil.process_iter(attrs=["pid", "name"]):
            if proc.info["name"] == service_name:
                return {"status": "running", "pid": proc.info["pid"]}
        return {"status": "stopped"}