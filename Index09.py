def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
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