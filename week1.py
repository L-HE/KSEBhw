# Baekjoon 1000 A+B

def add(a, b) -> int:
  sum = a + b
  return sum

a, b = map(int, input().split())

if 0 < a < 10 and 0 < b < 10:
    print(add(a, b))
else:
    print("Out of range.")