class Student:
	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name
	def setMarks(self,marks):
		self.marks=marks
	def getMarks(self):
		return self.marks
n=int(input("Enter the number of Student: "))
for i in range(n):
	name=(input("Enter student name: "))
	marks=int(input("Enter {} Marks: ".format(name)))
	s=Student()
	s.setName(name)
	s.setMarks(marks)
	print("Student name:",s.getName())
	print("Student marks:",s.getMarks())