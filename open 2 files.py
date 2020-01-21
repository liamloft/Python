import nester
import os
os.chdir('\\users\\liaml\\desktop\\python learn\\HeadFirstPython\\CH4')
man = [ "this is what i am going to save to 1 file" ]
other = [ "this is 2" , ['liam' , 'jack'] , 'and i can nest these values as well' ]
try:
    with open('man_data2.txt','w') as man_file, open('other_data2.txt','w') as other_file:
        nester.print_lol(man, fh=man_file)
        nester.print_lol(other, fh=other_file)
except IOError as err:
    print ('File error: ' + str(err))
    
