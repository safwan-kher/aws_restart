# Python Debugger Lab

This lab is designed to introduce you to the Python Debugger (pdb), an interactive source code debugger for Python programs. You will learn how to use pdb to step through Python scripts and explore its basic features.

## Lab Overview

1. **Accessing the AWS Cloud9 IDE**: This is the integrated development environment (IDE) where you will write and debug your Python scripts.

2. **Creating your Python exercise File**: You will create a new Python file and save it in the `/home/ec2-user/environment` directory.

3. **Accessing the terminal session**: You will open a new terminal session in your AWS Cloud9 IDE.

4. **Exercise 1: Exploring the basic features of the AWS Cloud9 Python Debugger**: You will learn how to use the Python Debugger in AWS Cloud9 IDE. You will add breakpoints to your code, add watch expressions, and step through your code.

5. **Exercise 2: Using the Python Debugger**: You will practice using the Python Debugger with other labs.

## Steps

1. Start your lab environment and open the AWS Management Console.

2. Navigate to Services > Cloud9 and open your Cloud9 environment.

3. Create a new Python file by choosing File -> New from template -> Python File from the menu bar. Save this file as `debugger.py` in the `/home/ec2-user/environment` directory.

4. Open a new terminal session in your AWS Cloud9 IDE.

5. In the `debugger.py` file, add the following code:

```python
name = "John"
print("Hello " + name + ".")
age = 40
print(name + " is " + str(age) + " years old.")
```

6. Open the Debugger tab and add breakpoints to lines 1 and 4 of your code.

7. Add two watch expressions: `name` and `age`.

8. Run your program in Debug Mode. The program will stop at the breakpoints.

9. Use the Step Over icon to run line 1 and display the value of the `name` variable.

10. Use the blue arrow to resume the program. It will stop at line 4 and display the value of the `age` variable.

11. Use the blue arrow again to resume and end the program.

12. Practice using the Python Debugger with other labs.

By the end of this lab, you should be familiar with the basic features of the Python Debugger and how to use it to step through Python scripts.