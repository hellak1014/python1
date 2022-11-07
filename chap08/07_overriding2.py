class Car:
    def ride(self):
        print("Run")


class FlyingCar(Car):
    def ride(self):
        # super.ride()  자바는 이렇게 하면 되지만 파이썬은 안됨.
        super().ride()  # 상속의 조건 하에서 부모 생성자 호출  할때도 이런 식으로 했다. 매서드에 대한 호출도 마찬 가지.
        print("Fly")


if __name__ == "__main__":
    # car = Car()    Car 인스턴스 생성. 그런데 부모 클래스는 보통 독립적으로 사용하기 위해 만드는 게 아니다.
    # car.ride()     자식들의 공통점을 모아서 제공 하기 위한 클래스.

    my_car = FlyingCar()  # FlyingCar 인스턴스 생성
    my_car.ride()  # 자식의 클래스 안에서 super로 부모 것도 호출 되었기 때문에 부모의 ride + 자식의 ride가 둘다 출력되는 것.
