# 생성자 안에 정해져 있는 필드. new 해야지만 설정되는 필드.

class InstanceVar:
    def __init__(self):
        self.text_list = []  # 멤버변수(fieid)

    def add(self, text):     # 멤버 메서드
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list) # 정의만 되어있지 아직 관심도 없음.

if __name__ == '__main__':
   # InstanceVar.text_list.append('a')  error. AttributeError: type object 'InstanceVar' has no attribute 'text_list'

    x = InstanceVar()              # 인스턴스 생성해줘 요청
    x.add('a')
    x.print_list()
    print(x.print_list())
