def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    inx=0
    if n[0]>n[1] or n[2] or n[3] or n[4] or n[5]:
         return n[0]
    if n[1]>n[0]or n[2] or n[3] or n[4] or n[5]:
        return n[1]
print(main('advgd'))
