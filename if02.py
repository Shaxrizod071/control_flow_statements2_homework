def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b:
         return a
    if b>c:
         return b
    else:
         return c
print(main(2,3,4))
