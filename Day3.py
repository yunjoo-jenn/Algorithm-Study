def solution(bridge_length, weight, truck_weights):
    time = 0    
    bridge = [0] * bridge_length   

    # bridge 위에 최대 bridege length 칸 만큼 있다고 생각
    currentWeight = 0    
    while len(truck_weights) > 0:   
        time+=1
        currentWeight = currentWeight - bridge.pop(0)
        
        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            # bridge 위에 올라갈 수 있기 때문에
            bridge.append(truck_weights.pop(0))
        else: 
            # 올라갈 수 없기 때문에 추가 트럭 없이 다음 칸으로 지나감
            bridge.append(0)

        
    time += bridge_length
    return time 