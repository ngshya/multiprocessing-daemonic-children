import multiprocessing
import multiprocessing.pool
 

class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)


class NoDaemonProcessPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess
 
 
def create_process_pool(index):
    print(index)
    li = range(3)
    pool = multiprocessing.Pool(processes = len(li))
    for sub_index in li:
        pool.apply_async(print_process_index, (index, sub_index))
    pool.close()
    pool.join()
 
 
def print_process_index(index, sub_index):
    print("%d-%d" %(index, sub_index))




li = range(12)
pool = NoDaemonProcessPool(processes = len(li))
r = pool.map(myFunction, myArray)
pool.close()
pool.join()