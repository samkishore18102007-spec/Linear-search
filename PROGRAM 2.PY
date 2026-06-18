numbers = [10, 20, 30, 40, 50, 60, 70]
search = int(input("Enter the number to search: "))
low = 0
high = len(numbers) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == search:
        print("Element found at position", mid + 1)
        found = True
        break
    elif numbers[mid] < search:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Element not found")