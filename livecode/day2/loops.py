# while loop

# usrInput = input("If you enter any value , it will be printed, 0 will be exit: ")
# while(usrInput != "0"):
#     print(usrInput)
#     usrInput = input("Enter other value: ")

# print("You've exited the system !!")

# Write a while loop to guess a predefined number
# once the input is equal to the predefined number 
# stop the while and print congrats

number = input("Hello, try to guess which number is correct: ")
counter=1
while(number != "5" and counter !=5):
    counter = counter + 1
    print("This is wrong, and you still have", 6-counter, "trails left")
    number = input("Try again: ")



if(number == "5"):
    print("Congratulations, you have guessed it!!")
else:
    print("GAME OVER !!!")