# Exercise 10.2
hourCount = dict()
lst = list()
fhand = open('mbox-short.txt')
#fhand = open('mbox.txt')

for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From': 
        tm = words[5]
        hrs = tm.split(':')
        hourCount[hrs[0]] = hourCount.get(hrs[0],0) +1

for key, val in hourCount.items():
    lst.append((key,val))
    
#print lst
lst.sort()

for key, val in lst:
    print key, val


