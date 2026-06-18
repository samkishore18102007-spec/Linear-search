arr = [10, 20, 30, 40, 50, 60, 70]
x = 50

l = 0
h = len(arr) - 1

while l <= h:
    m = (l + h) // 2

    if arr[m] == x:
        print("Found at index", m)
        break
    elif arr[m] < x:
        l = m + 1
    else:
        h = m - 1
else:
    print("Not Found")