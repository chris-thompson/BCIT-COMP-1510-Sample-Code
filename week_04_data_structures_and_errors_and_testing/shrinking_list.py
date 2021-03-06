"""
We can loop through lists and remove things.
"""


def remove_neg(num_list):
    """Remove the negative numbers from the list num_list.

    >>> numbers = [-5, 1, -3, 2]
    >>> remove_neg(numbers)
    >>> numbers
    [1, 2]
    """
    for item in num_list:
        if item < 0:
            num_list.remove(item)
