def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    mx=0
    while n!=0:
        b=n%10
        if b>mx:
           mx=b
        n=n//10
    return mx
print(main(98764))  
