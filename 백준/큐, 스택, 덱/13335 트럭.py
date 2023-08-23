# 큐 이용
# n은 다리를 건너는 트럭의 수/ W는 다리의 길이/ L은 다리의 최대하중
n, w, l = map(int, input().split())
# 트럭의 무게
arr = list(map(int, input().split()))

bridge = [0] * w        # 다리가 수용할 수 있는 크기만큼 리스트 생성
time = 0                # 걸리는 시간

while bridge:       # 다리에 트럭이 있는 동안
    time += 1
    bridge.pop(0)   # 맨 앞을 제거

    if arr:         # 건너야할 트럭이 있으면
        if sum(bridge) + arr[0] > l:    #다리가 버틸 수 있는 무게보다 다리에 있는 트럭 + arr의 0번쨰 인덱스의 합이 더 크면
            bridge.append(0)    # 다리에 0을 추가해줌으로써 한칸 씩 당겨줌
        else:
            bridge.append(arr.pop(0))       # 아니라면 arr의 첫값을 제거하면서 다리에 추가

print(time)