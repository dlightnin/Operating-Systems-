# Kai-Ming Chow Benabe
# 842-11-1666
# Assignment 3 - Optimal Algorithm

# Imported libraries
import  sys
# optimal page replacement function
#(receives current index in flist)
def optimal(index):
    # array that contains the distance of the next reference of each page in frames
    distance  = [None]* len(frames)
    # iterate through every frame value
    for i in range(len(frames)):
        # iterate from index to the rest of flist
        for j in range (index , len(flist)):
            # if the page is referenced again
            if (int(frames[i]) == int(flist[j])):
                # store the distance of the page in distance array
                distance[i] = abs(j - index)#subtract
                # once the first upcoming reference is found, break from loop
                break
    # if a frame wont be referenced
    if (None in distance):
        # replace the page
        frames[distance.index(None)] = flist[index]
    # if the pages in frames are going to be referenced again
    else:
        # retrieve the largest distance element
        mx = (max(distance))
        # replace the page with the largest distance for its next reference
        frames[distance.index(mx)] = flist[index]

# main function
def Main():
    # declare global variables
    global flist,frames
    # array of operations from the input file
    flist = []
    # array of frames
    frames =[]
    # number of frames specified by user
    frame_num = int(sys.argv[1])
    # initialize frames array with none values
    frames = [None] * frame_num
    # total number of page faults
    total_faults = 0
    # open file
    with open(str(sys.argv[2]),'r') as f:
        # iterate through each line of the file
        for line in f:
            for i in line.split():
            #store each line in an array
                tmp = i.split(":")
                # append page number to flist
                flist.append(int(tmp[1]))
    # iterate through all the operations in flist
    for i in range(len(flist)):
        # page hit
        if (flist[i] in frames):
            # do nothing
            pass
        # page fault
        else:
            # if a frame is available
            if (None in frames):
                # add page to frames
                frames[frames.index(None)]=flist[i]
            # if all frames are occupied
            else:
                # call optimal function with current index i
                optimal(i)
            # increment total number of page faults
            total_faults = total_faults + 1

    # display total number of page faults
    print "Total page faults: " +str(total_faults)


if __name__ == '__main__':
    # execute main function
    Main()
