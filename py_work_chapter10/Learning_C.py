# Assignment 10-2; Learning C
# Replace Python with the letter C

# We are importing here as it is so much easier than 
# using the with open() method
from pathlib import Path

fileObject = Path('learning_python.txt')
text = fileObject.read_text().rstrip()
# print(text) # First print

for line in text.splitlines():
    line = line.replace('Python', 'JavaScript')
    print(line)