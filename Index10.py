def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    a=int(s)//10000+int(s)//1000%10+int(s)//100%10+int(s)//10%10+int(s)%10
    return a
s=str(input())
print(main(s))