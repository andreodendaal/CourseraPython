<<<<<<< HEAD
import numpy as np
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:7]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
=======
def is_palindrome_v3(s):
    """ (str) -> bool
    Return True if and only if s is a palindrome.
    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('a')
    False
    """
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i]:
            return False

    return True
>>>>>>> 593d2a6d6ac89389946ede5903923d1d8097a257
