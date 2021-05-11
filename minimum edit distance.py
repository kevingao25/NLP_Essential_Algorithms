# Levenshtein Distance Algorithm for minimum editing distance
import numpy as np


def min_edit_distance(source, target):
    n = len(source)
    m = len(target)

    # Create a distance matrix distance[n+1, m+1]
    D = np.zeros((n+1, m+1))

    # Initialization: the zeroth row and column is the distance from the empty string
    D[0][0] = 0
    for i in range(n+1):
        D[i][0] = i
    for j in range(m+1):
        D[0][j] = j

    # Recurrence relation
    for i in range(1, n+1):
        for j in range(1, m+1):
            # Case when no substitution is needed
            if source[i-1] == target[j-1]:
                D[i][j] = min(D[i - 1][j] + 1,
                              D[i][j - 1] + 1,
                              D[i - 1][j - 1] + 0)
            # Case when substitution is needed
            else:
                D[i][j] = min(D[i-1][j] + 1,
                              D[i][j-1] + 1,
                              D[i-1][j-1] + 2)

    # Termination
    return int(D[n][m])


print("The minimum edit distance is:", min_edit_distance("kevin", "ke"))



