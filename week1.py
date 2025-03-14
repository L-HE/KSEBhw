# Baekjoon 10430 나머지

A, B, C = map(int, input().split())

ans1 = (A + B) % C
ans2 = ((A % C) + (B % C)) % C
ans3 = (A * B) % C
ans4 = ((A % C) * (B % C)) % C

print(f"{ans1}\n{ans2}\n{ans3}\n{ans4}\n")