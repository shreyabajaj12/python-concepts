from functools import lru_cache
import time
@lru_cache(maxsize=None)         # it helps to memoize the function and helps to stop xtra computation it stores the previous value 
def fx(n):
    time.sleep(5)
    return n*5
print(fx(20))
print("done in 20")
print(fx(2))
print("done in 2")
print(fx(6))
print("done in 6")

print(fx(20))
print("done in 20")
print(fx(2))
print("done in 2")
print(fx(6))
print("done in 6")