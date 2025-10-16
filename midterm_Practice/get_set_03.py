# 접근자/설정자 사용(정상적이지 않은 경우)
class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age  #private 아님

x = Friend("홍길동", 20)
x.age = -5  # 잘못된 값 방지
print(x.age)