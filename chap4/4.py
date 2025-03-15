# 슬라이싱
# jumin = "990120-1234567"
#
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 ~ 1
#
# print("뒤 7자리 : " + jumin[-7:])

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
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")