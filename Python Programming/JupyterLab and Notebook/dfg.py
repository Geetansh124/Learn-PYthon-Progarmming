def recursive_min(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < recursive_min(L[1:]) else recursive_min(L[1:])