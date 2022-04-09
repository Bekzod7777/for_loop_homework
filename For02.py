def main(n):
    rr=''
    for x in range(n-1):
        rr +=str(x)
        rr +=','
    
    rr +=str(n-1)
    #rr +='"'
    return rr
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """

