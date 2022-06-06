# Check whether the item is present in list or not 

def recursive_binary_search(list, target):

    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint + 1:], target)
        else:
            return recursive_binary_search(list[:midpoint], target)


list = [1, 2, 4, 6, 7, 8, 10, 14]
target = 4

print(recursive_binary_search(list, target))
