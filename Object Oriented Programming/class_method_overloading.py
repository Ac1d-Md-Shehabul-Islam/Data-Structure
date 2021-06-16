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

  @classmethod
  def overload(cls, info):
    name, id = info.split('-')
    obj = cls(name,id)
    return obj

#============================================================================

s1 = Student('siam',4)
s2 = Student('bob',20)
s3 = Student.overload('Jack-90')
s3.details()