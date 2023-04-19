def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.isdigit():
        a=int(s)
    else:
        a=-1
    return a
s=str(input())
print(main(s))