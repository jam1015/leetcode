ra = [0, 1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10]

def dup_element(ind_in, arr_in):
    print(f"array in: {arr_in}")
    lenth = len(arr_in)
    for k in reversed(range(ind_in, lenth - 1 )):
        arr_in[k + 1] = arr_in[k]
        print(k)
    print(f"            array out: {arr_in}")


for k in reversed(range(len(ra))):
    if ra[k] == 0:
        dup_element(k, ra)
