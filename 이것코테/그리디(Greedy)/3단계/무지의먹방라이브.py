import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐를 사용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i] , i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # (sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수) 한 시간이 k(방송이 중단되는 시간 전이라면)
        # 현재의 음식 시간 - 이전 음식 시간
            # 시간이 적은 음식부터 먹는데 지나간 시간을 계산을 한번에 계산할 때
            # 현재의 음식 시간을 현재 음식 개수만큼 곱해서 더해주게 되면 실제로 그만큼 시간이 지나간 것이 것이 아니라, 이전 음식 시간을 더해줄 때 현재 음식 시간도 같이 그만큼 처리가 된것이므로
            # 실제로는 이전 음식을 다먹는데 걸리는 시간과 현재 음식을 다 먹는데 걸리는 시간의 차이 * 현재 음식개수 만큼만 더해주어야함
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] # 현재 음식만을 먹는데 걸리는 시간
        sum_value += (now - previous) * length # 현재 음식을 다 먹는데 걸리는 시간
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x : x[1]) # 음식의 번호 기준으로 정렬
    # k- sum_value
        # 네트워크 지연 시간에서 현재까지 음식먹었던 누적 시간을 빼줌(아까, 누적시간이 네트워크 지연 시간을 넘어가 버리면 그 때 먹으려고 했던 음식에서 다시 계산해주어야되서)
    # (k - sum_value) % length
        # 네트워크 지연이후 어떤 음식부터 먹어야 하는지 index계산
    return result[(k - sum_value) % length][1]

#======================================================================================
# # 옛날 코드
# from queue import PriorityQueue
#
# food_times=[3, 1, 2]
# k=5
#
# def solution(food_times, k):
#     #food_times : 먹을 음식의 각각 걸리는 시간을 저장해놓은 리스트
#     #k : 네트워크 지연 시간
#     answer = 0
#
#     que=PriorityQueue() #우선순위 큐 사용, 먹는데 시간이 적게 걸리는 순서대로 음식 정렬하기 위해
#     #입력 받아서 먹는데 시간이 적게 걸리는 순서대로 정렬
#     for index,value in enumerate(food_times):
#         que.put((value,index+1)) #이때, queue의 indxe로는 0번째 음식이 1번째 음식이기 때문에 +1해줌
#
#     sum_food_time=0 # 지금까지 먹은 누적 시간
#     current_que_length = len(food_times) #현재 남은 음식 개수
#     previous_food_time=0 #이전에 먹었던 음식의 걸리는 시간 저장
#
#     if sum(food_times)<=k: #전체 음식먹는데 걸리는 시간보다 k가 크면
#         return -1
#
#     while True: # 현재까지 먹은 누적 시간이 k를 넘지 않을 때 까지 반복
#
#         #현재 남아있는 음식 개수 중 제일 시간이 적게 걸리는 것을 다 먹는데 걸리는 시간 계산
#         food_time_to_eat_current_food_all=(que.queue[0][0]-previous_food_time)*current_que_length # (현재 먹은 음식에 걸리는 시간 - 이전에 먹은 음식의 걸리는 시간) * 현재 남아있는 음식 개수
#
#         #이전까지 먹은 누적 시간 + 지금 음식 다 먹는데 거리는 시간의 합
#         current_food_time = food_time_to_eat_current_food_all+sum_food_time
#         if current_food_time >=k: # 만약 k보다 크면, 네트워크 지연 시간보다 더 걸리는 거니까 멈춰야함
#             break
#
#         que_first = que.get()[0] # 지금먹은 음식의 먹는데 걸리는 시간
#         previous_food_time=que_first #이전에 먹은 음식의 걸리는 시간에 지금먹은 음식의 먹는데 걸리는 시간 저장
#         sum_food_time+=food_time_to_eat_current_food_all # 지금까지 먹은 누적 시간에 현재 음식 먹는데 걸린 시간 더해줌
#         current_que_length -= 1 #먹는데 제일 적게 걸리는 음식 다 먹었으니 전체 음식 개수 줄이기(전체 음식에서 다 먹은 음식 빼는거)
#
#     #누적 시간이 k를 넘었을 때
#     #queue(현재 남은 먹을 음식 담고있는거)를 다시 index 기준으로 정렬
#     sorted_que=sorted(que.queue,key=lambda index: index[1])
#
#     k-=sum_food_time # 네트워크 지연 시간에서 현재까지 음식먹었던 누적 시간을 빼줌(아까, 누적시간이 네트워크 지연 시간을 넘어가 버리면 그 때 먹으려고 했던 음식에서 다시 계산해주어야되서)
#     target_index=k%current_que_length # 네트워크 지연이후 어떤 음식부터 먹어야 하는지 index계산
#     answer=sorted_que[target_index][1] #계산한 index에 해당하는 실제 음식의 index값 찾기
#     return answer