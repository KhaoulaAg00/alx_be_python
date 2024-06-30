# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
reminder_message = f"'{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder_message += " that requires immediate attention today!" if time_bound == "yes" else "."
    case "medium":
        reminder_message += " that should be completed soon."
        if time_bound == "yes":
            reminder_message += " Try to get it done today!"
    case "low":
        reminder_message += ". Consider completing it when you have free time."
        if time_bound == "yes":
            reminder_message += " However, it is time-bound and needs to be addressed."

# Provide a customized reminder
print(f"Reminder: {reminder_message}")
