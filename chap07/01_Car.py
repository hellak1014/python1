class Car:                   # 자바에서는 중괄호 안에 매서드 생성자 변수 등을 적었지만 여기에는 :를 사용한다.
    def __init__(self):      # 생성자 정의. self는 메모리를 할당하는 순간 시작 주소값을 가지고 있다. (java의 this와 같음)
        self.color = 0xFF0000
        # 필드 선언. 따로 필드를 두지 않고 생성자 안에서 필드를 선언한다. 이때 가져온 self 주소값은 생략이 불가능하다.
        # 그리고 필드값 초기화. 이 필드는 차량의 색상에 관련된 것이다.
        self.wheel_size = 16     # 바퀴의 크기
        self.displacement = 2000           # 엔진 배기량

    def forward(self):      # 차량의 기능 정의 - 나중에 만들거다. 전진 기능
        pass                # 에러를 안내기 위한 pass

    def backward(self):     # 후진
        pass

    def turn_left(self):    # 좌회전
        pass

    def turn_right(self):   # 우회전
        pass

if __name__=='__main__':
    # java는 new(메모리 할당). 파이썬은 메인임을 알려주는 main (메모리 할당)
    my_car = Car()
    # 함수 호출하듯 호출 하면 new 하듯이 해줄게

    # 1. 이름과 같은 자료형 찾음 찾으면 메모리 할당
    # 2. self 키워드에 주소값 넣기
    # 3. __init__ 호출
    # 4. 주소값 리턴.

    print('0x{:02X}' .format(my_car.color)) # 정수의 값을 두자리로. x의 값을 16진수로 뽑아라.
    print(my_car.wheel_size)
    print(my_car.displacement)

    my_car.forward() # my_car 매서드 접근. 매서드 호출시에는 self를 넣지 않는다.
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()

# 파이선은 변수 선언하는 필드가 없다. 파이선은 생성자와 매서드로 정의한다.
# 이때 기능정의에 사용되는 함수는 object의 특징으로 정의되는 기능이라고 한다. = 매서드
# 파이선-데이터분석의 객체지향 -> 하나의 레코드를 object로 본다. 철수의 데이터. 영희의 데이터. 
# 순수하게 데이터를 관리할 목적으로 필드를 정의하고 getter setter로 관리하는 것을 자바빈(VO)이라고 부른다.
# 일반적인 자료형은 속성(색, 크기, 배기량)과 기능(전진, 후진, 좌,우회전)으로 정의된다.
