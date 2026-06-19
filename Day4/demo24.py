def function1():
    studList = [
        {'rollno':1, 'name':"abc", 'marks':75.5},
        {'rollno':2, 'name':"xyz", 'marks':89.0},
        {'rollno':2, 'name':"mno", 'marks':69.2},
    ]   

    print(f"studList = {studList}")
    for stud in studList:
        print(stud)

    for stud in studList:
        print(stud.values())

function1()    