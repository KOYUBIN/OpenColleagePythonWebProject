def calc(calctype, a, b):
    if calctype == "더하기":
        return a + b
    elif calctype == "빼기":
        return a - b
    elif calctype == "나누기":
        return a / b
    elif calctype == "곱하기":
        return a * b
    else:
        print("다시입력하세요")


print("더하기, 빼기, 나누기, 곱하기")
calctype = input(str("계산정보를 입력하세요: "))
a = int(input("첫번째 숫자: "))

b = int(input("두번째 숫자: "))

result = calc(calctype, a, b)
print("계산결과 :" + str(result))
