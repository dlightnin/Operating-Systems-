# Kai-Ming Chow Benabe
# 842-11-1666
# Assignment 2

# Imported libraries
import threading, socket, random, time, sys

# main function
def Main():
    # number of messages to send
    n = 20
    # mobile id specified by user
    mob_id = str(sys.argv[1])
    # server tuple containing the host and port number specified by user
    server= (str(sys.argv[2]),int(sys.argv[3]))
    # declare udp socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # loop to send messages
    for i in range(n):
        # store random time
        cpu_time= random.randrange(1,6)
        # prepare message for the server
        message = mob_id + ":" + str(cpu_time)
        # send message to server
        sock.sendto(message,server)
        # sleep between sending messages
        time.sleep(cpu_time)

    # close socket after loop ends
    sock.close()

if __name__ == '__main__':
    # execute main function
    Main()
