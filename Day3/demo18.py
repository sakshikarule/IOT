# List

#   collection of similar or dissimilar type of values
#   mutable
#   ordered

#   creation
#       varName = [11, 22, 33, 44, 55]
#       varName = list()            -- empty list
#       varName = list(range(10))

def function():
    list1 = [11,22,33,44,55]

    print(f"length : {len(list1)}")
    print(f"type : {type(list1)}")
    print(f"list1 : {list1}")

    print(f"list1[0] = {list1[0]}")
    print(f"list1[3] = {list1[3]}")
    
    print("list1 using for loop : ", end="")
    for ele in list1:
        print(f" {ele}", end="")
    print("")

#function

def function2():
    list1 = [11,22,33,44,55]

    print(f"Before ops : list1 = {list1}")

    #list1.append(50)            # appended at the end of list
    #list1.insert(2, 50)         # value will be inserted at index

    #list1.pop()                   # last value will be deleted
    #list1.remove(33)              # value will be removed

    #list1.reverse()
    list1.clear()

    print(f"After ops : list1 = {list1}")

    #function2()

def function3():
     studInfo = [12, "abc", 12, 85.0]

     print(f"length = {len(studInfo)}")
     print(f"type : {type(studInfo)}")
     print(f"stuInfo : {studInfo}")

     for field in studInfo:
         print(f"{field} ({type(field)})") 
function3()