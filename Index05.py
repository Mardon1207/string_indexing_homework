def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        s.isdigit(): answer
    """
    a=0
    if s[0].isdigit():
        a=a+1
    if s[1].isdigit():
        a=a+1
    if s[2].isdigit():
        a=a+1
    if s[3].isdigit():
        a=a+1
    if s[4].isdigit():
        a=a+1
    return a
s=str(input())
print(main(s))