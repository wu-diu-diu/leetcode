from typing import Optional
from base import ListNode, array_to_list

test_list = [1,0,1]
          

def getDecimalValue(head: Optional[ListNode]) -> int:
        res = ''
        while(head):
            val = str(head.val)
            res += val
            head = head.next
        length = len(res)
        final_res = 0
        for i in range(length):
            val =  int(res[i]) * 2 ** (length - 1 - i)
            final_res += val
        return final_res

def getDecimalValue_linshen(head: Optional[ListNode]) -> int:
        ans = 0
        while(head):
            ans = ans * 2 + head.val
            head = head.next
        return ans

print(getDecimalValue_linshen(array_to_list(test_list)))