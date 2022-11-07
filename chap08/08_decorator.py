# 데코레이터(Decorator) 함수를 꾸미는 객체.


class Callable:
    def __init__(self):
        pass

    def __call__(self):
        print("I'm called.")


if __name__ == "__main__":
    obj = Callable()  # 참조 변수 선언 하면서 그 주소 값을 obj로 지정.

    obj()  # 객체를 함수 호출 하듯이 호출.
    # 인스턴스 뒤에 괄호를 붙여 호출하면
    # 내부적으로는 __call__(self) 메서드가 호출된다.
