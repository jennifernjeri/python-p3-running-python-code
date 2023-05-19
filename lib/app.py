print ("Hello world!")
print("Hello sun!")
print("Hello sky!")
print("Hello world!", end=" ")
print("Hello sun!", end="!! ")
print("Hello sky!", end="!!!\n")

# Concantenation is joining two variables to create a single output
# Scope is the region where the variable is being created
#Global variables are declared outside a function and can be used with any function
#Local variables are declared inside a function and can only be declared by that specific function

pass_mark = 50
def student_grade(marks):

    if marks < pass_mark:
       print ("Fail")
    elif marks == pass_mark:
        print ("Pass")
    else:
        print ("Distinction")

student_grade (int(input("Enter student marks")))

