#from my_package.calculator import plus
#from my_package.calculator import minus
#from~import 기능. 여기에서 작성해둔 모듈을 추가할 수 있다.

#from my_package.calculator import plus, minus, multiply, divide
#따로따로 정의해도 되지만 ,를 이용하여 한번에도 가능하다.

from my_package.calculator import *
#한번에 지정도 가능하다. *을 이용. 

print(plus(10, 5))
print(minus(10, 5))
print(multiply(10,5))
print(divide(10,5))