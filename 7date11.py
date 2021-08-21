class student:
    col_name="igloabl"
    col_add="Ameerpat"
    def std_info(self,sid,sname):
        self.sid=sid
        self.sname=sname
        print(self.sid)
        print(self.sname)
        print(student.col_name)
        print(student.col_add)
s1=student()
s1.std_info(101,"kuunaBhai")
s2=student()
s2.std_info(102,"shivambaba")
