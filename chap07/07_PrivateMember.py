# 파이썬 접근 제어 지시자
# 1. private
# 2. public
# default와 protect는 없음.

class HasPrivate:  # 참조자료형
    def __init__(self):  # 생성자 - 안에는 필드. 필드에는 두가지 접근 방법이 있다.
        self.public1 = "public1"
        self.__private1 = "private1"  # private 설정은 앞에 언더바 2개 + 끝에 언더바 1개로 표현한다.
        self.__private2_ = "private"
        self.__public2__ = "public2"  # 앞 뒤로 두개를 붙이게 되면 public으로 표현된다.

    def print_from_internal(self):
        print(self.public1)
        print(self.__private1)
        print(self.__private2_)
        print(self.__public2__)


if __name__ == '__main__':
    obj = HasPrivate()
    obj.print_from_internal()

    print("=========================")
    print(obj.public1)  # 접근 성공. public1
    # print(obj.__private1)  error. AttributeError: 'HasPrivate' object has no attribute '__private1'
    # print(obj.__private2_) error. AttributeError: 'HasPrivate' object has no attribute '__private2_'
    print(obj.__public2__)  # 접근 성공. public2.