# 다중 상속

class A:  # 자료형 A
    def method(self):
        print("A")


class B(A):
    def method(self):  # 매서드 이름은 공통적으로 사용이 가능하다. 같은 자료형에서만 불가능한것. 매서드 오버로딩에서는 불가능함.
        print("B")


class C(A):
    def method(self):
        print("C")


class D(B, C):  # 자바는 지원하지 않으나, C++이나 파이썬은 지원한다. 다중 상속.
    pass


if __name__ == "__main__":
    obj = D()
    obj.method()  # 이렇게 호출되면 B, C, A 셋 중 뭐가 호출 될까? -> 언어 마음이다.
    # 모호성을 가지고 있기 때문에 자바는 다중상속을 지원하지 않는것.
