# 데코레이터 @

class MyDecorator:
    def __init__(self, f):
        print("initializing MyDecorator...")
        self.func = f  # 입력으로 받은 f를 저장. 함수의 이름을 전달 받을것. 여기서는 print_hello

    def __call__(self):  # 참조 변수를 함수 호출 하듯이 호출 하면 얘가 호출됨.
        print("Begin:{}".format(self.func.__name__))

        self.func()  # 위에서 전달 받은 함수 이름 호출. __call__() 매서드가 호출되면 생성자에서 저장해둔 함수(데이터 속성. func)를 호출.

        print("End:{}".format(self.func.__name__))


@MyDecorator
def print_hello():
    print("Hello.")


if __name__ == "__main__":
    print_hello()  # print_hello 가 데코레이터 처리 되어있다. 함수 호출 처럼 되어있지만 전후의 모든 기능들도 같이 수행된다.
