# This questionnaire was created by Sabrina Palis
# during the Bertelsmann Scholarship Challenge 2019

import random

# The Quiz class consists of a question, a correct answer and
# the wrong answers. 
class Quiz:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.correctAnswer = correctAnswer
        self.otherAnswers = otherAnswers

# List of Quiz objects.
quizList = [Quiz("What program lets you interact with the shell?", "the Terminal program", ["Paint", "Internet Explorer"]),
Quiz("What are Windows, macOS, and Linux?", "Operating systems", ["A nerd's best friends", "Candies"]),
Quiz("What is the shell?", "The outermost layer of an operating system", ["A snail's little home", "The best way to your computer's heart"]),
Quiz("Which of the following is a graphical shell?", "GUI", ["CLI", "Chewey"]),
Quiz("Why should you learn to use CLI, Bash Shell?", "To become a more powerful programmer", ["To save Princess Peach", "To beat MrBison"]),
Quiz("What is Git Bash?", "A Unix style shell compatible with Linux servers", ["A wrestling game", "A bottle recycling app"]),
Quiz("How many terminals can be opened at once?", "Any number", ["Only one", "Maximum two"]),
Quiz("What is the output of the command echo Hello World?", "Hello World", ["Bye bye", "World"]),
Quiz("What is the output of the command echo 'Hello!!' ?", "Hello!!", ["Two many exclamations marks", "You okay?"]),
Quiz("What would be the equivalent of the echo command in Python?", "print", ["import", "for"]),
Quiz("x=100. How do you refer to the variable x?", "echo $x", ["echo x", "'x'"])]

# Correct Answers counter
correctCount = 0

# Shuffle the list of Quiz objects
random.shuffle(quizList)

# Loop to iterate over each item of the list
for quizItem in quizList:
  print(quizItem.question)
  possible = quizItem.otherAnswers + [quizItem.correctAnswer]
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnswer = input()
  while not userAnswer.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnswer = input()
  userAnswer = int(userAnswer)
  while not (userAnswer > 0 and userAnswer <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnswer = input()
  if possible[userAnswer-1] == quizItem.correctAnswer:
    print("Well done! Your answer was correct.")
    correctCount += 1
  else:
    print("I'm so sorry. Your answer was wrong.")
    print("The correct answer was: " + quizItem.correctAnswer)
  print("")

print("You answered " + str(correctCount) + " of " + str(len(quizList)) + " questions correctly.")
if correctCount > 8:
    print("Congratulations")
else:
    print("Watch the video lessons again and come back test your knowledge!")
