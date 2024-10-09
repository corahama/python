# You recieve as input a collection of numeric elements. You have a bag, in which you can add a
# a maximum of 2 different elements of each type. You have to find the maximum amount of 
# elements that you can add to the bag with that restriction.

def count_items(arr):
    max_itms = 0

    for i in range(len(arr)):
        temp_max = 0
        temp_list = []
        for j in range(i, len(arr)):
            if arr[j] in temp_list:
                temp_max += 1
            elif arr[j] not in temp_list and len(temp_list) < 2:
                temp_list.append(arr[j])
                temp_max += 1
            else:
                if temp_max > max_itms: max_itms = temp_max
                break

    return max_itms


def count_items_op(arr):
    head, tail = 0,0
    max_items = 0

    i_count = {}
    while head < len(arr):
        if len(list(filter(lambda v: v > 0, i_count.values()))) > 2:
            i_count[arr[tail]] -= 1
            tail += 1
        else:
            if arr[head] not in i_count:
                i_count[arr[head]] = 1
            else:
                i_count[arr[head]] += 1
            head += 1

        temp_itms = list(filter(lambda v: v > 0, i_count.values()))
        if len(temp_itms) <=  2:
            if sum(temp_itms) > max_items:
                max_items = sum(temp_itms)

    return max_items


arr =  [1,2,3,3,3,1,1,2,1,1,3,3] # output = 5
# arr =  [1,2,3,4,5,6] # output = 2

print(count_items_op(arr))
