def find_max_sum_subarray(arr, k):
    if arr is None or len(arr) < k:
        raise ValueError("Array is null or smaller than k")

    # Calculate the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Example usage
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(find_max_sum_subarray(arr, k))  # Output: 9 (5+1+3)
