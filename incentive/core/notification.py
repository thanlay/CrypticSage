import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import threading
import time


class NotificationManager:
    def __init__(self, email_settings, firebase_server_key, sms_provider_settings):
        """
        Initialize notification manager with email, Firebase, and SMS settings.
        """
        self.email_settings = email_settings
        self.firebase_server_key = firebase_server_key
        self.sms_provider_settings = sms_provider_settings

    def send_email(self, recipient, subject, message, is_html=False, retry=3):
        """
        Send an email notification with retry mechanism.
        """
        attempts = 0
        while attempts < retry:
            try:
                msg = MIMEMultipart()
                msg["From"] = self.email_settings["user"]
                msg["To"] = recipient
                msg["Subject"] = subject
                msg.attach(MIMEText(message, "html" if is_html else "plain"))
                server = smtplib.SMTP(self.email_settings["host"], self.email_settings["port"])
                server.starttls()
                server.login(self.email_settings["user"], self.email_settings["password"])
                server.sendmail(self.email_settings["user"], recipient, msg.as_string())
                server.quit()
                print(f"Email sent successfully to {recipient}")
                return True
            except Exception as e:
                attempts += 1
                print(f"Email attempt {attempts} failed: {e}")
                time.sleep(2)  # Exponential backoff
        print("Failed to send email after multiple attempts.")
        return False

    def send_push_notification(self, device_token, title, body, retry=3):
        """
        Send a push notification with retry mechanism.
        """
        url = "https://fcm.googleapis.com/fcm/send"
        headers = {
            "Authorization": f"key={self.firebase_server_key}",
            "Content-Type": "application/json",
        }
        data = {
            "to": device_token,
            "notification": {
                "title": title,
                "body": body,
            },
        }
        for attempt in range(retry):
            try:
                response = requests.post(url, json=data, headers=headers)
                if response.status_code == 200:
                    print(f"Push notification sent to {device_token}")
                    return True
                else:
                    print(f"Push notification failed: {response.json()}")
            except Exception as e:
                print(f"Attempt {attempt + 1} failed for push notification: {e}")
            time.sleep(2)
        print("Failed to send push notification after multiple attempts.")
        return False

    def send_sms(self, phone_number, message, retry=3):
        """
        Send an SMS notification using an external SMS provider.
        """
        url = self.sms_provider_settings["api_url"]
        headers = {"Authorization": f"Bearer {self.sms_provider_settings['api_key']}"}
        data = {"to": phone_number, "message": message}
        for attempt in range(retry):
            try:
                response = requests.post(url, json=data, headers=headers)
                if response.status_code == 200:
                    print(f"SMS sent to {phone_number}")
                    return True
                else:
                    print(f"SMS failed: {response.json()}")
            except Exception as e:
                print(f"Attempt {attempt + 1} failed for SMS: {e}")
            time.sleep(2)
        print("Failed to send SMS after multiple attempts.")
        return False

    def async_send(self, method, *args, **kwargs):
        """
        Send notifications asynchronously using threading.
        """
        thread = threading.Thread(target=method, args=args, kwargs=kwargs)
        thread.start()


# Example usage:
if __name__ == "__main__":
    email_settings = {
        "host": "smtp.example.com",
        "port": 587,
        "user": "your-email@example.com",
        "password": "your-password",
    }
    firebase_key = "your-firebase-key"
    sms_provider = {
        "api_url": "https://sms-provider.example.com/send",
        "api_key": "your-sms-api-key",
    }

    notification_manager = NotificationManager(email_settings, firebase_key, sms_provider)

    # Asynchronous email sending
    notification_manager.async_send(
        notification_manager.send_email,
        recipient="user@example.com",
        subject="Welcome!",
        message="Hello, welcome to our service!",
    )

    # Send push notification
    notification_manager.async_send(
        notification_manager.send_push_notification,
        device_token="device-token",
        title="New Message",
        body="You have a new message.",
    )

    # Send SMS
    notification_manager.async_send(
        notification_manager.send_sms,
        phone_number="+1234567890",
        message="Your verification code is 123456",
    )