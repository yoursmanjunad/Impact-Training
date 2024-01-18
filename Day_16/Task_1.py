# This is a task file, in which we have to collect data from the user like
# 1. Employee Id
# 2. Employee First Name
# 3. Employee Second Name
# 4. Employee Phone Number

'''
have a class of employees with following data:
first name : string
second name :string
phone num :int

*prepare a 50 empolyee linkedlist
*sort the employee using first name in ascending
*serial number should be generated
*sort the list using phonenumber
'''
# Approach is first, create  class for the input of the number of users.
# After getting the input from the user, insert them into the list.
class Employee:
    def __init__(self, emp_Id, emp_FName, emp_SName, emp_Phone):
        self.emp_Id = emp_Id
        self.emp_FName = emp_FName
        self.emp_SName = emp_SName
        self.emp_phone = emp_Phone
    def __str__(self):
        # Employee = self.emp_Id
        # Employee = self.emp_FName
        # Employee = self.emp_SName
        # Employee = self.emp_phone
        iD = 'empId'+ str(self.emp_Id)
        fName = "emp First Name" + str(self.emp_FName)
        sName = "Emp Second Name "+ str(self.emp_SName)
        ePhone = "Emp Phone- : "+str(self.emp_phone)

class EmpLL:
    def __init__(self):
        self.head = None
    def insertEmp(self,empProp):
        nn = (empProp['emp_Id'], empProp['emp_FName'], empProp['emp_SName'], empProp['emp_Phone'])
        nn.next = self.head
        self.head = nn
    def printingEmp(self):
        temp = self.head
        while temp:
            print(f"Emp ID: {temp.emp_id}, Emp Name: {temp.emp_FName} {temp.emp_SName}, Emp Age: {temp.emp_Phone}")
            temp = temp.next
worker = EmpLL()
empProp = Employee(emp_Id=242, emp_FName="Manjunath", emp_SName="Irukulla", emp_Phone=323536725)
worker.insertEmp(empProp)
worker.printingEmp()

