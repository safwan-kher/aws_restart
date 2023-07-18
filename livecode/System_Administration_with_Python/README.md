# System Administration with Python

This lab provides an overview of how to use Python for system administration tasks. It covers the use of Python's `os.system()` and `subprocess.run()` functions to execute Bash commands.

## Lab Setup

1. Start the lab environment.
2. Access the AWS Cloud9 IDE.
3. Create a new Python file for the exercises.
4. Open a terminal session in the Cloud9 IDE.

## Exercise 1: Using os.system

The `os.system()` function allows you to run Bash commands from Python. The function takes a string argument which is the Bash command to be executed.

```python
import os
os.system("ls")
```

This code imports the `os` module and runs the `ls` command, which lists the contents of the current directory.

## Exercise 2: Using subprocess.run

The `subprocess.run()` function is a more powerful alternative to `os.system()`. It can spawn new processes, connect to input/output/error pipes, and obtain return codes.

```python
import subprocess
subprocess.run(["ls"])
```

This code imports the `subprocess` module and runs the `ls` command. The command is passed as a list of arguments.

## Exercise 3: Using subprocess.run with two arguments

The `subprocess.run()` function can take a list of arguments. This allows you to pass options to the Bash command.

```python
subprocess.run(["ls","-l"])
```

This code runs the `ls` command with the `-l` option, which displays the directory contents in a long listing format.

## Exercise 4: Using subprocess.run with three arguments

You can pass multiple arguments to the `subprocess.run()` function. This allows you to specify the command, options, and arguments.

```python
subprocess.run(["ls","-l","README.md"])
```

This code runs the `ls` command with the `-l` option on the `README.md` file.

## Exercise 5: Retrieving system information

The `subprocess.run()` function can be used to run any Bash command. This includes commands that retrieve system information.

```python
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
```

This code runs the `uname` command with the `-a` option, which displays all system information.

## Exercise 6: Retrieving information about disk space

The `subprocess.run()` function can also be used to run commands that retrieve disk space information.

```python
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
```

This code runs the `ps` command with the `-x` option, which displays information about the active processes.

## Conclusion

This lab demonstrated how to use Python for system administration tasks. The `os.system()` and `subprocess.run()` functions allow you to execute Bash commands from Python, providing a powerful tool for automating system administration tasks.