# Set
#   - collection of unique values
#   - mutable
#   - unordered

#   - use {} to create a set

def function1():
    s1 = {11,22,33,44,55}

    print(f"length : {len(s1)}")
    print(f"type : {type(s1)}")
    print(f"s1 : {s1}")

    for val in s1:
        print(val)

#function1()

def function2():

    print(f"Before ops : s1 = {s1}")


    #s1.add(55)
    #s1.add(33)
    #s1.pop()
    s1.remove(22)

    print(f"After ops : s1 = {s1}")

#function2()

def function3():
    s1 = {11,22,33,44}
    s2 = {33,44,55,66} 

    print(f"s1 = {s1}")
    print(f"s2 = {s2}")

    res = s1.union(s2)
    print(f"union = {res}")

    res = s1.intersection(s2)
    print(f"intersection = {res}") 

    res = {11,22}.issubset(s1)
    print(f"issubset = {res}")

    function3()          