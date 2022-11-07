def my_power(y):
    print("숫자를 입력하세요.")
    x = int(input())  # 들어올때는 String 이라서 강제 형변환위해 int로 감싸주기
    return x ** y


if __name__ == '__main__':

    print(my_power(2))