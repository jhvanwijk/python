# Exercise 4.1
#import random

#for i in range(10) :
#    x = random.random()
#    print x

# Exercise 4.2 & 4.3
#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

#def print_lyrics():
#    print "I'm a lumberjack, and I'm OK."
#    print "I sleep all night and I work all day."

#repeat_lyrics()

# Exercise 4.4
#"def" indicates that the indented section of code to follow is stored for later

# Exercise 4.5
# ABC Zap ABC

# Exercise 4.6
#def computepay (hrs, rate):
#    earnings = hrs * rate
#    return earnings

#hours = raw_input("Enter Hours: ")
#hours = float(hours)
#try:
#    float(hours) and True
#    rates = raw_input("Enter Rates: ")
#    rates = float(rates)
#    if float(hours) > 40.0 :
#        hours = ((hours - 40) * 1.5) + 40
#        pay = computepay(hours,rates)
#    else :
#        pay = computepay(hours,rates)
#    print "Pay:", pay
#except:
#    print 'Error, please enter a numeric input'

# Exercise 4.7
def computegrade (point):
    if point > 0.9 :
        x = 'A'
    elif point <= 0.9 and point > 0.8 :
        x = 'B'
    elif point <= 0.8 and point > 0.7 :
        x = 'C'
    elif point <= 0.7 and point > 0.6 :
        x = 'D'
    else :
        x = 'F'
    return x

score = raw_input("Please enter a score between 0.0 and 1.0: ")

try :
    score = float(score)
    if score >= 0.0 and score <= 1.0 :
        print "The student's grade is a", computegrade(score)
    else :
        print "The score entered is out of range"
except :
    print "A bad score was entered"