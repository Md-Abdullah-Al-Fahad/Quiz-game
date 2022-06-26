print("Welcome to Computer Basic Quiz.")
start = input("Start the game? (y/n) - ")

if start == 'y':
    print("Get ready!")
elif start == 'n':
    print("Exited.")
    quit()
else:
    print("Please try again!")
    quit()


score = 0

answer1 = input("The first web browser is _______?	").upper()
if answer1 == 'MOSAIC':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("Name of 1st electronic computer? ").upper()
if answer2 == 'ENIAC':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("BIOS stands for _______?	").upper()
if answer3 == 'BASIC INPUT OUTPUT SYSTEM':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("Who is the father of Computer science?	").upper()
if answer4 == 'CHARLES BABBAGE':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer5 = input("Where are the CPU and memory located?	").upper()
if answer5 == 'MOTHERBOARD':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You scored {score} out of 5 questions")
print("You answered", score / 5 * 100, "% questions correctly.")