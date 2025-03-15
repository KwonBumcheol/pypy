# 슬라이싱
# jumin = "990120-1234567"
#
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 ~ 1
#
# print("뒤 7자리 : " + jumin[-7:])
from idlelib.debugobj import myrepr
from idlelib.replace import replace
from runpy import run_path

# 문자열 처리

# python = "Python is Amazing"
# print(python.lower()) # 소문자
# print(python.upper()) # 대문자
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java")) # 값 교체
#
# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
#
# print(python.find("Java")) # 없는 값이면 -1
# # print(python.index(("Java"))) # error -> exit
# print("hi")
#
# print(python.count("n")) # n의 수

# 문자열 포맷

# 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
# %s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파린", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파린", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파린", "빨간"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4(v3.6 ~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
# print("백문이 불여일건 \n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
# print("~\\pypy main !2 ?1 ")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스(한글자 삭제)
# print("Redd\bApple")

# \t : tab

# quiz
# url = "http://naver.com"
# my_str = url.replace("http://", "") # http:// -> 공백
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 리스트[]
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)
#
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
#
# print(subway.index("조세호"))
#
# # 하하가 다음 정류장에서 다음칸에 탐
# subway.append("하하")
# print(subway)
#
# subway.insert(1, "정형돈")
# print(subway)
#
# print(subway.pop())
# print(subway)
#
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석")) # 유재석이 나온 횟수

# 정렬
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)
#
# # 뒤집기
# num_list.reverse()
# print(num_list)
#
# # 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


