def min_num_in_list(a):
    min=a[0]
    for temp in a:
        if min > temp:
            min=temp
    return min


print(min_num_in_list([1, -20, -8, 0]))
