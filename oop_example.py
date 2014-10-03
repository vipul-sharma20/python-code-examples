# Object Oriented Programming example
class Employee:  # Common base class for all employees
   
   empCount = 0
   def __init__(self, name, salary):  # initializing instance of the class
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

# This would create first object of Employee class
emp1 = Employee("Lorem", 2000)

# This would create second object of Employee class
emp2 = Employee("Ipsum", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employees %d" % Employee.empCount
