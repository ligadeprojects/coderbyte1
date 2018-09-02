# Using the Python language, have the function ArithGeo(arr) take the array of numbers stored in arr and
# return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it
# follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one ' \
# where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first
# is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].
# Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.
#
#
# Sample Test Cases
# Input:5,10,15
#
# Output:"Arithmetic"
#
#
# Input:2,4,16,24
#
# Output:-1

def ArithGeo(arr):
    # code goes here
    const = arr[1] - arr[0]
    const2 = arr[1] / arr[0]

    flag = False

    if arr[1] - arr[0] == arr[2] - arr[1]:
        geo = False
    elif arr[1] / arr[0] == arr[2] / arr[1]:
        geo = True

    for i in range(len(arr)-1):
        if geo:
            if arr[i + 1] / arr[i] == const2:
                flag = True
            else:
                flag = False
                break

        if not geo:
            if arr[i + 1] - arr[i] == const:
                flag = True
            else:
                flag = False
                break

    return "True"


# keep this function call here
print(ArithGeo([1,2,3,4]))