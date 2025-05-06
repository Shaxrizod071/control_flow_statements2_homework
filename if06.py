def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    mx=0
    for i in range(len(n)):
        if n[-1]>str(i) or not i:
            mx=n[-1]
        return mx
print(main(12345))
