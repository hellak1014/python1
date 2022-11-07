# 다형성 (Polymorphism)
# 상속의 조건 관계에서만 사용할 수 있는 개념.
# 자식 클래스의 인스턴스를 생성했을때 그 인스턴스를 당연히 자식 자료형으로 바라보는 것이 정상이나, 상속의 조건하에서는
# 부모의 자료형으로도 자식을 바라볼 수 있다는 것이 다형성이다.
# Computer nb = new NoteBook(). 노트북 안에는 컴퓨터의 기능이 담겨있다. 컴퓨터(부모)-노트북(자식).
# 따라서 노트북 보고 노트북 샀네? 맞는말. 컴퓨터 샀네? 도 맞는 말. 컴퓨터 + a (이동성, 휴대성) = 노트북.
# 조카가 만약에 노트북 보고 컴퓨터라고 말한다면, 이 a를 생각하지 않고 있다는 것.
# 컴퓨터(부모)에 잇는 생성자와 변수에 추가적인 것을 더해서 노트북(자식)이라고 한것. 따라서 노트북의 휴대성이나 이동성같은
# 추가적인 기능을 부모에서 호출하면 에러를 낸다.
# 노트북 삼 -> 컴퓨터 샀네? ㅇㅋ. 컴퓨터 삼 -> 노트북 샀네? 아님. 부모를 자식의 자료형으로 바라볼 수 없다.

class Suite:
    pass


class Armorsuite:
    def armor(self):
        print('armored')


class Ironman(Armorsuite):
    pass


def get_armored(suite):
    suite.armor()


if __name__ == '__main__':
    suite = Armorsuite()

    get_armored(suite)

    iron_main = Ironman()
    get_armored(iron_main)

    # suite = Suite() # Suite 안에는 이런거 없다.
    # get_armored(suite)
