import functions

a = input("Enter boy's name:")
b = input("Enter girl's name:")

functions.wordsplitter(a,b)
l = functions.wordsplitter(a,b)[0]
h = functions.wordsplitter(a,b)[1]
x = 3
functions.counter(x,l,h)
