import math

# 標準入力を受け付ける。
N = int(input())

# N == 1の時、平行移動するだけでTの点と一致させられるので、必ず`Yes`となる。
if N == 1:
    print('Yes')
    exit()

S = []
for _ in range(N):
    a, b = map(int, input().split())
    S.append((a, b))

T = []
for _ in range(N):
    c, d = map(int, input().split())
    T.append((c, d))

# 重心を演算する関数
def get_center_point(arr):
    x = 0
    y = 0
    for i in range(N):
        x += arr[i][0]
        y += arr[i][1]

    return (x / N, y / N)

# S集合の重心を求める。
(sx1, sy1) = get_center_point(S)
# T集合の重心を求める。
(tx1, ty1) = get_center_point(T)

# 各座標を重心からの相対座標に変換(平行移動)する。
for i in range(N):
    S[i] = (S[i][0] - sx1, S[i][1] - sy1)
    T[i] = (T[i][0] - tx1, T[i][1] - ty1)

# 回転角の計算に使うS[z]が重心と一致してしまう場合(S[z][0] == 0, S[z][1] == 0)の場合の回避処理
# math.atan2(S[z][1], S[z][0])が0になると計算が合わない。
z = 0
for i in range(N):
    if S[i][0] == 0 and S[i][1] == 0:
        continue
    z = i
    break

# 1*10^-6
DICT_MIN = 1e-6

# 回転角を計算し、あるSの点を回転させる。総当たりであるTの点に一致するか確認する。
for i in range(N):
    # 回転角を求める。
    # 参考 : https://note.nkmk.me/python-math-sin-cos-tan/
    # 参考 : https://atarimae.biz/archives/18041
    angle = math.atan2(T[i][1], T[i][0]) - math.atan2(S[z][1], S[z][0])

    count = 0
    for j in range(N):
        # 先ほど求めた回転角を元に、あるSの座標を回転させる。
        # 参考 : http://www.geisya.or.jp/~mwm48961/kou2/linear_image3.html
        x2 = S[j][0] * math.cos(angle) - S[j][1] * math.sin(angle)
        y2 = S[j][0] * math.sin(angle) + S[j][1] * math.cos(angle)

        # あるSの座標とあるTの座標が一致しているのか、確認する。
        is_match = False
        for k in range(N):
            # 点の一致具合を調べる。
            dx = abs(T[k][0] - x2)
            dy = abs(T[k][1] - y2)
            if dx <= DICT_MIN and dy <= DICT_MIN:
                # あるSの回転後の点が、あるTの点に一致
                is_match = True
                break

        if is_match == False:
            break
        else:
            count += 1

    if count == N:
        print("Yes")
        exit()

print("No")
