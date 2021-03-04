# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     print("출금이 완료되었습니다. 수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance - money - commission))
#     return commission, balance - money - commission


# balance = 0
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)

# balance = withdraw_night(balance, 200)

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 수업

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 가변인자

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "C", "D", "E")


# gun = 10

# def checkpoint(soldiers): # 근무 나가는 군인 수
#     #gun = 20 # 지역변수
#     global gun # 전역공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# Quiz) 표준체중 구하는 프로그램
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         *함수명 : std_weight
#         *전달값 : 키(height), 성별(gender)
# 조건2 : 표준체중은 소수점 둘째자리까지 표시
# 예제 : 키 175cm 남자의 표준체중은 67.38kg 입니다.

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(height, gender, weight))

# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "Java", file=sys.stdout)
# print("python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, score)