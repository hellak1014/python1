class InstanceCounter:
    count = 0 # 클래스 변수 선언

    def __init__(self): # 생성자 정의
        InstanceCounter.count += 1 # 클래스 변수 사용은 가능하지만, 클래스 이름.변수 식으로 써야한다.

    @classmethod # 클래스 이름으로 접근하게끔 되어있는 필드의 값에 최적화 되어진 기능으로 만들어진 매서드. 매개변수 cls 전달 필요. (내 자신의 클래스 이름)
    def print_instance_count(cls):
        print(cls.count)

if __name__ == '__main__':
    x = InstanceCounter()
    x.print_instance_count()

    InstanceCounter.print_instance_count()

    y = InstanceCounter()
    y.print_instance_count()

    InstanceCounter.print_instance_count()

    InstanceCounter.count = 10
    InstanceCounter.print_instance_count()

