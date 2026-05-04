# # 02-2. 문자열 자료형

# # - 문자열을 만드는 방법
# # 1. 큰따옴표(" ")
# print("Hello World")
# # 2. 작은따옴표(' ')
# print('Python is fun')
# # 3. 큰따옴표 연속 3개
# print("""Life is too short, You need python""")
# # 4. 작은따옴표 연속 3개
# print('''Life is too short, You need python''')

# # - 문자열 안에 큰/작은따옴표를 포함시키고 싶을 때
# # 1. 작은따옴표 포함
# print("Python's favorite food is perl")
# # 2. 큰따옴표 포함
# print('"Python is very easy." he says.')
# # 3. 역슬래시 사용
# print('Python\'s favorite food is perl')
# print("\"Python is very easy.\" he says.")

# # - 여러 줄인 문자열을 변수에 대입하고 싶을 때
# # 1. 이스케이프 코드 \n
# print("Life is too short\nYou need python")
# # 2. 작은따옴표 3개 or 큰따옴표 3개
# mul = '''Life is too short
# You need python'''
# print(mul)

# ti = """Life is too short
# You need python"""
# print(ti)

# #----------------------------------------------------------
# # 문자열 더하기
# a = "Python"
# b = " is fun!"
# print(a+b)  # Python is fun!

# # 문자열 곱하기
# a = "python"
# print(a * 2)    # pythonpython

# # 문자열 길이 구하기
# a = "All we have is now"
# print(len(a))   # 18

# ## 미니문제. You need python을 문자열로 만들고 길이를 구하라
# x = "You need python"
# print(len(x))   # 15

# #----------------------------------------------------------
# # - 문자열 인덱싱
# x = "Try your best rather than be the best"
# print(x[2])     # y
# print(x[0])    # T
# print(x[-1])    # t

# # - 문자열 슬라이싱
# # 방법1
# x = "Try your best rather than be the best"
# y =  x[0] + x[1] + x[2] + x[3] + x[4] + x[5]
# print(y)    # Try yo

# # 방법2
# # x[시작 번호:끝 번호-1] => 0 <= x < 5
# # 숫자를 생략하면 '끝 번호부터 ~' or '~부터 끝번호까지' 라는 뜻이다.
# print(x[0:5])       # Try y
# print(x[:8])         # Try your
# print(x[13:21])    #  rather
# print(x[14:-1])    # rather than be the bes

# # - 슬라이싱으로 문자열 나누기
# a = "20230331Rainy"
# date = a[:8]
# weather = a[8:]
# print(date)         # 20230331
# print(weather)   # Rainy

# year = a[:4]
# day = a[4:8]
# print(year)     # 2023
# print(day)      # 0331

# ## 응용문제
# a = "Pithon"
# print(a[1])     # i
# # a[1] = 'y'      # TypeError: 'str' object does not support item assignment
# print(a)        # Pithon

# b = a[:1] + 'y' + a[2:]
# print(b)        # Python

# # - 문자열 포매팅(string formatting)
# print("I eat %d apples" % 3)        # I eat 3 apples
# print("I eat %s apples" % "five")        # I eat five apples
# print("I ate %d apples. so I was sick for %s days" % (10, "three"))        # I ate 10 apples. so I was sick for three days
# print("I eat %f apples" % 3.1234)        # I eat 3.123400 apples
# print("I eat %.1f apples" % 3.1234)        # I eat 3.1 apples
# print("I eat %.3f apples" % 3.1234)        # I eat 3.123 apples

# # print("Error is %d%" % 98)     # ValueError: incomplete format
# print("Error is %d%%" % 98)     # Error is 98%

# count = 2
# coffee = "americano coffee"
# print(f"I have {count} {coffee}")       # I have 2 americano coffee

# # - 포맷코드와 숫자
# # 1. 정렬과 공백
# print("%10s" % "hi")           #         hi
# print("%-10sjane." % "hi")  # hi        jane.

# # 2. 소수점 표현
# print("%0.4f" % 3.123456789)    # 3.1235
# print("%10.4f" % 3.123456789)    #     3.1235

# - format 함수
print("{0}% or nothing".format(100))    # 100% or nothing
print("{0}, think".format("First"))          # First, think

number = 99
print("{0}% or nothing".format(number))    # 99% or nothing

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days".format(number, day))   # I ate 10 apples. so I was sick for three days

print("I ate {number} apples. so I was sick for {day} days".format(number=7, day=2))    # I ate 7 apples. so I was sick for 2 days