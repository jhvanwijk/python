# Exercise 5.1
#total = 0
#count = 0
#average = 0

#while True:
#    valueEntered = raw_input("Enter a number: ")
#    try:
#        if valueEntered == "done":
#            break
#        total = total + float(valueEntered)
##        count = count + 1
#        average = total / count
#    except:
#        print "Bad data"
#print "Total value: ", total, "\nCount: ", count, "\nAverage value: ", average

# Exercise 5.2
total = 0
count = 0
maximum = 0
minimum = 0

while True:
    valueEntered = raw_input("Enter a number: ")
    try:
        if valueEntered == "done":
            break
        total = total + float(valueEntered)
        count = count + 1
        if maximum is None or valueEntered > maximum:
            maximum = valueEntered
        elif minimum is None or valueEntered < minimum:
            minimum = valueEntered
    except:
        print "Bad data"
print "Total value: ", total, "\nCount: ", count, "\nMaximum number: ", maximum, "\nMinimum number: ", minimum