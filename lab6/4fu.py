from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)

n = int(input())
m = int(input())
print(delay(lambda x: math.sqrt(x), n, m))