def main(n):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if n==1:
        return 'Monday'
    if n==2:
        return 'Tuesday'
    if n==3:
        return 'Wednesday'
    if n==4:
        return 'Thursday'
    if n==5:
        return 'Friday'
    if n==6:
        return 'Saturday'
    if n==7:
        return 'Sunday'
print(main(3))
