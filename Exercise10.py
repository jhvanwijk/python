# Exercise 10.1
emailCount = dict()
lst = list()
#fhand = open('mbox-short.txt')
fhand = open('mbox.txt')

for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From': 
        #email = words[1]
        emailCount[words[1]] = emailCount.get(words[1],0) +1

for email, count in emailCount.items():
    lst.append((count,email))
    
#print lst
lst.sort(reverse=True)

for count, email in lst[:1]:
    print email, count


