# 데이터 속성(field) 상속

"""

class A:  # 참조 자료형
    def __init__(self):  # 생성자
        print("A.__init()__")
        self.message = "hello"  # message의 접근 제어 지시자는 public


class B(A):
    def __init__(self):
        print("b.__init__()")


if __name__ == "__main__":

    obj = B()

    print(obj.message)

"""


# A와 B는 상속관계이고, 메세지는 A클래스에 정의되어 있으며 A클래스에서 초기화 되어있다.
# 생성자의 호출은 프로그래머가 불가하며, 프로그래머가 A의 인스턴스 생성 요청을 파이선에게 하면, 파이선이 메모리를 할당하고 난 뒤에
# new 하면서 인스턴스를 생성하면서 자리값을 넘기면서 생성자 함수가 들어간다. => 파이썬은 생성자 안에서 필드를 정의하게끔 한다.
# 상속의 조건에서 자식은 부모의 생성자를 부르면서 부모의 필드를 초기화 할 의무를 가진다. => 초기화 안하면 에러가 난다.
# 여기서는 그 초기화를 위해서 자료형을 정의하지 않았기 때문. A(부모)필드를 초기화 할수 있게끔 자식필드에서 부모의 생성자를 호출한다.
# 부모필드에서도 생성자를 초기화 해줘야 한다. (값을 넣어줘라)
# 자바에서는 자식에서 부모의 생성자를 호출하면 에러가 난다. 파이썬에서도 저런식 (A.__init__(self)) 은 권고하지 않음.


class A:  # 참조 자료형
    def __init__(self):  # 생성자
        print("A.__init()__")
        self.message = "hello"  # message의 접근 제어 지시자는 public


class B(A):
    def __init__(self):
        A.__init__(self)
        print("b.__init__()")


if __name__ == "__main__":
    obj = B()

    print(obj.message)
