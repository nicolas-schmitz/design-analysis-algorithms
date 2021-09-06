def insertion_sort(vector: list):
    """Sort the vector utilizign insertion sort. Loops through the vector and finishes each iteration sorting the vector to position j.
    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        vector (list): list with values

    Returns:
        list: list with sorted values
    """
    for j in range(1, len(vector)):
        key = vector[j]
        i = j - 1

        while i >= 0 and vector[i] > key:
            vector[i + 1] = vector[i]
            i -= 1
        vector[i + 1] = key

    return vector
