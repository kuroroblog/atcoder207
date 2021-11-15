# 標準入力を受け付ける。
A, B, C, D = map(int, input().split())

# 操作の回数を格納する。
ans = 0

# 以前の計算結果を代入する。
# 初期値が-100000000000000000000なのは、previous_valへ代入される値が、徐々にプラスの方向へ変化するため。
previous_val = -100000000000000000000

while True:
    # (A + (B * ans)) / (C * ans) <= D ⏩ 0 <= D * (C * ans) - ((A + (B * ans))) ⏩ 0 <= (D * C * ans) - A - (B * ans)
    val = (D * C * ans) - A - (B * ans)
    if 0 <= val:
        print(ans)
        exit()
    ans += 1

    # 以前の計算結果よりも0に近づいていないと、永遠にD倍以下になることはないので、以下の条件式が成り立つ。
    if previous_val >= val:
        print(-1)
        exit()

    previous_val = val
