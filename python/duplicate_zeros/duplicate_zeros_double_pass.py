#Input:    [1,5,2,0,6,8,0,6,0]
#Expected: [1,5,2,0,0,6,8,0,0]
ra = [1,0,2,3,0,4,5,0]#{[1,0,2,2,3,4,5,4][1,0,2,2,3,4,5,4]


def count_indices(arr_in):
    array_info = {"last_index": 0,
                  "over_bounds": False}
    length = len(arr_in)
    count = 0  # counting how many digits will be in final array based on where we are in input array
    index_found = -1  # index of number we are looking at in original array
    for k in arr_in:
        if k == 0:
            count += 2
            index_found += 1
        else:
            count += 1
            index_found += 1
        if count >= length:
            array_info["last_index"] = index_found
            if count > length:
                array_info["over_bounds"] = True
            break
    return array_info


print(count_indices(ra))


def back_expand(arr, array_info):
    print("array in:")
    print(arr)
    last_index = array_info["last_index"]
    over_bounds = array_info["over_bounds"]
    do_last = True

    count = -1

    for d in reversed(range(last_index + 1)):
        if arr[d] == 0:
            if do_last and over_bounds:
                do_last = False
                arr[count:count+1 or None] = [arr[d]]
                count -= 1
                continue
            print(f"moving {arr[d]} from index {d} to {count-1} and {count}")
            arr[count-1:count+1 or None] = [arr[d], arr[d]]
            print(arr)
            count -= 2
        else:
            print(f"moving {arr[d]} from index {d} to {count}")
            arr[count:count+1 or None] = [arr[d]]
            print(arr)
            count -= 1

#
back_expand(ra, count_indices(ra))
#print(ra)
