# IF
# weather = input("오늘 날씨는 어떄요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지 마세요")

# FOR
# for waiting_no in range(1, 6):
#     print(waiting_no)

# starbucks = {"아이언맨", "토르", "그루트"}
# for wait in starbucks:
#     print("{}, 커피가 준비되었습니다".format(wait))

# WHILE
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "토르"
# person = "unknown"
# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# absent = [2, 5] # 결석
# no_book = [7]
# for student in range(1, 11): # 1-10까지의 출석번호
#     if student in absent:
#         continue # 계속해서 반복문 진행
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break # 반복문 탈출
#     print("{0}, 책을 읽어봐".format(student))

# 한 줄 For
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# Quiz) 50명의 승객과 매칭 기회가 있는 택시기사
# 아래 2가지 조건에 대해 승객 구분하고 매칭된 수를 구하시오
# 조건1 : 승객별 운행 소요시간은 5-50분 사이의 난수
# 조건2 : 소요시간 5-15분 사이만 매칭
# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분) 등등등
# 총 탑승 승객 : 2분

from random import *

total = 0
for i in range(1, 51):
    ride_time = randrange(5, 51)
    if ride_time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, ride_time))
        total += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, ride_time))
        
print("총 탑승 승객 : {0}".format(total))