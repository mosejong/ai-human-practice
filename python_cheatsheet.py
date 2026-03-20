# python_cheatsheet.py

"""
========================================
Python / OOP / File / ML 기초 치트시트
========================================

목적:
- 지금까지 배운 내용을 한 파일에 정리
- 나중에 "이럴 때 뭐 쓰지?" 할 때 빠르게 참고
- 실습할 때 복붙용 / 복습용

주의:
- 이 파일은 실행용이라기보다 참고용 정리 파일
- 필요한 부분만 복사해서 실습에 사용하면 됨
"""

# ========================================
# 1. 출력 / 변수 / 자료형
# ========================================

# print() : 출력할 때 사용
print("Hello, Python")

# 변수 : 값을 저장하는 이름
name = "모세종"
age = 30
height = 175.5
is_student = True

# 자료형 확인
print(type(name))       # str
print(type(age))        # int
print(type(height))     # float
print(type(is_student)) # bool

# 여러 변수 한 번에 출력
print(name, age, height, is_student)

# f-string : 문자열 안에 변수 넣기
print(f"이름: {name}, 나이: {age}")


# ========================================
# 2. 연산자
# ========================================

a = 10
b = 3

# 산술 연산자
print(a + b)   # 덧셈
print(a - b)   # 뺄셈
print(a * b)   # 곱셈
print(a / b)   # 나눗셈
print(a // b)  # 몫
print(a % b)   # 나머지
print(a ** b)  # 제곱

# 비교 연산자
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# 논리 연산자
print(a > 5 and b < 5)
print(a > 20 or b < 5)
print(not a == b)


# ========================================
# 3. 문자열
# ========================================

text = "Python Study"

print(text[0])      # 첫 글자
print(text[-1])     # 마지막 글자
print(text[0:6])    # 슬라이싱
print(len(text))    # 길이

print(text.lower())       # 소문자
print(text.upper())       # 대문자
print(text.replace("Study", "Practice"))
print(text.split())       # 공백 기준 분리

# 문자열 연결
first = "AI"
second = "Human"
print(first + " " + second)


# ========================================
# 4. 리스트 / 튜플 / 딕셔너리 / 집합
# ========================================

# 리스트(list) : 수정 가능
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("orange")
fruits.remove("banana")
print(fruits)

# 튜플(tuple) : 수정 불가
point = (10, 20)
print(point[0])

# 딕셔너리(dict) : key-value
student = {
    "name": "홍길동",
    "age": 25,
    "major": "AI"
}
print(student["name"])
student["age"] = 26
student["grade"] = "A"
print(student)

# 집합(set) : 중복 제거
numbers = {1, 2, 2, 3, 4, 4}
print(numbers)


# ========================================
# 5. 조건문
# ========================================

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 삼항 연산자
result = "합격" if score >= 60 else "불합격"
print(result)


# ========================================
# 6. 반복문
# ========================================

# for문
for i in range(5):
    print("for문:", i)

# 리스트 순회
for fruit in fruits:
    print("과일:", fruit)

# while문
count = 0
while count < 3:
    print("while문:", count)
    count += 1

# break / continue
for i in range(10):
    if i == 3:
        continue  # 3은 건너뜀
    if i == 7:
        break     # 7에서 종료
    print(i)


# ========================================
# 7. 함수
# ========================================

def greet(name):
    """이름을 받아 인사하는 함수"""
    return f"{name}님 안녕하세요"

print(greet("세종"))

def add(x, y):
    return x + y

print(add(3, 5))

# 기본값 매개변수
def power(base, exponent=2):
    return base ** exponent

print(power(3))    # 3^2
print(power(3, 3)) # 3^3


# ========================================
# 8. 예외 처리
# ========================================

try:
    num = int("10")
    print(num)
except ValueError:
    print("숫자로 변환할 수 없습니다.")
finally:
    print("예외 처리 종료")


# ========================================
# 9. 클래스 / 객체지향(OOP)
# ========================================

class Person:
    """사람 정보를 저장하는 클래스"""

    def __init__(self, name, age):
        # 생성자: 객체가 만들어질 때 자동 실행
        self.name = name
        self.age = age

    def introduce(self):
        return f"이름은 {self.name}, 나이는 {self.age}살입니다."

p1 = Person("세종", 30)
print(p1.introduce())


# ========================================
# 10. 상속
# ========================================

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "소리를 냅니다."

class Dog(Animal):
    def speak(self):
        return "멍멍"

dog = Dog("초코")
print(dog.name)
print(dog.speak())


# ========================================
# 11. 은행 계좌 예제 (클래스 실습 느낌)
# ========================================

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원 입금 완료. 현재 잔액: {self.balance}원")

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount
            print(f"{amount}원 출금 완료. 현재 잔액: {self.balance}원")

    def show_balance(self):
        print(f"{self.owner}님의 잔액: {self.balance}원")

account = BankAccount("세종", 10000)
account.deposit(5000)
account.withdraw(3000)
account.show_balance()


# ========================================
# 12. 파일 입출력
# ========================================

# 파일 쓰기(write)
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("안녕하세요\n")
    file.write("파이썬 파일 처리 연습입니다.\n")

# 파일 읽기(read)
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 한 줄씩 읽기
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# 파일 추가(append)
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("한 줄 더 추가합니다.\n")


# ========================================
# 13. 모듈 import
# ========================================

import math
import random

print(math.sqrt(16))        # 제곱근
print(random.randint(1, 6)) # 1~6 랜덤 숫자

# 특정 함수만 가져오기
from math import pi
print(pi)


# ========================================
# 14. 많이 쓰는 문법 팁
# ========================================

# 언더스코어(_) :
# - 변수명 연결용 ex) user_name
# - 반복문에서 값 안 쓸 때 ex) for _ in range(3)

user_name = "mosejong"

for _ in range(3):
    print("반복")

# 백슬래시(\) :
# - 이스케이프 문자에 사용
print("안녕하세요\n반갑습니다")
print("이름:\t세종")
print("큰따옴표 출력: \"Python\"")

# 주석:
# 한 줄 주석

"""
여러 줄 주석처럼
정리할 때 자주 사용
"""


# ========================================
# 15. 리스트 컴프리헨션
# ========================================

numbers = [1, 2, 3, 4, 5]

squared = [x ** 2 for x in numbers]
print(squared)

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


# ========================================
# 16. 머신러닝 기본 흐름
# ========================================

"""
머신러닝 기본 순서:
1. 데이터 불러오기
2. X, y 분리
3. train / valid(or test) 분리
4. 모델 생성
5. 모델 학습(fit)
6. 예측(predict)
7. 평가(score, accuracy 등)
"""

# 아래 코드는 예시용
# 실제 실행하려면 scikit-learn 설치 필요


# ========================================
# 17. train_test_split
# ========================================

from sklearn.model_selection import train_test_split

# 예시 데이터
X = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
y = [0, 0, 0, 1, 1, 1]

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y,
    test_size=0.2,      # 검증용 데이터 20%
    random_state=42     # 결과 고정
)

print("X_train:", X_train)
print("X_valid:", X_valid)


# ========================================
# 18. 분류 모델 예시
# ========================================

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Decision Tree
model_dt = DecisionTreeClassifier(random_state=42)
model_dt.fit(X_train, y_train)
pred_dt = model_dt.predict(X_valid)

# RandomForest
model_rf = RandomForestClassifier(random_state=42, n_estimators=100)
model_rf.fit(X_train, y_train)
pred_rf = model_rf.predict(X_valid)


# ========================================
# 19. 모델 평가 지표
# ========================================

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 예시용 실제값/예측값
y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]

print("accuracy :", accuracy_score(y_true, y_pred))
print("precision:", precision_score(y_true, y_pred))
print("recall   :", recall_score(y_true, y_pred))
print("f1       :", f1_score(y_true, y_pred))

"""
accuracy  : 전체 중 맞춘 비율
precision : 양성이라고 예측한 것 중 실제 양성 비율
recall    : 실제 양성 중 맞춘 비율
f1 score  : precision과 recall의 균형
"""


# ========================================
# 20. RandomForest 하이퍼파라미터
# ========================================

# 기본 모델
model_rf_1 = RandomForestClassifier(random_state=42, n_estimators=100)

# 트리 개수 증가
model_rf_2 = RandomForestClassifier(random_state=42, n_estimators=200)

# 깊이 제한
model_rf_3 = RandomForestClassifier(
    random_state=42,
    n_estimators=200,
    max_depth=10
)

"""
하이퍼파라미터 팁:
- n_estimators:
    트리 개수
    많아지면 성능이 좋아질 수 있지만 시간도 오래 걸림

- max_depth:
    트리 깊이 제한
    너무 깊으면 과적합 가능
    적절히 제한하면 일반화 성능이 좋아질 수 있음

- random_state:
    결과를 고정하고 싶을 때 사용
"""


# ========================================
# 21. 모델 비교 출력 예시
# ========================================

# 실제 실습에서 이런 식으로 많이 씀
# (아래는 구조 예시)

"""
print("RandomForest 1")
print("accuracy :", accuracy_score(y_valid, pred_rf_1))
print("precision:", precision_score(y_valid, pred_rf_1))
print("recall   :", recall_score(y_valid, pred_rf_1))
print("f1       :", f1_score(y_valid, pred_rf_1))

print("-" * 30)

print("RandomForest 2")
print("accuracy :", accuracy_score(y_valid, pred_rf_2))
print("precision:", precision_score(y_valid, pred_rf_2))
print("recall   :", recall_score(y_valid, pred_rf_2))
print("f1       :", f1_score(y_valid, pred_rf_2))
"""

"""
모델 비교할 때 보는 포인트:
- accuracy만 보지 말기
- precision / recall / f1 같이 보기
- 어느 파라미터에서 성능이 좋아졌는지 확인
- 깊이 제한이 성능 향상인지 과한 제한인지 확인
"""


# ========================================
# 22. 실습할 때 자주 쓰는 출력 구분선
# ========================================

print("=" * 50)
print("실습 결과 확인")
print("=" * 50)


# ========================================
# 23. 내가 기억해야 할 핵심 팁
# ========================================

"""
[파이썬]
- 변수는 값을 저장한다
- 리스트는 수정 가능, 튜플은 수정 불가
- 딕셔너리는 key:value 구조
- 조건문/반복문은 들여쓰기 중요
- 함수는 반복되는 코드를 묶는다

[객체지향]
- 클래스는 설계도
- 객체는 클래스로 만든 실제 데이터
- __init__은 생성자
- self는 자기 자신 객체
- 상속을 사용하면 기존 클래스를 재사용 가능

[파일처리]
- with open()을 많이 사용
- "r" 읽기, "w" 쓰기, "a" 추가
- encoding="utf-8" 습관 들이기

[머신러닝]
- fit() : 학습
- predict() : 예측
- train_test_split() : 데이터 분리
- accuracy만 보지 말고 precision, recall, f1 같이 보기
- random_state=42 자주 사용
"""


# ========================================
# 24. 나중에 추가할 예정인 것들
# ========================================

"""
추가 예정:
- pandas
- numpy
- matplotlib
- logistic regression
- scaling
- confusion matrix
- up/down game 코드 정리
- git 명령어 정리
"""