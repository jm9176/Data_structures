'''
Implementing a job scheduler which takes
in a function, f, and an integer, n, and
calls f after n milliseconds.
'''

import threading
import time

# Function for scheduling the task
# which in this case is to print hello
# f is a function and t_ms is time in millisecs
def scheduler(f, t_ms):
    time.sleep(t_ms)
    return f(int(t_ms*1000))

def print_thread_name(num):
    for i in range(num):
        print threading.currentThread().getName()

# Initializing a thread for the job scheduler
t1 = threading.Thread(target = scheduler, args=(print_thread_name, 0.005))
t1.start()
time.sleep(1)
