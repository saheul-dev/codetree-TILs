for _ in range(4):
    arr = list(map(int, input().split()))
    arr_sum = 0
    for item in arr:
        arr_sum += item
    print(arr_sum)