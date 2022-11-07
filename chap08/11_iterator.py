# Iterator와 순화 가능한 객체


for i in range(5):  # range(0, 5)
    print(i)

iterator = range(3).__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())


# print(iterator.__next__()) error


#########################################

class Myrange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        print('iter')
        return self  # 현재 할당된 시작 주소 값을 리턴 한다.

    def __next__(self):  # 오버라이딩.
        print('next')
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration()


if __name__ == "__main__":
    print("=====================")
    for i in Myrange(0, 5):
        print(i)  # 반복문이 실행되는 최초 iter 매서드를 호출해주고, next 매서드를 출력해주며 반복문을 구현한다.
        # myrange에 참조자료형을 넣어 주었기 때문에.
