from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers(n):
    time.sleep(1)
    return n

numbers=[1,2,3,4,6,7,8,9]

if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=3) as exec:
        results=exec.map(print_numbers,numbers)

    for result in results:
        print(result)