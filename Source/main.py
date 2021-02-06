from QuestionOne import Employee, Fulltime
from QuestionTwo import two
from QuestionThree import three



emp1 = Employee("Todd", "Chavez", 5.43, "Rock-Opera")
emp2 = Fulltime("Bojack", "Horseman", 8.34, "Film", 45)

print("Question One")
print("Number of employees is", str(Employee.total_employees))
emp2.average_salary()
emp2.service()

print("\n\nQuestion Two")
two()

print("\n\nQuestion Three")
three()
