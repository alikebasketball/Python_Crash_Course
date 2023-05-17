# Assignment 10-3; Simpler Code
# Skip the temporary variable


# We are importing here as it is so much easier than 
# using the with open() method
from pathlib import Path

fileObject = Path('learning_python.txt')
text = fileObject.read_text().rstrip()
# print(text) # First print


for line in text.splitlines():
    print(line)