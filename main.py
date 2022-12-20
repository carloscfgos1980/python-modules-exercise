# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

import this
import time
import math
from datetime import datetime

print(this)
print(time)


def wait(sec):
    time.sleep(sec)
    return 'nothing'


print('Wait and see', wait(3))


def my_sin(x):
    return math.sin(x)


print('sin:\n', my_sin(10.5))


def iso_now():
    current_dateTime = datetime.now().isoformat()
    return current_dateTime[:-10]


print('datetime:\n', iso_now())
