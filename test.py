while True:
    char = input("문자를 입력하세요. 종료하려면 '.'을 입력하세요.: ")
    if char == '.':
        print("프로그램 종료.")
        break
    print(ord(char))