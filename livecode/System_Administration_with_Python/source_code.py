# Import the os and subprocess modules
import os
import subprocess

# Exercise 1: Using os.system
# Run the 'ls' command using os.system
os.system("ls")

# Exercise 2: Using subprocess.run
# Run the 'ls' command using subprocess.run
subprocess.run(["ls"])

# Exercise 3: Using subprocess.run with two arguments
# Run the 'ls' command with '-l' option using subprocess.run
subprocess.run(["ls","-l"])

# Exercise 4: Using subprocess.run with three arguments
# Run the 'ls' command with '-l' option on 'README.md' file using subprocess.run
subprocess.run(["ls","-l","README.md"])

# Exercise 5: Retrieving system information
# Define the command and its argument
command="uname"
commandArgument="-a"
# Print the command that will be executed
print(f'Gathering system information with command: {command} {commandArgument}')
# Run the command using subprocess.run
subprocess.run([command,commandArgument])

# Exercise 6: Retrieving information about disk space
# Define the command and its argument
command="ps"
commandArgument="-x"
# Print the command that will be executed
print(f'Gathering active process information with command: {command} {commandArgument}')
# Run the command using subprocess.run
subprocess.run([command,commandArgument])