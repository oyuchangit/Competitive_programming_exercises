import time

_start_time = time.time()

sum = 0
for i in range(10000000):
    sum += 1
'''

i = 0
while i < 30000000:
    i += 1
'''
_elapsed_time = time.time() - _start_time

print(_elapsed_time)