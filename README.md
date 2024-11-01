# Breaking The Habbit Habit Tracker

## Setup

1. Clone the repository:
   git clone <repository_url>
   cd <repository_directory>

2. Install dependencies:
   pip install -r requirements.txt

3. Create a config.json file with your SMTP credentials:
   {
        "email_user": "your_email@gmail.com",
        "email_pass": "your_password"
   }

## Usage

1. CLI commands:
   * Create a habit:
   python cli.py create-habit <name> <frequency>
   example:
   python cli.py create-habit Exercise daily

   * List all habits:
   python cli.py list-habits

   * Modify the frequency of a habit:
   python cli.py modify-frequency <name> <new_frequency>
   Example:
   python cli.py modify-frequency Exercise weekly

   * Complete a task:
   python cli.py complete-task <name>
   Example:
   python cli.py complete-task Exercise

   * Get the longest streak for a specific habit:
   python cli.py longest-streak <name>
   Example: 
   python cli.py longest-streak Exercise

   * Get the habit with the longest streak among all habits:
   python cli.py longest-streak-all

## Testing

    Run Tests:
    python -m unittest discover

## Configuration

The application uses a config.json file to store SMTP credentials for sending email reminders. Ensure this file is created in the root directory of the project with the following structure:

{
    "email_user": "your_email@gmail.com",
    "email_pass": "your_password"
}

## Code Quality

To ensure code quality, use flake8 for linting and black for formatting:
pip install flake8 black
flake8 .
black .

## Contributing

1. Fork the repository

2. Create a new branch (git checkout -b feature-branch)

3. Make your changes

4. Commit your changes (git commit -am 'Add new feature').

5. Push to the branch (git push origin feature-branch).

6. Create a new Pull Request.
