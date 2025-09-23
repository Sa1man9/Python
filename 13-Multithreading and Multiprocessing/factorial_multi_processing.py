import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

def factorial(num):
    result=math.factorial(num)
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]
    start_time=time.time()

    with multiprocessing.Pool() as pool:
        results=pool.map(factorial,numbers)

    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")