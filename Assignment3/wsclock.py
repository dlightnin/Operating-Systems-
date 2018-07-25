# Kai-Ming Chow Benabe
# 842-11-1666
# Assignment 3 - Wsclock Algorithm

# Imported libraries
import sys

#Definition of page class
class Page:
    #Attributes of page class
    def __init__(self):
        # page number
        self.page_num = None
        # reference bit
        self.r_bit = 0
        # modified bit
        self.m_bit = 0
        # virtual time
        self.v_time = 0
    #Method that retrieves page
    def getPage(self):
        return self.page_num
    #Method that sets page number
    def setPage(self, page):
        self.page_num = int(page)
    # Method that retrieves reference bit
    def getRef(self):
        return self.r_bit
    #Method that sets reference bit
    def setRef(self, bit):
        self.r_bit = int(bit)
    # Method that retrieves virtual time
    def getTime(self):
        return self.v_time
    #Method that sets page virtual time
    def setTime(self, time):
        self.v_time = int(time)
    # Method that retrieves modified bit
    def getMod(self):
        return self.m_bit
    #Method that sets the modified bit
    def setMod(self, bit):
        self.m_bit = int(bit)

# wsclock page replacement function
#(receives clock hand and current index in flist)
def wsclock(hand,i):
    # if reference bit is set to 0
    if (frames[hand].getRef()==0):
        # if age of the frame is less than tau
        if (abs(frames[hand].getTime() - i) < tau):
            # advance clock hand
            hand = (hand + 1) % len(frames)
            # recursively call wsclock function
            wsclock(hand,i)
        # if age of the frame is greater than tau
        else:
            # if the pointed frame's mod bit is set to 0
            if (frames[hand].getMod()==0):
                # replace page
                frames[hand].setPage(flist[i])
                # set ref bit to 1
                frames[hand].setRef(1)
                # update virtual time
                frames[hand].setTime(i)
                #if the page operation is W
                if ( str(operations[i])== "W"):
                    # set mod bit to 1
                    frames[hand].setMod(1)
                # advance clock hand
                hand = (hand + 1) % len(frames)
                # return from function
                return
            # if the pointed frame's mod bit is set to 1
            else:
                # advance clock hand
                frames[hand].setMod(0)
                # advance clock hand
                hand = (hand + 1) % len(frames)
                # recursively call wsclock function
                wsclock(hand,i)
    # if reference bit set to 1
    else :
        # set ref bit to 0
        frames[hand].setRef(0)
        # advance clock hand
        hand = (hand + 1) % len(frames)
        # recursively call wsclock function
        wsclock(hand,i)

# function that checks if page is already in frames
def check(page):
    # iterate through frames array
    for i in range(len(frames)):
        # if parameter page number is found in frames
        if (frames[i].getPage() == page):
            # return true
            return True
    # return false
    return False

# function that retrieves index of frame that already contains the page
def indexOf(page):
    # iterate through frames array
    for i in range(len(frames)):
        # if parameter page number is found in frames
        if (frames[i].getPage() == page):
            # return index
            return i

# definition of main function
def Main():
    # declare global variables
    global flist, frames, tau, hand, total_faults, operations
    # array of pages from the input file
    flist = []
    # array of operations from the input file
    operations = []
    # array of frames
    frames = []
    #position on flist
    pos = 0
    # number of frames specified by user
    frame_num = int(sys.argv[1])
    # initialize frames array with none values
    frames = [None] * frame_num
    # tau specified by user
    tau = int(sys.argv[2])
    # initialize total number of faults to 0
    total_faults = 0
    # open file specified by user
    with open(str(sys.argv[3]),'r') as f:
        # iterate through each line of the file
        for line in f:
            for i in line.split():
                #store each line in an array
                tmp = i.split(":")
                # append each operation in array
                operations.append(str(tmp[0]))
                # append each page number in array
                flist.append(int(tmp[1]))
    # iterate through frames array
    for i in range(len(frames)):
        # store page classes as elements of frames array
        frames[i]= Page()
    # initialize clock hand to 0
    hand = 0
    # initialize index, for page hits, to 0
    index = 0
    # iterate through flist
    for i in range(len(flist)):
        # If page hit occurs
        if (check( flist[i])):
            # store index of frame that already contains the page
            index = indexOf(flist[i])
            # if ref bit is 1
            if (frames[index].getRef()== 1):
                # update virtual time of page
                frames[index].setTime(i)
            # if ref bit is 0
            else:
                # Set ref bit to 1
                frames[index].setRef(1)
                # update virtual time of page
                frames[index].setTime(i)
        # If page fault occurs
        else:
            # if a frame is available
            if (frames[hand].getPage() == None):
                # store page in available frame
                frames[hand].setPage(flist[i])
                # set ref bit to 1
                frames[hand].setRef(1)
                #set virtual time
                frames[hand].setTime(i)
                # if the page operation is W
                if ( str(operations[i])== "W"):
                    # set modified bit to 1
                    frames[hand].setMod(1)
                # advance clock hand
                hand = (hand + 1) % len(frames)
            # if all frames are occupied
            else:
                # call wsclock function with current hand and i index for flist
                wsclock(hand,i)
            # increment total number of page faults
            total_faults = total_faults + 1

    # display total number of page faults
    print "Total page faults: "+ str(total_faults)

if __name__ == '__main__':
    # execute main function
    Main()
