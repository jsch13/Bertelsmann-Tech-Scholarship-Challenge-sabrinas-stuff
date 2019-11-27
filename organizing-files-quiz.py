# This questionnaire was created by Sabrina Palis
# during the Bertelsmann Scholarship Challenge 2019
# It focuses on the commands to organize your files.

import random

# The Quiz class consists of a question, a correct answer and
# the wrong answers. 
class Quiz:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.correctAnswer = correctAnswer
        self.otherAnswers = otherAnswers

# List of Quiz objects.
quizList = [Quiz("What does mkdir stand for ?", "make directory", ["milk director", "mike drop"]),
Quiz("What does mv stand for?", "move", ["melt", "marvel"]),
Quiz("How do you move all the epub files", "mv Documents/*.epub", ["mv Documents/.epub", "mv Documents/*."]),
Quiz("How do you create a Photos directory?", "mkdir Photos", ["create Photos", "folder Photos"]),
Quiz("How do you move all the jpg files to the Photos directory?", "mv *.jpg Photos", ["mv .jpg Photos", "mv *.jpg"]),
Quiz("Run mkdir Animations. What happens?", "It creates the Animations directory", ["It stores all the gif automatically", "It gives you the location of your animations"]),
Quiz("Run mv *2014*.jpg Vacations. What happens?", "It moves all the jpg files with 2014 in their name to the Vacations folder", ["It deletes the files from 2014", "It creates a 2014 directory"]),
Quiz("What is the use of the -l option tool?", "It prints a more detailed listing", ["It shows only the file starting with l", "It shows the length of the files"]),
Quiz("What does the pattern bear* do ?", "It matches any file whose name starts with the word bear", ["It finds all the animal files", "It finds the files that ends with Teddy."]),
Quiz("Run ls *poem* What happens?", "It lists the files with the name poem in it", ["It provides you with rhymes", "It prompts you to write"])]

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
