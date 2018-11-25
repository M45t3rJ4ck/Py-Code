class Student(object):
        def __init__(self, age, name, gender, grades):
                self.age = age
                self.name = name
                self.gender = gender
                self.grades = grades
        def compute_average(self):
                average = sum(self.grades)/len(self.grades)
                print("The average for student " + self.name + " is " + str(average))
        def check_male(self):
                if self.gender == male:
                        return True
                else:
                        return False

philani = Student(20, "Philani Sithole", "male", [64,65])
sarah = Student(19, "Sarah Jones", "female", [82,58])
riaan = Student(35, "Willem Voges", "male", [69,69])
anni = Student(55, "Anni Pompies", "female", [93, 96])

philani.compute_average()
sarah.compute_average()
riaan.compute_average()
anni.compute_average()
