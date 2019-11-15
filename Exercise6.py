# Execrise 6.1
#fruit = "banana"
#length = len(fruit)
#letterPos = -1
#while letterPos >= -length:
#    print fruit[letterPos]
#    letterPos = letterPos - 1

#for char in fruit:
#    print char

# Execrise 6.2
# fruit[:] will return the whole word

# Execrise 6.3
#def wordCount (string, letter):
#    count = 0
#    for char in string:
#        if char == letter:
#            count = count + 1
#    return count

#print wordCount(fruit, "n")

# Exercise 6.5
str = 'X-DSPAM-Cofidence: 0.8475'
spacePos = str.find(' ')
print float(str[spacePos + 1:])

# Exercise 6.6
