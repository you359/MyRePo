# 사칙연산 함수 정의
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by 0"  # 0으로 나눌 경우
    return a / b


def power(a, b):
    return a ** b


def mod(a, b):
    return a % b


# 함수 테스트 코드
if __name__ == "__main__":
    # 테스트 값
    x = 10
    y = 5

    # 결과 출력
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")
    print(f"{x} ** {y} = {power(x, y)}")
    print(f"{x} % {y} = {mod(x, y)}")

    # 나누기 0 테스트
    print(f"{x} / 0 = {divide(x, 0)}")