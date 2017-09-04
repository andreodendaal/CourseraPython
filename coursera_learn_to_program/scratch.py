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