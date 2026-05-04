## 02-1. 숫자형
### 주요 연산자
| 연산자 | 설명 | 예시 | 결과 |
|--------|------|------|------|
| `**` | 거듭 제곱 | `3 ** 4` | `81` |
| `/` | 나눗셈 (소수점 포함) | `7 / 4` | `1.75` |
| `//` | 몫 (정수만)          | `7 // 4` | `1` |
| `%` | 나머지               | `7 % 4` | `3` |

<details>
<summary>✏️ 미니문제 ㅡ 14를 3으로 나눴을 때, 몫과 나머지를 구하라</summary>

```python
a = 14 % 3  
b = 14 // 3  
print(f"몫: {b}, 나머지: {a}")      # 몫: 4, 나머지: 2
```

</details>

---

## 02-2. 문자열 자료형
문자열(String)이란 **문자, 단어 등으로 구성된 문자들의 집합**을 말한다.

### 문자열을 만드는 방법

```python
"Hello World"       # 큰따옴표
'Python is fun'     # 작은따옴표
"""Life is too short, You need python"""    # 큰따옴표 3개
'''Life is too short, You need python'''       # 작은따옴표 3개
```

### 따옴표를 문자열 안에 포함시키기
**방법 1** ㅡ 다른 종류의 따옴표로 감싸기

```python
"Python's favorite food is perl"        # 출력: Python's favorite food is perl
' "Python is very easy." he says.'      # 출력: "Python is very easy." he says.
```
> 큰따옴표가 아닌 작은따옴표로 둘러싼다면 **'Python'이 문자열로 인식**되어 구문 오류 _(SyntaxError: invalid syntax)_ 가 발생한다.

**방법 2** ㅡ 역슬래시( `\` ) 사용  

```python
'Python\'s favorite food is perl'           # 출력: Python's favorite food is perl  
"\"Python is very easy.\" he says."      # 출력: "Python is very easy." he says.
```

### 이스케이프 코드
| 코드 | 설명 | 자주 쓰임 |
|-----|-----|:---------:|
| `\n` | 문자열 안에서 줄을 바꿀 때 사용 | ✔ |
| `\t` | 문자열 사이에 탭 간격을 줄 때 사용 | ✔ |
| `\\` | `\` 를 그대로 표현할 때 사용 | ✔ |
| `\'` | 작은따옴표 `' '` 를 그대로 표현할 때 사용 | ✔ |
| `\"` | 큰따옴표 `" "` 를 그대로 표현할 때 사용 | ✔ |
| `\r` | 캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동) | |
| `\f` | 폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동) | |
| `\a` | 벨소리(출력할 때 PC 스피커에서 '삑' 소리가 난다) | |
| `\b` | 백 스페이스 | |

### 문자열 연산하기

```python
# 더하기
a = "Python"
b = " is fun!"
print(a+b)      # Python is fun!

# 곱하기
a = "python"
print(a * 2)        # pythonpython

# 문자열 길이
• 길이는 len 함수를 사용하여 구할 수 있다(공백 문자 포함)   
• len 함수는 print 함수처럼 파이썬의 기본 내장 함수로, 별다른 설정 없이 바로 사용할 수 있다.

a = "All we have is now"
print(len(a))   # 18
```

<details>
<summary>✏️ 미니문제 ㅡ "You need python" 의 길이를 구하라</summary>

```python
x = "You need python"
print(len(x))   # 15
```

</details>

### 인덱싱

```python
x = "Try your best rather than be the best"
print(x[2])     # y
print(x[0])    # T
print(x[-1])    # t      ← 뒤에서 첫 번째
```

>파이썬은 0부터 인덱스를 세며, 음수 인덱스는 뒤에서부터 카운트한다

### 슬라이싱
 
```python
x = "Try your best rather than be the best"
print(x[0:5])     # Try y
print(x[:8])      # Try your
print(x[13:21])   #  rather
print(x[14:-1])   # rather than be the bes
```
 
> **주의** `x[시작:끝]`에서 끝 인덱스는 포함되지 않는다 (끝-1까지)
 
**슬라이싱으로 문자열 분리**
 
```python
a = "20230331Rainy"
date    = a[:8]    # 20230331
weather = a[8:]    # Rainy
year    = a[:4]    # 2023
day     = a[4:8]   # 0331
```
 
<details>
<summary>✏️ 응용문제 — "Pithon"에서 'i'를 'y'로 바꾸기</summary>
문자열은 직접 수정이 불가하므로 슬라이싱으로 합친다.
 
```python
a = "Pithon"
# a[1] = 'y'  → TypeError: 'str' object does not support item assignment
b = a[:1] + 'y' + a[2:]
print(b)    # Python
```
 
</details>

### 문자열 포매팅(string formatting)

| 코드 | 대입 타입 | 예시 | 결과 |
|------|----------|------|------|
| `%d` | 정수 | `"I eat %d apples" % 3` | `I eat 3 apples` |
| `%s` | 문자열 | `"I eat %s apples" % "five"` | `I eat five apples` |
| `%f` | 실수 | `"%.1f" % 3.1234` | `3.1` |
| | | `"I eat %.3f apples" % 3.1234` | `3.123` |
| `%%` | % 기호 출력 | `"%d%%" % 98` | `98%` |
 
> **추천** f-string이 가장 간결하다
> ```python
> count = 2
> coffee = "americano"
> print(f"I have {count} {coffee}")   # I have 2 americano
>```

### 정렬 / 소수점

```python
# 전체 길이가 10개인 문자열 공간에 'hi' 라는 문자열은 오른쪽/왼쪽 정렬을 하고, 나머지 공간은 공백으로 채운다.
print("%10s" % "hi")            #         hi   (오른쪽 정렬)
print("%-10sjane." % "hi")      # hi        jane.   (왼쪽 정렬)
 
print("%0.4f" % 3.123456789)    # 3.1235
print("%10.4f" % 3.123456789)   #     3.1235
```

### - format 함수

```python
# 숫자 대입
print("{0}% or nothing".format(100))    # 100% or nothing

# 문자열 대입
print("{0}, think".format("First"))          # First, think

# 숫자 값을 가진 변수로 대입
number = 99
print("{0}% or nothing".format(number))    # 99% or nothing

# 2개 이상의 값
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days".format(number, day))   # I ate 10 apples. so I was sick for three days

# {name} 형태
print("I ate {number} apples. so I was sick for {day} days".format(number=7, day=2))    # I ate 7 apples. so I was sick for 2 days
```