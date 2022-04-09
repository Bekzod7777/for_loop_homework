def main(N):
    s=0
    for x in range(1,N+1):
        s +=1/x
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    return  s
