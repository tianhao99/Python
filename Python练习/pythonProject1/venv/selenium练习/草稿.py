


days = eval(input())
datas = eval(input())
num = []
for i in range(days):
    if i == 0:
        su = 1
        num.append([i,1,su])

    elif i ==1:
        su = 4
        num.append([i,3,su])
    else:
        su += num[i-1][1]*2
        num.append([i,2*num[i-1][1],su])

if num[days-1][2] <= datas:
    print(num[days-1][1]+datas-num[days-1][2])
else:
    for i in range(days):

        if num[i][2]>=datas:
            print(num[i][1])
            break




# for j in num:
#     print(j)