def est_premier(N):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

est_premier(50) # False
est_premier(17) # True
est_premier(1000000000000000) # False
est_premier(9576890767) # True
est_premier(95647806479275528135733781266203904794419563064407) # True
