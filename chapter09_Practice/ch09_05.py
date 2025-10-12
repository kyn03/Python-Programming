class Employee:
    empCount=0 #클래스변수

    def __init__(self, name, salary) :
        self.name=name
        self.salary=salary

        Employee.empCount+=1 #클래스변수값 변경

    def displayEmp(self):
        print(f"Name:{self.name}, Salary:{self.salary}")

emp1=Employee("kim", 5000) #객체생성
emp2=Employee("lee", 6000)

emp1.displayEmp() #직원 정보 출력
emp2.displayEmp()

print(f"Total employees: {Employee.empCount}") #전체 직원수 출력