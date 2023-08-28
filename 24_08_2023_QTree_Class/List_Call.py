from List_Function import Create
from List_Function import Update
from List_Function import Del
from List_Function import Add

print("******* LIST CREATED METHOD ********")
Created_List = Create.list_create()
print(Created_List)

print("1) Update List")
print("2) Add List")
print("3) Delete List")

user = int(input("Enter your choice: "))

if user == 1:
    for i in range(3):
        index = int(input("Enter your update index: "))
        value = input("Enter your value index: ")
        Updated_List = Update.update(Created_List, index, value)
    print(Updated_List)

elif user == 2:
    print("1) Apend Method")
    print("2) Extend Method")

    user = int(input("Enter your choice: "))
    if user == 1:

        Apend_Value = int(input("Enter Your Append vlaue: "))
        Add_value = Add.f1(Created_List, Apend_Value)
        print(Add_value)
    elif user == 2:

        Apend_Value = [x for x in input("Enter your extend list: ").split(" ")]
        Add_value = Add.f2(Created_List, Apend_Value)
        print(Add_value)

elif user == 3:

    print("1) Pop Method ")
    print("2) Remove Method ")
    print("3) Delete Method")

    user = int(input("Enter your choice: "))

    if user == 1:
        for i in range(int(input("How many item your want pop: "))):
            index1 = int(input("Enter your pop index: "))
            Pop_value = Del.Remove_index_Value(Created_List, index1)
            print(Pop_value)
    elif user == 2:
        Delete_value = int(input("Enter your Delete value: "))
        Remove_item = Del.Remove_Value(Created_List, Delete_value)
        print(Remove_item)
    elif user == 3:
        Delete_value = int(input("Enter your Delete value: "))
        Remove_item = Del.Delete_List(Created_List, Delete_value)
        print(Remove_item)
