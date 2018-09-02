# Challenge
# Using the Python language, have the function SwapII(str) take the str parameter and swap the case of each character.
# Then, if a letter is between two numbers (without separation), switch the places of the two numbers.
#
# For example: if str is "6Hello4 -8World, 7 yes3" the output should be 4hELLO6 -8wORLD, 7 YES3.
#
# Sample Test Cases
# Input:"Hello -5LOL6"
#
# Output:"hELLO -6lol5"
#
#
# Input:"2S 6 du5d4e"
#
# Output:"2s 6 DU4D5E"

def swap(lst,start,finish):
    temp=lst[finish]
    lst[finish]=lst[start]
    lst[start]=temp


def SwapII(str):

    lst = list(str)

    lst2 =[x.upper() for x in lst]

    tup = [0, 0]
    tup2 = [0, 0]

    i=0
    cnt=0

    for item in lst2:
        if item.isdigit():
            if i == 0:
                tup[0]=item
                tup2[0] = lst.index(item)
                i = i+1
            elif i == 1:
                tup[1]=item
                tup2[1] = lst.index(item)
                i = i+1

        if i == 1:
            #tup2[0]=lst.index(item)
            prev = lst2.index(item)
            if not item.isdigit():
                cnt = cnt+1

        if i == 2:
            #tup2[1]=lst.index(item)
            swap(lst2, tup2[0], tup2[1])

        #print(lst2)
        print(tup2)


    str = ''.join(lst2)

    return str


print(SwapII("aaa5abbbbbLOL6"))



















