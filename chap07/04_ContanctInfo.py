class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}' .format(self.name, self.email))


if __name__ == '__main__':
    hong = ContactInfo('홍길동', 'aaa@aaa.com') # 인스턴스 생성 요청. init를 호출하면서 2개의 데이터를 받게 된다. 메모리 할당 받으면서 self에 시작주소값 리턴
    lee = ContactInfo('이순신', 'bbb@bbb.com')

    hong.print_info()
    lee.print_info()