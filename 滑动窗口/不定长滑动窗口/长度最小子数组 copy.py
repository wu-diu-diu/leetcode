from collections import defaultdict, Counter
def test(s):
    cnt = 0
    dic = defaultdict(int)
    length = len(s) / 4
    for right, char in enumerate(s):
        dic[char] += 1
        if dic.values():
            cnt += 1
    return cnt



        

string = 'QQWEEEWW'
print(test(string))
        