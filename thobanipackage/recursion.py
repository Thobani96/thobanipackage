def sum_array(array):

    '''Return sum of all items in array'''

    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:])



def fibonacci(n):

    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    """

    if n <= 1:
        return n
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def factorial(n):

    '''Returns the product of all positive integers less than or equal to n.'''

    if n < 0:
        raise ValueError(" n must be a positive integer")

    elif n == 0:
        return 1

    elif n == 1:
        return n

    else:
        return  n * factorial(n-1)



def reverse(word):

    '''Return word in reverse'''
    if len(word) > 1:
        return word[-1] + reverse(word[:-1])
    else:
        return word
