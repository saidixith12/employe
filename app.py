emp_name=input('name of the employee=')
emp_slno=input('enter the slno given by the company= ')
emp_age=int(input("enter the age of the employee="))
join=input('new or  old:')


if join=='n':
    print("employee's is a new joine")
else:
    print('employee is a old joine')

emp_sal=input('enter the salary=')

if emp_sal>='50000':
    print('employee is in higher post')


elif emp_sal<='30000':
    print('employee is in lower post')
else:
    print('in valid entry')




