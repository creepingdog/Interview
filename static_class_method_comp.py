import numpy.random as rd


class Student:
    def __init__(self, sid, fname=None, lname=None):
        self.sid = sid
        self.fname = fname
        self.lname = lname
        self.description = None
    #

    def describe(self):
        self.description = 'My name is {} and my student id is {}'.format(
            self.lname+','+self.fname, self.sid
        )
        print(self.description+'\n')
    #

    @staticmethod
    def randomize_id_static(fname, lname):
        sid = 'UKI'+str(rd.randint(low=1, high=10000)).zfill(6)
        student = Student(sid=sid, fname=fname, lname=lname)
        return student
    #

    @classmethod
    def randomize_id_class(cls, fname, lname):
        sid = 'UKI'+str(rd.randint(low=1, high=10000)).zfill(6)
        student = cls(sid=sid, fname=fname, lname=lname)
        return student
    #
#


s1 = Student('FFU000001', 'Joan', 'Wang')
print('s1 is {} instance of Student.'.format('an' if isinstance(s1, Student) else 'not an'))
s1.describe()


class Grad(Student):
    def __init__(self, sid, fname=None, lname=None, subject=None):
        super().__init__(sid=sid, fname=fname, lname=lname)
        self.subject = None
    #

    def research(self, subject):
        self.subject = subject
    #

    def describe(self):
        if self.subject is None:
            self.description = 'My name is {} and my student id is {}. I have not started my research yet'.format(
                self.lname + ',' + self.fname, self.sid
            )
        else:
            self.description = 'My name is {} and my student id is {}. I am doing research on {}'.format(
                self.lname+','+self.fname, self.sid, self.subject
            )
        #
        print(self.description+'\n')
    #
#


s2 = Grad('SMG000001', 'Jason', 'Zhang')
print('s2 is {} instance of Grad.'.format('an' if isinstance(s2, Grad) else 'not an'))
s2.describe()

s3 = Grad.randomize_id_static('Andrew', 'Lee')
print('s3 is {} instance of Grad.'.format('an' if isinstance(s3, Grad) else 'not an'))
s3.describe()

s4 = Grad.randomize_id_class('Angela', 'Cheng')
print('s4 is {} instance of Grad.'.format('an' if isinstance(s4, Grad) else 'not an'))
s4.describe()
