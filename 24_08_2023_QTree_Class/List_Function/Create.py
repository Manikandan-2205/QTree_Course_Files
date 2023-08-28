def list_create():
    list = []
    for i in range(15):
        Values = int(input(f"Enter your {i} Elements: "))
        list.append(Values)
    return list
        
