import time
import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in "abcde":
        print(letter)
        time.sleep(1)

if __name__=="__main__":
    p1=multiprocessing.Process(target=print_numbers)
    p2=multiprocessing.Process(target=print_letters)

    t=time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    total_time=time.time()-t
    print(total_time)
