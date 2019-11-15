# Exercise 7.1
#fname = raw_input('Enter a file name: ')
#fhand = open(fname)
#for line in fhand:
#    line = line.rstrip().upper()
#    print line

# Exercise 7.2
#fname = raw_input('Enter a file name: ')
#fname = 'mbox-short.txt'
#fhand = open(fname)
#count = 0
#spam = 0
#conf = 0
#for line in fhand:
#    line = line.rstrip()
#    spam = line.find('X-DSPAM-Confidence:')
#    if spam == -1:
#        continue
#    count = count + 1
#    spacePos = line.find(' ',spam)
#    conf = conf + float(line[spacePos + 1:spacePos + 7])
#print 'Average spam confidence: ', conf/count 

# Exercise 7.3
fname = raw_input('Enter a file name: ')
#fname = 'mbox-short.txt'
try:
    fhand = open(fname)
    
    count = 0
    spam = 0
    conf = 0
    for line in fhand:
        line = line.rstrip()
        spam = line.find('X-DSPAM-Confidence:')
        if spam == -1:
            continue
        count = count + 1
        spacePos = line.find(' ',spam)
        conf = conf + float(line[spacePos + 1:spacePos + 7])
    print 'Average spam confidence: ', conf/count 
    
except:
    if fname == 'na na boo boo':
        print "NA NA BOO BOO TO YOU - You have been Prank'd"
    else:
        print 'File cannot be opened:', fname