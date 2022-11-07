class ClassVar:  # 자바의 경우 클래스를 선언하면서 반드시 필수적으로 있어야 할건 없다. 매서드, 참조변수 뭐 암튼 암것도 없어도 됨. 인터페이스 생각해봐.
    text_list = []  # 변수 선언하면서 형태가 리스트라는 것을 표시. 근데 이상하지 않니 생성자 안에 필드를 정의해야하는데 왜 아닐까.
    # 이건 static 변수이다. 클래스 변수라고도 함. 글로벌 변수처럼 사용하기 위해서 제공하는 것이 클래스 변수. 어디에서든 동일한 값을 가져오기 위해서.
    # 대표적으로 파이값(PI, 3.14) 자바의 경우 Math{}안에 정의 되어있고, 따로 new 하지 않아도 출력이 가능하다.
    # 근데 new 안해도 왜 사용이 가능하지? => 얘는 자바가 알아서 메모리를 주는 친구. 매서드 영역에 메모리를 저장해준다.
    # 자바가 혼자서 메인을 돌리다가 보고, 클래스 이름을 본 순간 메모리를 할당해준뒤 복귀한다. heap과 stack 영역 매서드를 잘 확인해볼것. 이름 보고 들어와서 무조건 static이 있으면 할당해줌.

    def add(self, text):       # 입력 받은 값을 추가하는 매서드.
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

if __name__ == '__main__' :
    ClassVar.text_list.append('a')
    print(ClassVar.text_list)

    x = ClassVar()
    x.add('b')
    x.print_list()

    print(ClassVar.text_list)

    y = ClassVar()
    y.add('c')
    y.print_list()

    print(ClassVar.text_list)