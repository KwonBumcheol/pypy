# 사전
# cabinet = {3:"유재석", 100:"김태호"} # key = 3, 100
# print(cabinet[3])
# print(cabinet[100])
#
# print(cabinet.get(3)) # print(cabinet[3])
# # print(cabinet[5]) # 없는 key -> 이 줄에서 끝냄
# print(cabinet.get(5)) # 없는 key -> None 출력 후 다음 문장도 이어서 읽음
# print(cabinet.get(5, "사용 가능"))
# print("hi")
from grp import struct_group
# print(3 in cabinet) # key 3 있으면 true
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국" # 유재석 -> 김종국 초기화
# cabinet["C-20"] = "조세호"
# print(cabinet)
#
# # 간 손님
# del cabinet["A-3"] # A-3 삭제
# print(cabinet)
#
# # key 들만 출력
# print(cabinet.keys())
#
# # value
# print(cabinet.values())
#
# # key, value
# print(cabinet.items())
#
# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet) # {}

# 튜플() 변경 불가능 <-> 리스트[] 변경 가능
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
#
# # menu.add("생선까스") # 튜플은 add함수 지원x
#
# # name = "김종국"
# # age = 20
# # hobby = ("코딩")
# # print(name, age, hobby)
#
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 세트(set) == 집합
# 중복x, 순서 없음
# my_set = {1, 2, 3, 3, 3}
# print(my_set)
#
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
#
# # 교집합
# print(java & python)
# print(java.intersection(python))
#
# # 합집합
# print(java | python)
# print(java.union(python))
#
# # 차집합
# print(java - python)
# print(java.difference(python))
#
# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
#
# # java를 까먹음
# java.remove("김태호")
# print(java)

# 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu = tuple(menu)
# print(menu, type(menu))
#
# menu = set(menu)
# print(menu, type(menu))

# quiz
from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

users = range(1, 21) # 1~20
# print(type(users))
users = list(users)
# print(type(users))
print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print("--- 당첨자 발표 ---")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--- 축하합니다 ---")