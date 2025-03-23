T = int(input())

for _ in range(T):
    # arr = input().split()
    # split은 해주는데 공백을 기준으로 나눠줌. 공백이 없으니 한 덩어리로 취급
    arr = input()
    print(f"{arr[0]}{arr[-1]}")