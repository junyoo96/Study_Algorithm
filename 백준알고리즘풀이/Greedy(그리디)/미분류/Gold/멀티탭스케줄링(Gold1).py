# 10:40~10:57 / 11:01~
# 10:35~10:44 / 10:44~ - 틀림(꽂혀있는 플러그중 가장 나중에 사용하는 플러그 뽑는다는 아이디어 생각못함)
# 4:41~4:57/4:57~ - 틀림(저번처럼 꽂혀있는 플러그중 가장 나중에 사용하는 플러그 뽑는다는 아이디어 생각못함)
# 11:42~12:05/12:05~12:15

# n : 멀티탭 구멍 개수
# k : 플러그(전기용품)의 총 사용횟수
# answer : 하나씩 플러그를 빼는 최소 횟수
# 최적해 방안
    # 플러그가 모두 꽂혀있을 때 새 전기용품이 들어오는 경우 꽂혀있는 플러그중 다음 기준에 해당하는 플러그를 우선적으로 뽑기
        # 1. 현재 꽂혀있는 플러그 중 이후에 사용하지 하지 않는 플러그
        # 2. 꽂혀있는 플러그 모두 이후에 사용한다면 가장 나중에 사용하는 플러그
#=========================================================
import sys

# answer
answer = 0
# n, k 입력
n, k = map(int, sys.stdin.readline().split())
# 플러그 사용순서 입력
uses = list(map(int, sys.stdin.readline().split()))

# 꽂혀있는 플러그 리스트
plugs = []
# 플러그 사용순서를 반복하면서
for i in range(k):
    # 만약 이미 같은 플러그가 이미 꽂혀있다면
    # 주의 - if len(plugs) != n: 문 보다 먼저 위치해야함 / if len(plugs) != n: 문보다 먼저 오게 될 경우 같은 플러그가 이미 꽂혀있어도 동일한 플러그를 꽂게 되는 케이스를 방지 못함
    if uses[i] in plugs:
        continue
    # 만약 콘센트가 모두 차 있지 않다면
    if len(plugs) != n:
        # 콘센트에 플러그 꽂기
        plugs.append(uses[i])
        continue

    # 밑에서부터는 콘센트가 모두 차 있는 경우 새 플러그를 뽑기 위해 어떤 플러그를 뽑을지 결정하는 코드
    # 콘센트에 현재 꽂혀있는 플러그 중 가장 나중에 사용할 플러그의 인덱스(uses리스트에서 현재 사용할 플러그의 인덱스가 0으로 시작)
    most_far = 0
    # 콘센트에서 바꿀 플러그
    tmp = 0
    # 현재 꽂혀있는 플러그를 반복하면서
    for p in plugs:
        # 중요 - 만약 현재 꽂혀있는 플러그를 이후에 사용할 예정이 없다면
        if p not in uses[i:]:
            # 콘센트에서 뺄 플러그 저장
            tmp = p
            break
        # 중요 - 만약 현재 꽂혀있는 플러그가 현재 꽂혀있는 플러그들 중 가장 이후에 사용할 플러그라면
        elif uses[i:].index(p) > most_far:
            # 가장 나중에 사용할 플러그 갱신
            most_far = uses[i:].index(p)
            # 콘센트에서 뺄 플러그 저장
            tmp = p
    # 꽂혀있는 플러그중 바꿀 플러그를 빼고 현재 플러그 꽂기
    plugs[plugs.index(tmp)] = uses[i]
    # 플러그 뺏기 때문에 횟수 증가
    answer += 1

# answer 출력
print(answer)