# Have the function LetterCount(str) take the str parameter being passed and return the first word with the
#     greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest
#     because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating '' \
#     ''letters return -1. Words will be separated by spaces.



def repeat(word):

    sword = sorted(word)

    wtbl = dict.fromkeys(sword,0)

    for char in sword:
        wtbl[char] = wtbl[char] + 1

    wtbl2 = [v for v in wtbl.values() if v>1]

    return sum(wtbl2)



def LetterCount(str):

    lst = str.split(" ")

    htbl = {}


    for word in lst:
        htbl[word]=repeat(word)

    return max(htbl, key=htbl.get)

print(LetterCount("Today is greatest day ever"))