#! /usr/bin/env python3

'''A simple cronometer implementation'''

from time import sleep


init_hour = 0
init_minute = 0
init_second = 0
init_decisecond = 0
init_centisecond = 0



def execute_centisecond_counter(current_centiseconds):
    sleep(0.01)
    current_centiseconds = current_centiseconds + 1
    return current_centiseconds


def execute_cronometer_logic():
    current_hours = init_hour
    current_minutes = init_minute
    current_seconds = init_second
    current_centiseconds = init_centisecond
    while(True):
        try:
            current_time = '{}:{}:{}:{}'.format(current_hours, current_minutes, current_seconds, current_centiseconds)
            print(current_time)
            current_centiseconds = execute_centisecond_counter(current_centiseconds)
            if current_centiseconds == 100:
                current_centiseconds = 0
                current_seconds = current_seconds + 1
            if current_seconds == 60:
                current_seconds = 0
                current_minutes = current_minutes + 1
            if current_minutes == 60:
                current_minutes = 0
                current_hours = current_hours + 1   
        except KeyboardInterrupt:
            break
            
    
            

execute_cronometer_logic()
