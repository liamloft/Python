import pickle
import nester
import os
os.chdir('\\users\\liaml\\desktop\\python learn\\HeadFirstPython\\CH4')
man = ['liam' , 'jack' , 'kyle' ,['tom','andrew' ,['fleming']]]
other = [ str(3)+'tres', 'happy' , 'tigres']
try:
    with open('man_data2pickle.txt','wb') as man_file, open('other_data2pickle.txt','wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print ('File error: ' + str(err))
except picle.PickleError as perr:
    print('Pickling error ' + str(perr))
    
    
