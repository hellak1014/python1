class A:
    def __init__(self):  # 생성자 함수
        print("A.__init__()")
        self.message = "hello."


class B(A):
    def __init__(self):  # 부모 클래스의 생성자를 초기화 해야한다.
        super().__init__()  # 부모에 정의되어있는 생성자를 호출하는 super. java 와 같다. 이 방법을 권고한다.
        print("B.__init__()")

        print("self.message is " + self.message)  # A와 B는 상속 관계이기 때문에 다이렉트 접근이 가능하다.


if __name__ == "__main__":
    obj = B()  # B에 대한 인스턴스 생성 요청. 위에 것들을 실행하고 난 뒤 주소값을 가져온다. 이거로 A의 self.message에 접근

    print(obj.message)  # hello.


####################################################################################33


class Base:
    def __init__(self):
        print("Base")  # 필드 정의 없음.


class Derived(Base):
    pass
    # def __init__(self):
    #   super().__init__()

print("==========================")

d = Derived()
# Base 출력. 생성자를 별도로 정의하지는 않았지만, 내부에서는 이걸 보면 super라는 생성자를 디폴트 생성자 함수로 생성해준다.
# def __init__(self): <enter> super().__init__()
