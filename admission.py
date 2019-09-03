class student:
	def __init__(self,sid,marks,age):
		self.sid=sid
		self.marks=marks
		self.age=age
	def validate_marks(self):
		if(self.marks>=0 and self.marks<=100):
			print("valid marks")
		else:
			print("invalid marks")
	def validate_age(self):
		if(self.age>20):
			print("valid age")
		else:
			print("invalid age")
	def check(self):
		if self.marks>65 and self.age>20:
			print("qualified")
		else:
			print("not qualified")
	def display(self):
		print("student id=",self.sid)
		print("Marks=",self.marks)
		print("age=",self.age)
a=student(54,76,23)
b=a.validate_marks()
a.display()
a.check()
