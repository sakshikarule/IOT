
def function1():
    l1 = [[1, 2, 3, 4],
          [10, 20, 30, 40],
          [11, 22, 33, 44]
        ]
    print(f"l1 = {l1}")

#function1()

def function2():
    l1 = [[1, 2, 3, 4],
          [10, 20, 30, 40],
          [11, 22, 33, 44]
        ]
    
    for l in l1:
        print(l)

#function2()

def function3():
    l1 = [[1, 2, 3, 4],
          [10, 20, 30, 40],
          [11, 22, 33, 44]
        ]
    
    for l in l1:
        for ele in l:
            print(f" {ele}", end="")
        print("")

#function3()

def function4():
    studList = [[1, "abc", 75.5],
                [2, "xyz", 89.0],
                [3, "mno", 69.2]
            ]
    
    #print(f"studList = {studList}")

    #for stud in studList:
    #    print(stud)

    #for stud in studList:
    #    print(f"rollno = {stud[0]}, name = {stud[1]}, marks = {stud[2]}")

    for rollno, name, marks in studList:
        print(f"rollno = {rollno}, name = {name}, marks = {marks}")

function4()