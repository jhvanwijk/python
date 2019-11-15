# EXERCISE 8 #
# Choose exercise numbers
#exercise = raw_input('I want to do Exercise8.[?]')
#print exercise
#if exercise == 1:
#    # Exercise 8.1
#    def chop(t):
#       del t[0]
#        del t[len(t)-1]

#    def middle(t):
#        length = len(t);
#        return t[1:length-1]

#    numbers = [1,2,3,4,5,6,7,8,9,0]

#    print 'Original Numbers list:', numbers
#    print 'Result of the Middle function:', middle(numbers)
#    print 'Numbers list after Middle function:',numbers
#    print 'Result of Chop function:',chop(numbers)
#    print 'Numbers list after Chop function:',numbers
#print 'i am here'
#if exercise == 2:
    # Exercise 8.2
#fhand = open('mbox-short.txt')

#for line in fhand:
    #words = line.split()
    #print 'Debug: ', words
    #if len(words) ==0: continue
    #if words[0] != 'From': continue
    #print words[2]
    # Next code is for Exercise 8.3
    #if len(words) > 0 and words[0] == 'From': print words[2]
    
# Exercise 8.4
#fhand = open('romeo.txt')
#wordList = []
#for line in fhand:
#    words = line.split()
#    for word in words:
#        if word in wordList: continue
#        wordList.append(word)
#wordList.sort()
#print wordList

# Exercise 8.5
#fhand = open('mbox-short.txt')
#count = 0
#for line in fhand:
#    words = line.split()
#    if len(words) > 0 and words[0] == 'From':
#        print words[1]
#        count = count +1
#print count

# Exercise 8.6
maximum = 0
minimum = 0
valueList = []

while True:
    valueEntered = raw_input('Please enter a number: ')
    try:
        if valueEntered == 'Done' or valueEntered == 'done': break
        valueList.append(valueEntered)

    except:
        print 'Bad data'

print 'Maximum: ' + max(valueList)
print 'Minimum: ' + min(valueList)
