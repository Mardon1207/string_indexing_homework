def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s)<n:
        a=False
    else:
        a=s[n-1]
    return a
s=str(input())
n=int(input())
print(main(s,n))
