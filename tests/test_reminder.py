import os
import unittest
from unittest.mock import patch, MagicMock
from src.user import User
from src.habit import Habit
from src.reminder import Reminder

class TestReminder(unittest.TestCase):

    def setUp(self):
        self.user = User(username="test_user", email="test_user@example.com")
        self.habit1 = Habit(name="Exercise", frequency="daily")
        self.habit2 = Habit(name="Read", frequency="weekly")
        self.user.add_habit(self.habit1)
        self.user.add_habit(self.habit2)
        self.reminder = Reminder(self.user)

    @patch('smtplib.SMTP_SSL')
    def test_send_email_reminder(self, mock_smtp):
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        self.reminder.send_email_reminder(self.habit1)

        mock_smtp.assert_called_once_with('smtp.gmail.com', 465)
        mock_server.login.assert_called_once_with('your_email@gmail.com', 'your_password')
        mock_server.sendmail.assert_called_once()

    @patch('requests.post')
    def test_send_push_notification(self, mock_post):
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        device_token = "device_token_placeholder"
        self.reminder.send_push_notification(self.habit1, device_token)

        mock_post.assert_called_once_with(
            "https://fcm.googleapis.com/fcm/send",
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'key={os.getenv("FCM_SERVER_KEY")}',
            },
            json={
                'to': device_token,
                'notification': {
                    'title': f"Reminder: {self.habit1.name}",
                    'body': f"Don't forget to complete your habit: {self.habit1.name} ({self.habit1.frequency})",
                },
            }
        )

    @patch('smtplib.SMTP_SSL')
    @patch('requests.post')
    def test_send_reminders(self, mock_post, mock_smtp):
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        self.reminder.send_reminders()

        self.assertEqual(mock_smtp.call_count, 2)
        self.assertEqual(mock_post.call_count, 2)

if __name__ == '__main__':
    unittest.main()