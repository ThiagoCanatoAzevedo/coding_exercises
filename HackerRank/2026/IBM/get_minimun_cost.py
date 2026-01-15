def getMinimumCost(arr):
    n = len(arr)

    # última ocorrência de cada valor
    last = {}
    i = 0
    while i < n:
        last[arr[i]] = i
        i += 1

    cost = 0
    seen = {}
    R = -1
    active = False

    i = 0
    while i < n:
        x = arr[i]

        # se esse valor aparece novamente no futuro,
        # ele força um segmento
        if last[x] > i:
            if not active:
                active = True
                seen = {}
                R = last[x]
            else:
                if last[x] > R:
                    R = last[x]

        if active:
            seen[x] = 1

            # fim do segmento
            if i == R:
                cost += len(seen)
                active = False

        i += 1

    return cost

print(getMinimumCost([3, 1, 3, 2, 7, 2, 5, 2]))