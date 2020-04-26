N, Q = list(map(int, input().split()))
binary_list = list(map(int, input().split()))
if N == len(binary_list):
    for i in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            flip_position = query[1] - 1
            if binary_list[flip_position] == 0:
                binary_list[flip_position] = 1
            else:
                binary_list[flip_position] = 0
        else:
            start_index = query[1] - 1
            end_index = query[2]
            calculate_binary_value = binary_list[start_index:end_index]
            print("ODD" if calculate_binary_value[-1] == 1 else "EVEN")



# N , Q = list(map(int , input().split()))
# n = list(map(int , input().split()))
# cal = 0
# sum1 = 0
# for i in range(Q):
#     inp = list(map(int , input().split()))
#     if(inp[0]==1):
#         if(n[inp[1]-1]==0):
#             n[inp[1]-1] = n[inp[1]-1]+1
#         else:
#             n[inp[1]-1] = n[inp[1]-1]-1
#     else:
#         if(n[inp[2]-1]==1):  # looks it is not correct though accepted.
#             print("ODD")
#         else:
#             print("EVEN")