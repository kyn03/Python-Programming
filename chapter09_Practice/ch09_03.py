class Student:
    def __init__(self,name):
        self.name=name
        self.score=[] #빈리스트

    def add_score(self,score): # 리스트에 성적을 추가하는 메소드
        self.score.append(score)
        print(f"{self.name}의 성적 {score}점이 추가되었습니다.")

    def cal_avg(self):
        if not self.score:
            return 0
        return sum(self.score)/len(self.score) # 평균 연산
    
# 학생 인스턴스 생성
stu = Student("Kim")
    
stu.add_score(90)
stu.add_score(70)
stu.add_score(80)

avg = stu.cal_avg()
print(f"{stu.name}의 평균 성적은 {avg:.2f}")