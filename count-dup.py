
def countDupHash():
    lst = [1,2,2,3,4,5,6,6]

    dct = dict.fromkeys(lst,0)

    for item in lst:
        dct[item]=int(dct[item])+1

    print(dct)

    dct2 = {k for k,v in dct.items() if(v>1)}

    #print(dct2.__class__)

    print(dct2)

    for k,v in dct.items():
        print("number of duplicates for {} is {}".format(k,v))

countDupHash()