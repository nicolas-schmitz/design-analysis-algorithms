def insertion_sort(vector):
    for j in range(1, len(vector)):
        key = vector[j]
        i = j - 1

        while i >= 0 and vector[i] > key:
            vector[i + 1] = vector[i]
            i -= 1
        vector[i + 1] = key

    return vector
