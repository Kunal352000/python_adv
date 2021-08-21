class student:
    col_name="svvv"#static variable
    def __init__(self):
        self.sid=101#instance variable
        self.sname="kunal"#instance varibale
    @classmethod
    def col_info(cls):
        cls.col_add="indore"#static variable
        print(student.col_name)
        print(student.col_add)
        print(cls.col_add)
    def std_info(self):
        print(self.sid)
        print(self.sname)
        print(student.col_name)
        print(student.col_add)
        #print(cls.col_add)#error bcoz we are accesing ouside of classmethod by cls
    @staticmethod
    def msg():
        print("Hey kunal good evening")
s1=student()
s1.col_info()
student.col_info()
s1.std_info()
s1.msg()
student.msg()
