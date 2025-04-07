def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

## 二分查找
## 利用二分查找找到target应该插入的位置
def binary_search_insert(arr, target):
    left, right = 0, len(arr) - 1
    ## 最终当left == right时，mid= left 如果arr[mid] < target，则left+1一定是第一个大于targetd的，因为[left,right]右边的数一定是大于target的，则应该插入这个位置
    ## 如果arr[mid] > target，则right-1一定是第一个小于target的，因为[left,right]左边的数一定是小于target的，
    ## 但是要求返回的是第一个大于target的位置，所以如果找不到，则返回left索引
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:  ## 如果找到了target，则直接返回
            arr.insert(mid, target)
            return arr
    ## 如果没有找到target，则返回left
    arr.insert(left, target)
    return arr
## 二分查找寻找目标元素的插入位置，如果有多个目标元素，则插入到最左边
def binary_search_repeat(arr, target):
    i, j = 0, len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] < target:
            i = mid + 1
        elif arr[mid] > target:
            j = mid - 1
        else:  ## 找到了目标元素，j向左移动，直到找到目标元素，且找到的目标元素是最左边的，则是要插入的位置
            ## 同理，要插入到最右边，则i向右移动
            j = mid - 1
    arr.insert(i, target)
    return arr


arr = [1,3,6,8,12,15,23,26,31,35]
target = 25
print(binary_search_insert(arr, target))
arr = [1,3,6,6,6,6,6,10,12,15]
target = 6
print(binary_search_repeat(arr, target))