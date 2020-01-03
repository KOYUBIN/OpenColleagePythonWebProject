# 이 함수는 두 개의 숫자 재료를 건내받아 곱한 값과 나눈 값을 고객에게 리턴해준다
def multiplyanddivide(a,b):
    multiplyResult = a * b
    divideResult = a / b
    return multiplyResult, divideResult


result = multiplyanddivide(12, 6)

# 여러개의 값을 리턴하는 함수는 튜플값을 리턴함
print(type(result))
print(result[0])
print(result[1])

# 함수를 호출할 때, 재료를 차례대로 넣는 방법도 있지만 이름을 지정해서 넣는 방법도 있다.
result2 = multiplyanddivide(b=12, a=6)
print(type(result2))
print(result2[0])
print(result2[1])
