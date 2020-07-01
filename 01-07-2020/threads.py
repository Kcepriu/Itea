import time
from threading import Thread, enumerate

def io_bound(ind, t):
    print(f'Operation with index {ind} startted')
    time.sleep(t)
    print(f'Operation with index {ind} enden in {t} second')

# start = time.time()
#
# io_bound(0, 3)
# io_bound(1, 4)
# io_bound(2, 3)
#
# print(f'Total time {time.time()-start}')
start = time.time()
t = Thread(target = io_bound, args=(0, 3), daemon=True, name='Sleeping')
t2 = Thread(target = io_bound, args=(1, 4), daemon=True)
t3 = Thread(target = io_bound, args=(2, 3), daemon=True)

t.start()
t2.start()
t3.start()

# t.join()
# t2.join()
# t3.join()
print(t,  t2, t3)
print(t.getName())
print(t.is_alive())
print(enumerate())
print(f'Total time {time.time()-start}')
