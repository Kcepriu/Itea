import time
from threading import Thread, enumerate
from multiprocessing import Process

def cpu_bounds():
    return range(2700**1000000)

def start_sync():
    start = time.time()
    cpu_bounds()
    cpu_bounds()
    cpu_bounds()
    print(f'Total time {time.time()-start}')

def start_in_threads():
    start = time.time()
    t = Thread(target=cpu_bounds)
    t1 = Thread(target=cpu_bounds)
    t2 = Thread(target=cpu_bounds)
    t.start(), t1.start(), t2.start()

    t.join(), t1.join(), t2.join()


    print(f'Total time {time.time()-start}')

def start_in_process():
    start = time.time()
    t = Process(target=cpu_bounds)
    t1 = Process(target=cpu_bounds)
    t2 = Process(target=cpu_bounds)
    t.start(), t1.start(), t2.start()

    t.join(), t1.join(), t2.join()


    print(f'Total time {time.time()-start}')
start_sync()
start_in_threads()
start_in_process()
