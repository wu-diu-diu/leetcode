def numOfSubarrays(arr: list[int], k: int, threshold: int) -> int:
        sub_sum = 0
        cnt = 0
        if len(arr) == 1: return int(arr[0] >= threshold)
        for i, num  in enumerate(arr):
            sub_sum += num

            if i < k - 1:
                continue
            
            # average = sub_sum / k
            if sub_sum >= k * threshold:  # 这里直接判断和是否大于等于k*threshold，避免了浮点数的精度问题
                cnt += 1
            
            sub_sum -= arr[i + 1 - k]

        return cnt