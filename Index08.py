def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.find("*")==-1:
        a=False
    else:
        a=s.find("*")
    return a
s=str(input())
print(main(s))
        