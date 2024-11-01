import os
import smtplib
import requests
import json
from email.mime.text import MIMEText
from typing import List
from src.user import User
from src.habit import Habit

class Reminder:
    def __init__(self, user: User):
        """
        Initialize a new reminder for a user.

        :param user: The user to send reminders to.
        """
        self.user = user
        with open('config.json', 'r') as f:
            config = json.load(f)
        self.email_user = config['email_user']
        self.email_pass = config['email_pass']

    def send_email_reminder(self, habit: Habit) -> None:
        """
        Send an email reminder for a habit.

        :param habit: The habit to send a reminder for.
        """
        subject = f"Reminder: {habit.name}"
        body = f"Don't forget to complete your habit: {habit.name} ({habit.frequency})"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.email_user
        msg['To'] = self.user.email

        # Email sending logic using Gmail's SMTP server
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(self.email_user, self.email_pass)
                server.sendmail(self.email_user, [self.user.email], msg.as_string())
            print(f"Email reminder sent to {self.user.email} for habit '{habit.name}'")
        except Exception as e:
            print(f"Failed to send email reminder: {e}")

    def send_push_notification(self, habit: Habit, device_token: str) -> None:
        """
        Send a push notification reminder for a habit.

        :param habit: The habit to send a reminder for.
        :param device_token: The device token to send the push notification to.
        """
        # FCM endpoint
        url = "https://fcm.googleapis.com/fcm/send"

        # FCM server key
        server_key = os.getenv('FCM_SERVER_KEY')

        # Notification payload
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'key={server_key}',
        }
        payload = {
            'to': device_token,
            'notification': {
                'title': f"Reminder: {habit.name}",
                'body': f"Don't forget to complete your habit: {habit.name} ({habit.frequency})",
            },
        }

        # Send the push notification
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            print(f"Push notification sent to {device_token} for habit '{habit.name}'")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send push notification: {e}")

    def send_reminders(self) -> None:
        """
        Send reminders for all habits of the user.
        """
        for habit in self.user.get_habits():
            # Placeholder device token
            device_token = "device_token_placeholder"
            self.send_email_reminder(habit)
            self.send_push_notification(habit, device_token)