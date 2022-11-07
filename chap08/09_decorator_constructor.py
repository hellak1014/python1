# 데코레이터 사용 용도 (생성자)

class MyDecorator:
    def __init__(self, f):
        print("initializing MyDecorator...")
        self.func = f  # 입력으로 받은 f를 저장. 함수의 이름을 전달 받을것. 여기서는 print_hello

    def __call__(self):  # 참조 변수를 함수 호출 하듯이 호출 하면 얘가 호출됨.
        print("Begin:{}".format(self.func.__name__))

        self.func()  # 위에서 전달 받은 함수 이름 호출. __call__() 매서드가 호출되면 생성자에서 저장해둔 함수(데이터 속성. func)를 호출.

        print("End:{}".format(self.func.__name__))


def print_hello():
    print("Hello.")


if __name__ == "__main__":
    hello = MyDecorator(print_hello)
    #  MyDecorator의 인스턴스가 만들어지며
    #  __init__() 생성자 메서드가 호출.
    #  print_hello 식별자는 앞에서 정의한 함수가 아닌 MyDecorator의 객체.

    hello()  # 인스턴스 혹은 객체를 함수 호출 모양으로 호출. __call__(self)가 MyDecorator 객체를 호출하 듯 사용할 수 있음.
