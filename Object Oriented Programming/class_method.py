class Student:

  uni_name = 'BracU'

  def __init__(self,name,id):
    self.name = name
    self.id = id

  def details(self):
    print("Name:",self.name,"\nID:",self.id,"\nUniversity:",Student.uni_name)

  @classmethod
  def update_name(cls,new_name):
    Student.uni_name = new_name

#============================================================================

s1 = Student('Siam',11)
s2 = Student('Jack',49)
s1.details()
print("\n")
Student.update_name('Dhaka University')
s1.details()