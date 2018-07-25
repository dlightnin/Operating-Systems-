# Kai-Ming Chow Benabe
# 842-11-1666
# Assignment 3 - Second Chance Algorithm

# Imported libraries
import  sys
# main function
def Main():
    # declare global variables
    global flist,frames
    # array of page numbers from the input file
    flist = []
    # array of frames
    frames =[]
    # number of frames specified by user
    frame_num = int(sys.argv[1])
    # initialize frames array with none values
    frames = [None] * frame_num
    #total number of faults
    total_faults = 0
    # open file
    with open(str(sys.argv[2]),'r') as f:
        # iterate through each line of the file
        for line in f:
            for i in line.split():
            #store each line in an array
                tmp = i.split(":")
                # append to page number flist
                flist.append(int(tmp[1]))
    # iterate through all the operations in flist
    for i in range(len(flist)):
        # page hit
        if (flist[i] in frames):
            # retrieve index of page contained in frames
            ref_index = frames.index(flist[i])
            # move the page to the end of the frames array
            frames.append(frames.pop(ref_index))
        # page fault
        else:
            # if a frame is available
            if (None in frames):
                # add page to the frames
                frames[frames.index(None)]=flist[i]
            # if all frames are occupied
            else:
                # remove the first element from the frames array
                frames.pop(0)
                # append to the end of the frames array
                frames.append(flist[i])
            # increment total number of page faults
            total_faults = total_faults + 1

    # display total number of page faults
    print "Total page faults: " +str(total_faults)

if __name__ == '__main__':
    # execute main function
    Main()
