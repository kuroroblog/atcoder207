# 標準入力を受け付ける。
N = int(input())

sample_list = []
for _ in range(N):
    t, l, r = map(int, input().split())
    sample_list.append((t, l, r))

cnt = 0
# <計算量>
# A2 = 1, An+1 = An + Nの漸化式である。
# A2000 = A1999 + 1999 = 1997001 + 1999 = 1999000回ループなので問題ない。
for i in range(N):
    for j in range(i + 1, N):
        i_val = sample_list[i]
        i_left, i_right = i_val[1:]

        j_val = sample_list[j]
        j_left, j_right = j_val[1:]

        # 区間の条件に入らない場合に、continueを行う。
        if (j_right < i_left or i_right < j_left):
            continue

        # 区間の条件に入らない場合に、continueを行う。
        if (i_right < j_left or j_right < i_left):
            continue

        # 区間の条件に入らない場合に、continueを行う。
        if i_val[0] == 2 and i_right == j_left:
            continue

        # 区間の条件に入らない場合に、continueを行う。
        if j_val[0] == 2 and j_right == i_left:
            continue

        # 区間の条件に入らない場合に、continueを行う。
        if i_val[0] == 3 and j_right == i_left:
            continue

        # 区間の条件に入らない場合に、continueを行う。
        if j_val[0] == 3 and i_right == j_left:
            continue

        # 区間の条件に入らない場合に、continueを行う。
        if i_val[0] == 4 and (j_right == i_left or i_right == j_left):
            continue

        # 区間の条件に入らない場合に、continueを行う。
        if j_val[0] == 4 and (i_right == j_left or j_right == i_left):
            continue

        cnt += 1

print(cnt)
