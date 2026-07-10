def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    raise ValueError(f"지원하지 않는 연산자입니다: {op}")


def main():
    print("간단한 계산기 (종료: q)")
    while True:
        expr = input("수식을 입력하세요 (예: 3 + 4): ").strip()
        if expr.lower() == "q":
            break
        try:
            a, op, b = expr.split()
            result = calculate(float(a), op, float(b))
            print(f"결과: {result}")
        except ValueError as e:
            print(f"입력 오류: {e}")


if __name__ == "__main__":
    main()
