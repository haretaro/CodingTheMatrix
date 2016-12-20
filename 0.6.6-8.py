from functools import reduce

with open('stories_small.txt') as f:
    stories = f.read().split('\n')
    dic = {}
    for (i,story) in enumerate(stories):
        for word in story.split(' '):
            if word not in dic.keys():
                dic[word] = set()
            dic[word] |= {i}

def orSearch(query):
    result = set()
    for word in query:
        result |= dic[word]
    return result

print(orSearch(['WASHINGTON', 'AID']))

def andSearch(query):
    results = map(lambda k: dic[k], query)
    return reduce(lambda x,y: x & y, results)

print(andSearch(['WASHINGTON', 'AID']))

