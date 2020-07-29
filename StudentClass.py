class Student:
    count = 0
    students = []

    @classmethod 
    def print(cls):
        print("------학생 목록-------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("--------- --------- -------")
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english 
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())

Student("윤인성",87,98,88,95) 
Student("연하진",84,64,76,86) 
Student("구지연",81,85,90,67) 
Student("나선주",63,74,58,80) 
Student("윤아린",44,79,45,69) 
Student("윤명월",77,78,79,89) 
Student("김미화",99,98,68,44) 
Student("김연화",35,77,54,88) 
Student("박아현",87,98,88,96) 
Student("서준서",80,79,56,97)



Student.print()


