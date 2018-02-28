def wordsplitter(a,b):
    l =[]
    h= []
    for i in a:
        l.append(i)
    for i in b:
        h.append(i)
    return l,h

def counter(x,l,h):
    x = x -1
    if x== 0:
        finder(l,h)
    for i in h:
        for j in l:
            if i == j:
                l.remove(i)
                h.remove(i)
                counter(x,l,h)
                break
    
def finder(l,h):
    l = l + h
    fl = len(l)
    flame =['f','l','a','m','e','s']
    flames = {'f':"Friends",'l':"Love",'a':"Affection",'m':"Marriage",'e':'Enemy','s':"Sister"}
    s = 6 
    i= 0
    while s > 1:
        i = i+fl
        while i > s:
            i = i - s
        del flame[i-1]
        if s == 2:
            print(flame[0],' ',flames[flame[0]])
        s = s - 1
    