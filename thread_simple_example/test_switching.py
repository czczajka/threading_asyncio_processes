import threading
import sys

# TEST VARIABLES
OPERATIONS_PER_THREAD = 100000
SWITCH_INTERVAL = 999

thread_list = []
lock = threading.Lock()


def thread0_fun():
    for i in range(OPERATIONS_PER_THREAD):
#        lock.acquire()
        print("Thread number: 0")
#        lock.release()

def thread1_fun():
    for i in range(OPERATIONS_PER_THREAD):
#        lock.acquire()
        print("Thread number: 1")
#        lock.release()

def thread2_fun():
    for i in range(OPERATIONS_PER_THREAD):
#       lock.acquire()
        print("Thread number: 2")
#        lock.release()

def main():
    sys.setswitchinterval(SWITCH_INTERVAL)

    thread0 = threading.Thread(target=thread0_fun)
    thread1 = threading.Thread(target=thread1_fun)
    thread2 = threading.Thread(target=thread2_fun)

    thread0.start()
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    try:
        print(sys.getswitchinterval())
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
