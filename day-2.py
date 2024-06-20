# When I wrote this code only God and I know what it means, now only God knows.
list = [1, 4, 9, 16, 25]

a = [7, 11, 37, 97, 203, 367, 601, 917, 1327, 1843]
b = [-8, -9, -12, -29, -96, -273, -644, -1317, -2424, -4121]
c = [1, 2, 9, 22, 41, 66, 97, 134, 177, 226]
d = [6, 7, 38, 129, 310, 611, 1062, 1693, 2534, 3615]
e = [-1, 0, -3, -10, -21, -36, -55, -78, -105, -136]

def difference(list):
    cache = []
    for i in range(0, len(list) - 1):
        cache.append(list[int(i) + 1] - list[i])
    return cache


def check_diff(list):
    for i in range(0, len(list) - 1):
        if list[int(i) + 1] != list[i]:
            return False
    return True


def polynomial(input):
    check_list = input.copy()
    diff_not_found = False
    diff_list = []
    diff_count = 0
    while not diff_not_found:
        diff_list.append(difference(check_list))
        diff_not_found = check_diff(diff_list[diff_count])
        check_list = diff_list[diff_count].copy()
        diff_count += 1
    return diff_list


def next_element(list):
    diff = polynomial(list)
    cache = 0
    for i in range(len(diff) - 1, -1, -1):
        cache += diff[i][-1]
    return list[-1] + cache

output = next_element(list)
print(output)

print(polynomial(a))
print(polynomial(b))
print(polynomial(c))
print(polynomial(d))
print(polynomial(e))

print(next_element(a))
print(next_element(b))
print(next_element(c))
print(next_element(d))
print(next_element(e))

