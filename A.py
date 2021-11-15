# 標準入力を受け付ける。
A, B, C = map(int, input().split())

# 3枚のカードの中から2枚のカードを選ぶ場合を、全て洗い出す。
pattern1 = A + B
pattern2 = A + C
pattern3 = B + C

# max関数を利用して、2枚のカードを選ぶ場合の最大値を求める。
print(max(pattern1, pattern2, pattern3))
