# 12:20~12:30
# n : 주어진 숫자
# k : 나누는 수
#============================================================================================
n, k = map(int, input.split())

result = 0
while n != 1:
    result += 1
    if n % k == 0:
        n //= k
        continue
    n -= 1

print(result)

#==========================================================================================
# 개선코드
# 문제에서는 N의 범위가 10만 이하이므로 일일이 1씩 빼도 되지만,
# N이 100억 이상의 큰 수가 되는 경우를 가정했을 때 빠르게 동작하려면, N이 K의 배수가 되도록 효율적으로 한번에 빼는 방식 사용해야 함
#==========================================================================================
n, k = map(int, input.split())
result = 0

while True:
    # 1. 일일이 1씩 빼지않고 1씩 빼야되는 횟수 계산하기
    # n == k 로 나누어 떨어지는 수 계산
    target = (n // k) * k
    # 1씩 빼는 횟수 더하기
    result += (n-target)
    # 1씩 빼고 남은 나누어떨어지는 숫자
    n = target

    # 2. 나누기 수행
    # N이 K보다 작을 때(더이상 나눌수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대해 1이 될때까지 1씩 빼야되는 횟수 더하기
result += (n-1)