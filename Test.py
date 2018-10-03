# Complete the isPalindrome function below. DocTest
def isPalindrome(x):
    # Write your doctests below.
    """
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
    Traceback (most recent call last):
    ...
    ValueError: x must be a positive integer
    >>> isPalindrome("Hello")
    Traceback (most recent call last):
    ...
    ValueError: x must be an integer
    """
    temp=x
    rev=0
    while(x>0):
        dig=x%10
        rev=rev*10+dig
        x=x//10
    if(temp==rev):
        return True
    else:
        return False
       
