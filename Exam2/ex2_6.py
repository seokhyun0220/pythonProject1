class person:
    def __init__(self, name):
        self.name = name

    def work(self):
        print('%s working...' % self.name)

class student(person):
    def work(self):
        print('%s studying...' % self.name)

class Developer(person):
    def work(self):
        print('$s programming...' % self.name)

if __name__=='__main__':

    obj1 = person('김유신')
    obj2 = student('김춘추')
    obj3 = Developer('장보고')

    people = [obj1, obj2, obj3]

    for person in people:
        person.work()