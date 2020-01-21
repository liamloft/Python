import os
os.chdir('\\users\\liaml\\desktop\\python learn\\HeadFirstPython\\CH6')
from sanitize import sanitize
class AthleteList(list):
    def __init__(self, a_name, a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])
    
def get_coach_data1(filename):  
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0),templ))
    except IOError as ioerr:
        print('File error: '+ str(ioerr))
        return(None)


james = get_coach_data1('james2.txt')
julie = get_coach_data1('julie2.txt')
mikey = get_coach_data1('mikey2.txt')
sarah = get_coach_data1('sarah2.txt')


print(james.name + "'s fastest times are: "+str(james.top3()))
print(julie.name + "'s fastest times are: "+str(julie.top3()))
print(mikey.name + "'s fastest times are: "+str(mikey.top3()))
print(sarah.name + "'s fastest times are: "+str(sarah.top3()))
              
    
