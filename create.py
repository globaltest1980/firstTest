from sys import argv

script, myFile = argv

def see_list(list1):
    print new_file.read()

def review(list1):
    list1.seek(0)

def add_number(newNumber, list1):
    print newNumber, list1.readline()



print "Let's create a new File."
print "The file name is %s."  % myFile


new_file = open (myFile, 'w')

print "Print the 4 car's brands"

line1 = raw_input()
line2 = raw_input()
line3 = raw_input()
line4 = raw_input()

new_file.write(line1)
new_file.write('\n')
new_file.write(line2)
new_file.write('\n')
new_file.write(line3)
new_file.write('\n')
new_file.write(line4)
new_file.write('\n')

print "\nNow, let's review your list.\n"

new_file = open(myFile)
see_list(new_file)

print "Awesome!!! "
print "What about if we enumerate your list"
print raw_input('Press ENTER')

review(new_file)


number = 1
add_number(number, new_file)

number = number + 1
add_number(number, new_file)

number = number + 1
add_number(number, new_file)

number = number + 1
add_number(number, new_file)

new_file.close()
