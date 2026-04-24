# 02-2. 문자열 자료형

##문자열을 만드는 방법
# 1. 큰따옴표(" ")
print("Hello World")
# 2. 작은따옴표(' ')
print('Python is fun')
# 3. 큰따옴표 연속 3개
print("""Life is too short, You need python""")
# 4. 작은따옴표 연속 3개
print('''Life is too short, You need python''')

### 문자열 안에 큰/작은따옴표를 포함시키고 싶을 때
# 1. 작은따옴표 포함
print("Python's favorite food is perl")
# 2. 큰따옴표 포함
print('"Python is very easy." he says.')
# 3. 역슬래시 사용
print('Python\'s favorite food is perl')
print("\"Python is very easy.\" he says.")

### 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1. 이스케이프 코드 \n
print("Life is too short\nYou need python")
# 2. 작은따옴표 3개 or 큰따옴표 3개
mul = '''Life is too short
You need python'''
print(mul)

ti = """Life is too short
You need python"""
print(ti)

#----------------------------------------------------------
## 문자열 연산하기
# 문자열 더하기
a = "Python"
b = " is fun!"
print(a+b)  # Python is fun!

### 문자열 곱하기
a = "python"
print(a * 2)    # pythonpython

### 문자열 길이 구하기
a = "All we have is now"
print(len(a))   # 18

### 미니문제. You need python을 문자열로 만들고 길이를 구하라
x = "You need python"
print(len(x))   # 15

#----------------------------------------------------------
## 문자열 인덱싱과 슬라이싱