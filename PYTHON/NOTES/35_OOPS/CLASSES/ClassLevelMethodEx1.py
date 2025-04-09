# ClassLevelMethodEx1.py
class Student:
    @classmethod
    def getcrsdet(cls):  # Class Level Method
        cls.crs = "PYTHON"  # OR u write as Student.crs="PYTHON"
        cls.cnt = "INDIA"  # OR u write as Student.cnt="INDIA"

    def dispcrsdet(self):  # Instance Method
        print("Course=", Student.crs)
        print("Country=", Student.cnt)


# Main Program
Student.getcrsdet()  # Calling Class Level Method
s = Student()
s.dispcrsdet()  # Calling Instance Method
