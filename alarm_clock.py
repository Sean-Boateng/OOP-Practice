# As a developer, I want to use Python’s proper snake_case for variable names.
# As a developer, I want to create an AlarmClock class (alarm_clock.py).
# As a developer, I want the AlarmClock class to have class variables to keep track of the AlarmClock’s current time,
#  whether the alarm is on or off, and the time the alarm is set to. 
# NOTE: You can use arbitrary strings to represent the time, it does not need to be accurate or change over time
# As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print
#  to the console the current time.
# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off. 
# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the 
# current alarm time.
# As a developer, I want to import the AlarmClock class into main.py so 
# I can instantiate it as a new AlarmClock object and call methods on it.
# Print the clock’s time to the terminal
# Call the alarm clock’s change time method to change the time
# Toggle the alarm clock’s on off switch




class AlarmClock :

    def __init__(self) -> None:
        self.alarm_is_on = False
        self.alarm_time = "12:00am"

    def on_off(self):
        self.alarm_is_on = True
        while  self.alarm_is_on is True:
                user_input =input("Do you want to keep alarm clock on? If yes, say True, else say False.")
                if user_input == "False":
                    self.alarm_is_on = False
                    print("See you later")
                    break
                else:
                    continue
    
    
    
    
    def current_time(what_time_is_it):
        time_now = (what_time_is_it)
        print(time_now)
        
    

        

    def set_alarm_time():
        user_input = input("When should I set your alarm for?")
        print("Okay. Your alarm has been set for " + user_input)
        return user_input




        