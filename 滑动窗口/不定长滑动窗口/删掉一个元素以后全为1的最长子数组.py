## nums中只有0和1元素，删除一个元素后，剩下的元素中1的个数最多是多少
# ## 题目要求删除一个元素，剩下的元素中1的个数最多是多少
def longestSubarray(nums: list[int]) -> int:
    max_len = 0
    last_zero_index = None
    ans = []
    if len(nums) == 1: return 0
    for i, num in enumerate(nums):
        ## 遇到0且之前没有遇到过0
        if num == 0 and not last_zero_index:
            ## 记录零元素的位置，方便下一次遇到0的时候为ans赋值
            last_zero_index = i
            ## 跳过，相当于删除了0，后续开始记录1元素的个数
            continue
        ## 遇到0且之前遇到过0
        if num == 0 and last_zero_index:
            ## ans直接赋值为上一个0和当前0之间的序列
            ans = nums[last_zero_index+1:i]
            last_zero_index = i
            ## 跳过，相当于删除了当前0，后续开始记录元素1的个数
            continue
        
        ans.append(num)
        max_len = max(max_len, len(ans))
    ## 如果元素中没有0元素，则max_len = len(nums)，按照题目要求，需要减1返回
    return max_len if last_zero_index is not None else max_len - 1

nums = [0,1,1,1,1,1]
print(longestSubarray(nums))