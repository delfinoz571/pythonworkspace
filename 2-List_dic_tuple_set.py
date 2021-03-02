# 리스트 []

subway = [10, 20, 30]
print(subway)

# 캐비넷

cabinet = {1:"ss", 2:"sd", 4:"ff"}
print(cabinet.get(3,"사용가능"))
print(3 in cabinet)

cabinet["c-20"] = "조세호"

del cabinet[1]
print(cabinet)

print(cabinet.keys())

cabinet.clear()

# 튜플 - 변경되지 않는 목록
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

menu = {"돈까스", "치즈까스"}
print(menu)

# 집합 (Set) => 중복안됨 순서없음
my_set = {1,2,3,3,3}
print(my_set) # 1, 2, 3

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 Python을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java나 python 둘 중 하나는 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 줄 알지만, python을 못하는 사람)
print(java - python)
print(java.difference(python))

# 교육을 해서 Python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# 까먹어서 제외
java.remove("양세형")
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

# Quiz
# 파이썬 코딩대회! 댓글이벤트 ㄱㄱ
# 1명은 치킨, 3명은 커피 쿠폰
# 조건1 : 댓글 20명 작성 ID는 1-20
# 조건2 : 무작위 추첨이나, 중복 불가
# 조건3 : random 모듈의 shuffle과 sample 활용

# (출력 예제)
#  -- 당첨자 발표 --
#  치킨 당첨자 : 1
#  커피 당첨자 : [2, 3, 4]
#   -- 축하합니다 --

from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print('''-- 당첨자 발표 --
치킨 당첨자 : {}
커피 당첨자 : {}
-- 축하합니다 --'''.format(winners[0], winners[1:]))