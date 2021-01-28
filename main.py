"""
-------------------------------------------------------------------------------
Name:		main.py
Purpose: Multiple choice review quiz of course content

Author:	 Wang.J

Created:	01/14/2021
-------------------------------------------------------------------------------
"""
# title
print("*** Multiple Choice Computer Studies Review Quiz ***")

# name
name = input("Enter your first and last name: ")

# confirmation to start quiz with instruction
question = input(name + ", Type 'READY' to start the quiz: ")
confirmation = "READY"

while question != confirmation:
    question = input("Type 'READY' when you are ready: ")

if question == confirmation:
    print("Read each question carefully and answer each with one of the following lowercase letters. Good Luck! ")

# variables
answers_correct = 0
answers_incorrect = 0

# get answers for the questions and output correct or incorrect through if statements.
# question one
q_one = input("\n 1. What is the computer processing sequence of events in order? \n  a) Input, process, output, storage. \n  b) Storage, input, process, output. \n  c) Process, output, input, storage. \n Enter Answer: ")

while q_one != "a" and q_one != "b" and q_one != "c":
    q_one = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")
  
if q_one == ("a"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1

# question two
q_two = input("\n 2. How many bits are in 1 byte? \n  a) 8 bits. \n  b) 7 bits. \n  c) 10 bits. \n Enter Answer: ")

while q_two != "a" and q_two != "b" and q_two != "c":
  q_two = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_two == ("a"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1


# question three
q_three = input("\n 3. How many bytes are in 1 Kilobyte (KB)? \n  a) 800 bytes. \n  b) 1024 bytes. \n  c) 2000 bytes. \n Enter Answer: ")

while q_three != "a" and q_three != "b" and q_three != "c":
  q_three = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_three == ("b"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'b'. ")
  answers_incorrect += 1

# question four
q_four = input("\n 4. How many bits are in 1 megabit? \n  a) 10 bits. \n  b) 1 million bits. \n  c) 1000 bits. \n Enter Answer: ")

while q_four != "a" and q_four != "b" and q_four != "c":
  q_four = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_four == ("b"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'b'.")
  answers_incorrect += 1


# question five
q_five = input("\n 5. DPI (Dots per Inch) and PPI (Pixels Per Inch) measures how many points of information can be captured in a _____? \n  a) centimeter. \n  b) meter. \n  c) inch. \n Enter Answer: ")

while q_five != "a" and q_five != "b" and q_five != "c":
  q_five = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_five == ("c"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'c'.")
  answers_incorrect += 1


# question six
q_six = input("\n 6. What does CPU stand for? \n  a) Circle process unit. \n  b) Central processing unit. \n  c) Central professional units. \n Enter Answer: ")

while q_six != "a" and q_six != "b" and q_six != "c":
  q_six = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_six == ("b"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'b'.")
  answers_incorrect += 1


# question seven
q_seven = input("\n 7. What is the purpose of the motherboard? \n  a) It serves a connection between the various different parts of a computer system. \n  b) It stores data. \n  c) It gives power to the computer. \n Enter Answer: ")

while q_seven != "a" and q_seven != "b" and q_seven != "c":
  q_seven = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_seven == ("a"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1

# question eight
q_eight = input("\n 8. What does RAM stand for? \n  a) Random access memory. \n  b) Real accessible memory. \n  c) Random application memory. \n Enter Answer: ")

while q_eight != "a" and q_eight != "b" and q_eight != "c":
  q_eight = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_eight == ("a"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1

# question nine
q_nine = input("\n 9. Megahertz(MHz) & Gigahertz(GHz) measure what type of speed? \n  a) Downloading speed. \n  b) Updating speed. \n  c) Processing speed. \n Enter Answer: ")

while q_nine != "a" and q_nine != "b" and q_nine != "c":
  q_nine = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_nine == ("c"):
  print("Correct!")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'c'.")
  answers_incorrect += 1


# question ten
q_ten = input("\n 10. What is the primary function of random access memory (RAM)? \n  a) It provides a temporary storage space for programs that are not actively being used. \n  b) It provides a permanent storage space for the computer. \n  c) It provides a temporary storage space for programs that are in the act of using. \n Enter Answer: ")

while q_ten != "a" and q_ten != "b" and q_ten != "c":
  q_ten = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_ten == ("c"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'c'.")
  answers_incorrect += 1


# question eleven
q_eleven = input("\n 11. What is the primary function of hard drives? \n  a) Storing data. \n  b) Updating files. \n  c) Providing power. \n Enter Answer: ")

while q_eleven != "a" and q_eleven != "b" and q_eleven != "c":
  q_eleven = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_eleven == ("a"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1


# question twelve
q_twelve = input("\n 12. What is the CPU performance measured in? \n  a) Megahertz(MHz). \n  b) Gigahertz(GHz). \n  c) Hertz(H). \n Enter Answer: ")

while q_twelve != "a" and q_twelve != "b" and q_twelve != "c":
  q_twelve = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_twelve == ("b"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'b'.")
  answers_incorrect += 1


# question thirteen
q_thirteen = input("\n 13. How many processors are on a dual core processor? \n  a) Three. \n  b) Two. \n  c) Four. \n Enter Answer: ")

while q_thirteen != "a" and q_thirteen != "b" and q_thirteen != "c":
  q_thirteen = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_thirteen == ("b"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'b'.")
  answers_incorrect += 1

# question fourteen
q_fourteen = input("\n 14. What is the primary unit of storage? \n  a) Gb/Tb. \n  b) MHz/GHz. \n  c) MM/CM. \n Enter Answer: ")

while q_fourteen != "a" and q_fourteen != "b" and q_fourteen != "c":
  q_fourteen = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_fourteen == ("a"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1

# question fifteen
q_fifteen = input("\n 15. What does DRAM stand for? \n  a) Dynamic random access memory. \n  b) Data random access memory. \n  c) Dynamic random application memory. \n Enter Answer: ")

while q_fifteen != "a" and q_fifteen != "b" and q_fifteen != "c":
  q_fifteen = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_fifteen == ("a"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1


# question sixteen
q_sixteen = input("\n 16. What is a url? \n  a) A complex phone number. \n  b) Phone book. \n  c) Web address you type into a browser to reach a website. \n Enter Answer: ")

while q_sixteen != "a" and q_sixteen != "b" and q_sixteen != "c":
  q_sixteen = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_sixteen == ("c"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'c'.")
  answers_incorrect += 1


# question seventeen
q_seventeen = input("\n 17. What is an IP address? \n  a) A series of numbers that tells your computer where to find the information you're looking for. \n  b) A web address you type into a browser to reach a website. \n  c) Phone book. \n Enter Answer: ")

while q_seventeen != "a" and q_seventeen != "b" and q_seventeen != "c":
  q_seventeen = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_seventeen == ("a"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1

# question eighteen
q_eighteen = input("\n 18. What is the least dangerous malware? \n  a) Adware. \n  b) Trojan. \n  c) Spyware. \n Enter Answer: ")

while q_eighteen != "a" and q_eighteen != "b" and q_eighteen != "c":
  q_eighteen = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_eighteen == ("a"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'a'.")
  answers_incorrect += 1

# question nineteen
q_nineteen = input("\n 19. What is the most dangerous malware? \n  a) Rootkit.  \n  b) Ransomware.  \n  c) Trojan. \n Enter Answer: ")

while q_nineteen != "a" and q_nineteen != "b" and q_nineteen != "c":
  q_sixteen = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_nineteen == ("c"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'c'.")
  answers_incorrect += 1

# question twenty
q_twenty = input("\n 20. What does GPU stand for? \n  a) Graphics Profesional Universe. \n  b) General Professional Unit. \n  c) Graphics Processing Unit. \n Enter Answer: ")

while q_twenty != "a" and q_twenty != "b" and q_twenty != "c":
  q_twenty = input("Invalid Answer. Choose one of the following letters shown! Try Again.\n Enter Answer: ")

if q_twenty == ("c"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'c'.")
  answers_incorrect += 1

# true and false questions
print("\n >>> Part 2 True or False Questions <<< \nPick 'True' if you think the statement is correct and 'False' if you think the statement is wrong.")

# question twenty one
q_twenty_one = input("\n 21. External storage allows users to store data separately from a computer’s main storage. \n  True \n  False \n Enter Answer: ")

while q_twenty_one != "True" and q_twenty_one != "False":
  q_twenty_one = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_one == ("True"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'True'.")
  answers_incorrect += 1

# question twenty two
q_twenty_two = input("\n 22. A pointing device is an input interface that allows a user to input spatial data to a computer. \n  True \n  False \n Enter Answer: ")

while q_twenty_two != "True" and q_twenty_two != "False":
  q_twenty_two = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_two == ("True"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'True'.")
  answers_incorrect += 1

# question twenty three
q_twenty_three = input("\n 23. The display monitor is an input device that displays the image taken from the storage device. \n  True \n  False \n Enter Answer: ")

while q_twenty_three != "True" and q_twenty_three != "False":
  q_twenty_three = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_three == ("False"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'False'.")
  answers_incorrect += 1

# question twenty four
q_twenty_four = input("\n 24. Speakers/Headphones output sounds from devices. \n  True \n  False \n Enter Answer: ")

while q_twenty_four != "True" and q_twenty_four != "False":
  q_twenty_four = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_four == ("True"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'True'.")
  answers_incorrect += 1

# question twenty five
q_twenty_five = input("\n 25. The keyboard is an output device that sends commands to the display monitor. \n  True \n  False \n Enter Answer: ")

while q_twenty_five != "True" and q_twenty_five != "False":
  q_twenty_five = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_five == ("False"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'False'.")
  answers_incorrect += 1

# question twenty six
q_twenty_six = input("\n 26. SSD is typically less expensive and slower than HDD. \n  True \n  False \n Enter Answer: ")

while q_twenty_six != "True" and q_twenty_six != "False":
  q_twenty_six = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_six == ("False"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'False'.")
  answers_incorrect += 1

# question twenty seven
q_twenty_seven = input("\n 27. Hz measures the refresh rate of the monitor. \n  True \n  False \n Enter Answer: ")

while q_twenty_seven != "True" and q_twenty_seven != "False":
  q_twenty_seven = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_seven == ("True"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'True'.")
  answers_incorrect += 1

# question twenty eight
q_twenty_eight = input("\n 28. Sound is measured in decibels. \n  True \n  False \n Enter Answer: ")

while q_twenty_eight != "True" and q_twenty_eight != "False":
  q_twenty_eight = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_eight == ("True"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'True'.")
  answers_incorrect += 1

# question twenty nine
q_twenty_nine = input("\n 29. GB measures how fast the monitor screen can switch between colours in milliseconds. \n  True \n  False \n Enter Answer: ")

while q_twenty_nine != "True" and q_twenty_nine != "False":
  q_twenty_nine = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_twenty_nine == ("False"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'False'.")
  answers_incorrect += 1

# question thirty
q_thirty = input("\n 30. The Auxiliary port allows the connection of the audio from one device to another. Ex. Headphones, speakers, microphones. \n  True \n  False \n Enter Answer: ")

while q_thirty != "True" and q_thirty != "False":
  q_thirty = input("Invalid Answer. Choose one of the following shown! Try Again.\n Enter Answer: ")

if q_thirty == ("True"):
  print("Correct.")
  answers_correct += 1
else:
  print("Incorrect. The correct answer was 'True'.")
  answers_incorrect += 1


# output the final score
total_questions = 30
print("\n >>>> Final Score <<<<")
print (name)
print("Your final score is " + str(answers_correct) + "/" + str(total_questions) + ".")

# calculate the average
average = round((answers_correct/total_questions) * 100)
print("Your average percentage is " + str(average) + "%.")

# feedback
if average >= 85:
  print("Excellent Work! You had " + str(answers_incorrect) + " incorrect answers out of " + str(total_questions) + ".")
elif average >= 70 and average <= 84:
  print("Good Job! You had" + str(answers_incorrect) + " incorrect answers out of " + str(total_questions) + ".")
else:
  print("Study harder next time, you had " + str(answers_incorrect) + " incorrect answers out of " + str(total_questions) + ".")

# end
print("Thank you for taking the online multiple choice computer studies review quiz. Have a good day!")