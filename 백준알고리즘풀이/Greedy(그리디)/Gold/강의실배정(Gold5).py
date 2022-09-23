# 9:43~10:12 / 10:22~

# n : 수업 수
# 최소의 강의실을 사용해서 모든 수업을 가능하게 해야함
# 수업이 끝난 직후에 다음 수업 시작 가능
# answer : 모든 수업이 가능한 최소 강의실 개수
# 최적해 방안 : 수업 시작시간 기준으로 정렬하면, 현재 수업이 이전 수업보다 늦게 시작하는 것이 보장되고, 이를 기준으로 수업이 끝났는지만 비교하면서 강의실 추가할지 말지 결정
#============================================================================================================
import sys
import heapq

# n 입력
n = int(sys.stdin.readline())
# 수업 시간(시작시간 , 끝시간) 입력
times = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 중요 - 수업 시간 시작 시간을 기준으로 정렬
times.sort()

# 강의실의 수업 끝 시간 저장 리스트
rooms = [] # 주의 - heapq로 사용할거여도 일단 리스트로 선언
# 중요 - 첫번째 수업을 우선순위 큐에 추가
    # 우선순위 큐 : 수업의 끝 시간들이 정렬 상태를 유지할 수 있도록함
heapq.heappush(rooms, times[0][1])
# 수업 시간을 반복하면서
for i in range(1, n):
    # 만약 현재 수업의 시작시간이 강의실 수업의 끝 시간보다 같거나 이후이면
    if times[i][0] >= rooms[0]:
        # 기존 강의실 수업 제거
        heapq.heappop(rooms)
        # 현재 수업의 끝 시간을 추가
        heapq.heappush(rooms, times[i][1])
    # 만약 현재 수업의 시작시간이 강의실 수업의 끝 시간보다 이전이면
    else:
        # 현재 수업의 끝 시간을 추가(새 강의실 추가)
        heapq.heappush(rooms, times[i][1])

# answer 출력
print(len(rooms))