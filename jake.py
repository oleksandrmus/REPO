class Employee:
    def __init__(self,salary,name ):
        self.salary = salary
        self.name = name

    def __str__(self):
        return  "Worker {} got  salary {}".format(self.salary ,self.name)
employ1 = Employee ("Jake","100k")
employ2 = Employee ("Anand","120")
print("{}".format(employ1))
print("{}".format (employ2))