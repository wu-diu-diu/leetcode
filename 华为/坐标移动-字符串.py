# 哈希表
position = [0, 0]
move_dict_x = {'A': -1, 'D': 1}
move_dict_y = {'W': 1, 'S': -1}
while True:
    try:
        x = input().split(';')[:-1]
        for move in x:
            if len(move) > 3 or len(move) < 2:
                continue
            if move[0] not in move_dict_x and move[0] not in move_dict_y:
                continue
            direc = move[0]
            try:
                num = int(move[1:])
            except:
                continue
            if direc in move_dict_x:
                position[0] += move_dict_x[direc] * num
            else:
                position[1] += move_dict_y[direc] * num
        print(f"{position[0]},{position[1]}")
    except:
        break

## 法二
# input_list = input().split(';')
# initial = [0,0]
 
# for item in input_list:
#     if not 2 <= len(item) <= 3:
#         continue
 
#     try:
#         direction = item[0]
#         step = int(item[1:])
#         if direction in ['A', 'D', 'W', 'S']:
#             if 0 <= step <= 99:
#                 if direction == 'A':
#                     initial[0] -= step
#                 elif direction == 'D':
#                     initial[0] += step
#                 elif direction == 'S':
#                     initial[1] -= step
#                 elif direction == 'W':
#                     initial[1] += step
#     except:
#         continue
 
# print(str(initial[0]) + ',' + str(initial[1]))
