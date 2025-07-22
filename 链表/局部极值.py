from typing import Optional, List
from base import ListNode, array_to_list

def nodesBetweenCriticalPoints(head: Optional[ListNode]) -> List[int]:
        index = 0
        lst_val = head.val
        head = head.next
        res = []
        min_pre = float('inf')  ## 和上一个极值的距离最小值
        while head:
            cur_val = head.val
            if head.next:
                nxt_val = head.next.val
            else:
                break
            index += 1
            if (nxt_val and nxt_val > cur_val and cur_val < lst_val) or (nxt_val and nxt_val < cur_val and cur_val > lst_val):
                if res:
                    pre = index - res[-1]  ## 和上一个极值的距离
                    if pre < min_pre:
                        min_pre = pre
                res.append(index)
            lst_val = cur_val
            head = head.next
        if index <= 1 or not res or len(res) == 1:
            return [-1, -1]
        max_val = res[-1] - res[0]
        return [min_pre, max_val]

head = [5,3,1,2,5,1,2]

print(nodesBetweenCriticalPoints(array_to_list(head)))