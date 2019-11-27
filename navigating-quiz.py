# This questionnaire was created by Sabrina Palis
# during the Bertelsmann Scholarship Challenge 2019
# It focuses on the commands to navigate directories.

import random

# The Quiz class consists of a question, a correct answer and
# the wrong answers. 
class Quiz:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.correctAnswer = correctAnswer
        self.otherAnswers = otherAnswers

# List of Quiz objects.
quizList = [Quiz("How do you navigate directories in Git Bash?", "With commands", ["With the mouse", "With a trackball"]),
Quiz("How do you see the content of the current directory?", "ls", ["show", "tell"]),
Quiz("How do you move to another directory", "cd", ["chg", "cj"]),
Quiz("How do you go up one directory?", "cd ..", ["up ..", "top .."]),
Quiz("How do you list the content of the parent directory?", "ls ..", ["lc ..", "parent ls"]),
Quiz("What does pwd stand for?", "Print Working Directory", ["Password", "Plot When Done"]),
Quiz("What happens if you run ls ~ ?", "It lists the home directory", ["It opens language settings", "It switches the font to Comic Sans"]),
Quiz("What is the home directory?", "It is the current user's top-level directory", ["It's another name for your contacts", "It doesn't exist"]),
Quiz("What is a relative path?", "The path relative to your current location", ["The family tree", "The path to the files modified last"]),
Quiz("What is an absolute path?", "When you provide the full path all the way from the home directory", ["When you guess a path", "When you create a path"]),
Quiz("What happens when you run cd ~ ?", "It takes you to your hone directory", ["It deletes punctuation", "'It loads music"])]

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
