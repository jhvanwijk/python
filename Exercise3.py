# Exercise 3.1
#hours = raw_input("Enter Hours: ")
#rates = raw_input("Enter Rates: ")
#if float(hours) > 40.0 :
#    pay = float(hours) * float(rates) * 1.5
#else :
#    pay = float(hours) * float(rates)
#print "Pay:", pay

# Exercise 3.2
#hours = raw_input("Enter Hours: ")
#try:
#    float(hours) and True
#    rates = raw_input("Enter Rates: ")
#    if float(hours) > 40.0 :
#        pay = float(hours) * float(rates) * 1.5
#    else :
#        pay = float(hours) * float(rates)
#    print "Pay:", pay
#except:
#    print 'Error, please enter a numeric input'

# Exercise 3.3
score = raw_input("Please enter a score between 0.0 and 1.0: ")
try :
    if float(score) >= 0.0 and float(score) <= 1.0 :
        if float(score) >= 0.9 :
            print "The student's grade is an A"
        elif float(score) < 0.9 and float(score) >= 0.8 :
            print "The student's grade is a B"
        elif float(score) < 0.8 and float(score) >= 0.7 :
            print "The student's grade is a C"
        elif float(score) < 0.7 and float(score) >= 0.6 :
            print "The student's grade is a D"
        else :
            print "The student's grade is a F"
    else :
        print "The score entered is out of range"
except :
    print "A bad score was entered"