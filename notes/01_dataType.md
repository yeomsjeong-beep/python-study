## 02-1. 숫자형
### - 주요 연산자
__거듭 제곱 (**)__
```
a = 3
b = 4
print(a ** b)       # 81
```

**나머지 (%)**
```
print(7 % 3)      # 1
```

**나눗셈 vs 몫 vs 나머지**
| 연산자 | 설명 | 예시 | 결과 |
|--------|------|------|------|
| /  | 나눗셈 (소수점 포함) | 7 / 4 | 1.75 |
| // | 몫 (정수만)          | 7 // 4 | 1 |
| % | 나머지               | 7 % 4 | 3 |


**💡 미니문제**
>```
>a = 14 % 3  
>b = 14 // 3  
>print(f"몫: {b}, 나머지: {a}")      # 몫: 4, 나머지: 2
>```

---

## 02-2. 문자열 자료형
문자열(String)이란 **문자, 단어 등으로 구성된 문자들의 집합**을 말한다.

### - 문자열을 만드는 방법
```
"Hello World"       # 큰따옴표
'Python is fun'     # 작은따옴표
"""Life is too short, You need python"""    # 큰따옴표 3개
'''Life is too short, You need python'''       # 작은따옴표 3개
```

### - 문자열 안에 큰/작은따옴표를 포함시키고 싶을 때
**방법 1 - 다른 종류의 따옴표로 감싸기**
```
"Python's favorite food is perl"        # 출력: Python's favorite food is perl
' "Python is very easy." he says.'      # 출력: "Python is very easy." he says.
```
> 큰따옴표가 아닌 작은따옴표로 둘러싼다면 **'Python'이 문자열로 인식**되어 구문 오류 _(SyntaxError: invalid syntax)_ 가 발생한다.

**방법 2 - 역슬래시(\\) 사용**  
역슬래시 뒤의 작은따옴표나 큰따옴표는 문자열을 둘어싸는 기호의 의미가 아니라 "나" 자체를 뜻한다.  
```
'Python\'s favorite food is perl'           # 출력: Python's favorite food is perl  
"\"Python is very easy.\" he says."      # 출력: "Python is very easy." he says.
```

### - 이스케이프 코드
| 코드 | 설명 |
|-----|-----|
| \n | 문자열 안에서 줄을 바꿀 때 사용 |
| \t | 문자열 사이에 탭 간격을 줄 때 사용 |
| \\\ | \를 그대로 표현할 때 사용 |
| \\' | 작은따옴표(' ')를 그대로 표현할 때 사용 |
| \\" | 큰따옴표(" ")를 그대로 표현할 때 사용 |
| \r | 캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
| \f | 폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동) |
| \a | 벨소리(출력할 때 PC 스피커에서 '삑' 소리가 난다) |
| \b | 백 스페이스 |
| \000 | 널 문자 |
이 중에서 활용 빈도가 높은 것은 \n, \t, \\\, \\', \\" 이다.

### - 문자열 연산하기
**문자열 더하기**
```
a = "Python"
b = " is fun!"
print(a+b)      # Python is fun!
```

**문자열 곱하기**
```
a = "python"
print(a * 2)        # pythonpython
```