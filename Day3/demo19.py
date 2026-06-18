# Tuple
#   collection of similar or dissimilar type of values
#   immutable
#   ordered

#   Create
#       myTuple = (11, 22, 33, 44, 55)
#       myVar = tuple(....)

def function():
    t1 = (11,22,33,44,55)

    print(f"length : {len(t1)}")
    print(f"type : {type(t1)}")
    print(f"t1 : {t1}")

    print(f"t1[0] = {t1[0]}")
    print(f"t1[4] = {t1[4]}")

    print("t1 : ")
    for val in t1:
        print(val)

#function1()
# 

def function2():
    t1 = (11,22,33,44,55) 

    print(f"index of 22 = {t1.index(22)}")
    print(f"count of 33 = {t1.count(33)}")       

#function2()

def function3():
     studInfo = (12, "abc", 12, 85.0)

     print(f"length = {len(studInfo)}")   
     print(f"type : = {type(studInfo)}")
     print(f"studInfo : {studInfo}")

     for field in studInfo:
        print(f"{field} ({type(field)})")

function3()

