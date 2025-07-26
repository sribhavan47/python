def min_days_for_happy_neighborhood(N, filling, K):
    filled = [0] * (N + 2)

    for day in range(len(filling)):
        filled[filling[day]] = 1
        count = 0
        for i in range(1, N + 1):
            if filled[i]:
                count += 1
                if count >= K:
                    return day + 1
            else:
                count = 0

    return -1

N = 5
filling = [3, 1, 2, 4, 2]
K = 6

print(min_days_for_happy_neighborhood(N, filling, K))
