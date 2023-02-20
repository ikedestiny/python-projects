#object oriented programming

class student:
    def __init__(self, name, age, nationality, score):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.score = score



class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print("Course already full")

    def get_average(self):
        value = 0
        for student in self.students:
            value+= student.score

        return value/len(self.students)
    
std1 = student("Isaac", 19, "Nigerian", 91)
std2 = student("favor", 18, "Ghana", 88)
std3 = student("Joy", 17, "Serre", 100)
std4 = student("Isa", 19, "Nigerian", 71)
std5 = student("fav", 18, "Ghana", 85)
std6 = student("Josss", 17, "Serre", 83)

std_list = [std1,std2, std3, std4, std5, std6]
physics = course("Physics", 5)
maths = course("maths",3)


for item in std_list:
    physics.add_student(item)
    maths.add_student(item)

print(physics.get_average())
print(maths.get_average())