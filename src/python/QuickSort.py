# coding:utf-8

def quick_sort(l, start, end):
    i = start
    j = end

    if i > j :
        return

    key = l[i]
    while i < j :
        while i < j and key <= l[j]:
            print key, l[j], "*" * 30
            j -= 1
        l[i] = l[j]

        while i<j and key >= l[i]:
            print key, l[j], "*" * 30
            i += 1
        l[j] = l[i]
    l[i] = key

    quick_sort(l, start, i-1)
    quick_sort(l, i+1, end)

if __name__ == "__main__":
    l = [5, 1, 8, 4, 9]
    quick_sort(l, 0, len(l)-1)
    print l
