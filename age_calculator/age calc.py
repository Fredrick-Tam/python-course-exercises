
# Tam Fredrick Kofi
# Date: 21/09/2014
# file: kofi.py
# UNI: fkt2105 
#
#***************************************

### question 3

### Python programme to find your age in days
   
### Greet the person  
print( '''Hello there, I hope you are fine!
Let me help me you to find your age in days''')
### Ask for name of person
print('Please what is your name?' )
name_of_person = raw_input( 'Your name please?')
if name_of_person == 'kofi':
    print( 'Welcome Mr.Tam')
else:
    print( 'Welcome new friend, my dear %s' %name_of_person)
print( '''Now, let us get down to business.
    Please enter your date of birth in the format year,month,day, numerically''' )
### get data from the person 
bd_y = input("Year: ")
bd_m = input("Month (1-12): ")
bd_d = input("Day: ")
### import date form datetime module
from datetime import date
### assign variable now to the current date
now = date.today()

birthdate = date(int(bd_y), int(bd_m), int(bd_d))
### assign variable ''age'' to result of calculation of age difference
age =  now-birthdate
print "Your age is %s" % age
### since minimum age is 110 years, no limitations are needed
