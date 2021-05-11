from collections import defaultdict

words=['inch','cat','chin','bit','act']

def getGroupedAnagrams(words):
    temp = defaultdict(list)
    for word in words:
        temp[str(sorted(word))].append(word)
    anagrams = list(temp.values())
    groups = len(anagrams)
    print(groups)
    return groups

getGroupedAnagrams(words)