#bridge_length = 2; weight = 10; truck_weights = [7,4,5,6]
#bridge_length = 100; weight = 100; truck_weights = [10]
bridge_length = 100; weight = 100; truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

from collections import deque
time = 0

passed = []
bridge = [0 for _ in range(bridge_length)]

bridge = deque(bridge)
truck_weights = deque(truck_weights)

while truck_weights or any(bridge):
    print(time, bridge, truck_weights)
    time += 1
    poped = bridge.popleft()

    if poped:
        passed.append(poped)

    # truck 출발 시키기
    if truck_weights and (truck_weights[0] + sum(bridge) <= weight):
        bridge.append(truck_weights.popleft())
    else:
        bridge.append(0)

print(time)