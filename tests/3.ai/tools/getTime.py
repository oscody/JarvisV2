from datetime import datetime


def get_current_time():
    # Get the current time
    now = datetime.now()

    # Format the date and time similar to the screenshot
    formatted_time = now.strftime("%a %b %d %I:%M%p")

    # Output the formatted date and time
    print(formatted_time)