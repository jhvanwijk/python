# Exercise 10.3
import string
letterCount = dict()
lst = list()
#fhand = open('romeo.txt')
fhand = open('wordstest.txt')

for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    if len(words) == 0: continue
    for word in words:
        letters = tuple(word)
        for letter in letters:
            if letter not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']: continue
            letterCount[letter] = letterCount.get(letter,0) +1

for letter, count in letterCount.items():
    lst.append((count,letter))

lst.sort(reverse=True)

for count, letter in lst:
    print letter, count
    
    
# Random, I know! This is one of the recommended sales email subject lines to get prospects to open, read and respond to your email.... proof is in the pudding, right?

Assuming this works, I can probably ask you the following list of questions and know you will read it. Ready? Here we go:

question1 = raw_input('How are you doing? ')
question2 = raw_input('Excited about the year? ')
question3 = raw_input('Are you in Cape Town already? ')
question4 = raw_input('How does it feel to be a "free man"? ')
question5 = raw_input('Missing Moore? ')
question6 = raw_input('Missing ME?! ')
question7 = raw_input(Rather don't answer the last question - don't think I can handle the rejection right now...

:-) OK,