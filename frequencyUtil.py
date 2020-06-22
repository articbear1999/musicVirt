
freqList = [pow(2, (i-49)/12)*440 for i in range(1, 89)] # create a list of frequencies with the indices as the note                                                 
                                                         # starts from 1, so the formula works
noteList = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def freq_to_note(freq):
        return findClosest(freqList, 88, freq)      # return index of given freq on what numNote to play

# findClosest, getClosest pulled straight from geeksforgeeks, minor tweaks to return index instead of value
def findClosest(arr, n, target):                        # returns the index of the closest given value in an array
        # Corner cases
        if (target <= arr[0]):
                return 0
        if (target >= arr[n - 1]):
                return n - 1

                # Doing binary search
        i = 0
        j = n
        mid = 0
        while (i < j):
                mid = (i + j) // 2

                if (arr[mid] == target):
                        return mid

                        # If target is less than array
                # element, then search in left
                if (target < arr[mid]):

                        # If target is greater than previous
                        # to mid, return closest of two
                        if (mid > 0 and target > arr[mid - 1]):
                                return getClosest(arr[mid - 1], arr[mid], mid - 1, mid, target)

                                # Repeat for left half
                        j = mid

                        # If target is greater than mid
                else:
                        if (mid < n - 1 and target < arr[mid + 1]):
                                return getClosest(arr[mid], arr[mid + 1], mid, mid + 1, target)

                                # update i
                        i = mid + 1

        # Only single element left after search
        return mid



# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def getClosest(val1, val2, val1Index, val2Index, target):
        if (target - val1 >= val2 - target):
                return val2Index
        else:
                return val1Index
