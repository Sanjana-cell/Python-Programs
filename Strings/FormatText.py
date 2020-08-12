import textwrap

value = """Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function"""

# Wrap this text.
wrapper = textwrap.TextWrapper(width=50)

string = wrapper.fill(text=value)

print(string)