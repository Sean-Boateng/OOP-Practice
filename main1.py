from re import A
from alarm_clock import AlarmClock
from alarm_clock import AlarmClock








def execute():
    my_clock = AlarmClock()
    my_clock.on_off()
    if my_clock.alarm_is_on == False:
        print("")
        return
   
    what_is_time_now = AlarmClock.current_time('3:03')
    change_alarm_time = AlarmClock.set_alarm_time()

testing = execute()