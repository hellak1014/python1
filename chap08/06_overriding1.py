# Overriding

class A:  # 자료형 A
    def method(self):
        print("A")


class B(A):
    def method(self):  # 매서드 이름은 공통적으로 사용이 가능하다. 같은 자료형에서만 불가능한것. 매서드 오버로딩에서는 불가능함.
        print("B")


class C(A):
    def method(self):
        print("C")


def overrided(overrriding):
    overrriding.method()


if __name__ == "__main__":
    a = A()
   # a.method()

    b = B()
   # b.method()

    c = C()
   # c.method()

    overrided(a)
    overrided(b)
    overrided(c)

    overrided("ABC")   # String에는 저런 메서드를 못받아서 에러.