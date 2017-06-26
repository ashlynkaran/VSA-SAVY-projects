# Classes

# defining a class called Person, which is a type of object
class Person(object):
    # defining the init method for the class person with a name
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setAge(self, age):
        self.age = int(age)

    def __str__(self):
        ans = self.name + " is age "+ str(self.age)
        # return a string
        return ans

    def getAge(self):
        return self.age

person1 = Person("Ashlyn", 26)
person1.setAge(27)
print str(person1)

class VSAstudent(Person):
    def set_class(self, class_name):
        self.class_name = class_name
    def get_class(self, class_name):
        return self.class_name
    def compareAge(self, otherStudent):
        if self.age > otherStudent.age:
            return self.name + "is older than " + otherStudent.name
        else:
            return self.name + "is younger than " + otherStudent.name

person2 = VSAstudent('Santosh', 15)
person2.set_class('programming')

print person2
print person2.class_name

person3 = VSAstudent('Damian', 13)

print person2.compareAge(person3)
