class Base:  # 이름만 있는 참조 자료형
    def __init__(self):  # 부모클래스. 상위 클래스.
        print(self)
        self.message = "hello world!"

    def print_message(self):
        print(self.message)


class Derived(Base):  # 상속의 모형. (괄호 안에)
    pass  # 자식클래스.하위클래스.


if __name__ == '__main__':
    base = Base()
    base.print_message()

    derived = Derived()
    derived.print_message()

# 자바는 주소값을 알 수 없었으나 파이썬은 주소값을 알 수 있다.
