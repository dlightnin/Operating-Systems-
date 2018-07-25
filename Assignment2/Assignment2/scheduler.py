# Kai-Ming Chow Benabe
# 842-11-1666
# Assignment 2

# Imported libraries
import threading, socket, random, time, sys

#Define producer class
class Producer(threading.Thread):
    #initialize the class
    def __init__ (self):
        threading.Thread.__init__(self)

    # Define what the thread does
    def run(self):

        # acquire empty Semaphore
        empty.acquire()
        # receive message from client
        data,addr = sock.recvfrom(1024)
        # split and store the data
        data_split = data.split(":")
        # store the mobile id
        mob_id = data_split[0]
        # store the time to wait for the job
        cpu_time = data_split[1]
        # acquire lock to enter critical region
        lock.acquire()
        # check if mob_id is NOT being used as a key in the dictionary
        if not str(mob_id) in total_time:
            # Use mob_id as key and initialize to 0
            total_time[str(mob_id)] = 0
        # append data in shared buffer
        buff.append(data_split)
        # release lock to exit critical region
        lock.release()
        # release full Semaphore
        full.release()

# Define Consumer class
class Consumer(threading.Thread):

    #initialize the class
    def __init__ (self):
        threading.Thread.__init__(self)

    # Define what the thread does
    def run(self):
        # acquire full Semaphore
        full.acquire()
        # acquire lock and enter the critical region
        lock.acquire()
        # Remove the first element from the queue and assign to variable
        stored_data = buff.pop(0)
        # release lock and exit the critical region
        lock.release()
        # assign mobile id to variable
        mob_id = int(stored_data[0])
        # assign the job's time to variable
        cpu_time = int(stored_data[1])
        # sleep
        time.sleep(cpu_time)
        # acquire lock to enter the critical region
        lock.acquire()
        # total job time stored
        total_time[str(mob_id)] += cpu_time
        # release lock and exit the critical region
        lock.release()
        # release the empty Semaphore
        empty.release()


# define the main function
def Main():
    # declare the global variables
    global lock, buff, addr, i, n, host, port, sock, empty, full,total_time,data_split
    # assign number of jobs
    n = 20
    # assign lock
    lock = threading.Lock()
    # assign queue
    buff = []
    # assign empty Semaphore
    empty = threading.Semaphore(n)
    # assign full Semaphore
    full = threading.Semaphore(0)
    # server host
    host = "127.0.0.1"
    # server port specified by user
    port = int(sys.argv[1])
    # declare udp socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # bind the server to localhost
    sock.bind((host,port))
    # dictionary with total job time
    total_time = {}
    # loop until nth job

    for i in range(n):
        # create producer thread
        producer = Producer()
        # create consumer thread
        consumer = Consumer()
        # execute producer thread
        producer.start()
        # execute consumer thread
        consumer.start()
        # wait for producer thread
        producer.join()
        # wait for consumer thread
        consumer.join()

    for x in total_time:
        print "mobile " + str(x) + " consumed " + str(total_time[x]) + " seconds of cpu time."

    # close socket after displaying results
    sock.close()


if __name__ == '__main__':
    Main()
