
# Defining a function and giving it the parameter of "name"
# "name" is a temporary variable that only exists within the scope of this function
def printName(name):
  print("Oh! Hello " + name)

# Now any string value can be passed into the function within the parentheses
printName("Mark")
printName("Rose")
printName("Denny")

# Functions can be given multiple parameters
# Parameters can also be provided with default values
def recordScore(name, score=1):
  # The score that is printed out will default to 0 if none is provided
  # First value
  try:
    print(name + "'s score is " + score)
  except Exception as e:
    print("You didn't provide a string")

recordScore("Jacob")
recordScore("Ahmed", "20")
recordScore("Steven", "15")

