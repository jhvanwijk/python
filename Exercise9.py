#################################
#           Exercise 9          #
#################################

# Exercise 9.1
#dictionary = dict()
#counter = 0
#fhand = open('words.txt')


#for line in fhand:
#    words = line.split()
#    for word in words:
#        if word in dictionary: continue
#        counter = counter + 1
#        dictionary[word] = counter
    
#print dictionary
    
    
# Exercise 9.2
#dictionary = dict()
#fhand = open('mbox-short.txt')


#for line in fhand:
#    words = line.split()
#    if len(words) != 0 and words[0] == 'From': 
#        day = words[2]
#        dictionary[day] = dictionary.get(day,0) +1
    
#print dictionary 

# Exercise 9.3
dictionary = dict()
domain = dict()
mostFreqEmail = None
count = 0
fhand = open('mbox-short.txt')
#fhand = open('mbox.txt')


for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From': 
        email = words[1]
        dictionary[email] = dictionary.get(email,0) +1
        # Exercise 9.5... continuation of # Exercise 9.3
        d = email.find('@')
        domain[email[d+1:]] = domain.get(email[d+1:],0) + 1

#print dictionary 

# Exercise 9.4... continuation of # Exercise 9.3
for email in dictionary:
    if mostFreqEmail is None or dictionary[email] > dictionary[mostFreqEmail]:
        mostFreqEmail = email

print domain