from itertools import count


class student:
    id:int
    name:str
    course:str
    year:str

    def __init__(self,id,name,course,year):
        self.id = id
        self.name = name
        self.course = course
        self.year = year

class studentDAO:
    students = []

    def __init__(self,students):
        self.students = students

    def getStudentById(self,id:int)->student:
        for student in self.students:
            if student.id == id:
                return student
        return None

    def getIndexById(self,id:int):
        index:int = 0

        for student in self.students:
            if student.id == id:
                return index
            index+=1

        return None

    def updateStudentById(self,id,std):
        
        index = self.getIndexById(id)
        student = self.getStudentById(id)
        
        if index == None and student == None:
            self.students.append(std)
            return std
        self.students.insert(index,std)
        
        return std

########### MAIN PROGRAM ###############

students = []

print("========= STUDENT APPLICATION ========")
s1 = student(3,"MADHU","BCA","2015")
students.append(s1)
s2 = student(1,"PAVAN","BCOM","2014")
students.append(s2)
s3 = student(8,"YUVAN","BBA","2016")
students.append(s3)
s4 = student(12,"BALA","BCA","2018")
students.append(s4)

stddao = studentDAO(students)

print("++++++++++ GET INDEXBYID ++++++++++")
print(stddao.getIndexById(12))
print("================================")

print("++++++++++ GET STUDENTBYID ++++++++++")
std = stddao.getStudentById(12)
print("ID: "+str(std.id)+" NAME: " + std.name 
+ " COURSE: " + std.course + " YEAR: " 
+ std.year)
print("================================")

print("=============== UPDATE STUDENT BY ID =======")
s5 = student(12,"Dhanush","BCA","2018")
stddao.updateStudentById(12,s5)
print("============================")

print("++++++++++ GET STUDENTBYID ++++++++++")
std = stddao.getStudentById(12)
print("ID: "+str(std.id)+" NAME: " + std.name 
+ " COURSE: " + std.course + " YEAR: " 
+ std.year)
print("================================")
