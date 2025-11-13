# Import the necessary libraries for Alarm Clock
import time
import winsound
import datetime

# Getting user input for the alarm time
# I define a function called set_alarm and from here I define my alarm minutes
# and hours based on user input. the int() functions is used for data casting
# and the input() function is to take user input
def set_alarm():
    alarm_hour = int(input(f"Enter the alarm hor (0-23): "))
    alarm_minute = int(input("Enter the alarm minute (0-59): "))

    # Print the alarm time in hour and minute formation
    print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")

    # create a while look to read the current time and interate until the standard
    # local time matches the set alarm time
    while True:
        current_time = datetime.datetime.now()
        if current_time.hour == alarm_hour and current_time.minute == alarm_minute:
            print("It is time to wake up!!!!")
            winsound.Beep(2500, 1000)   # make the sound based on (frequency, seconds)
            break
        time.sleep(1) # hold off for 1 second

if __name__ == "__main__":
    set_alarm()


# Implementing the Alarm Clock

# Triggering the Alarm Clock