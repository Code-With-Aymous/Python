class Array:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)
        return self.array
    
    def delete_from_index(self, index):
        if 0 <= index < len(self.array):
            deleted_value = self.array.pop(index) 
            print(f"Element '{deleted_value}' at index {index} is deleted!")
        else:
            print("Error: Index out of bounds.")
    
    def display(self):
        print(self.array)

    def access(self, index):
        print(self.array[index])

arr = Array()

while True:
    print("************************")
    print("    ARRAY OPERATIONS    ")
    print("************************")
    print("1. Insert Elements\n2. Delete Elements\n3. Display Array\n4. Access Elements\n5. Exit")
    print("************************")

    try:
        choice = int(input("enter your choice (1-5): "))
    except TypeError:
        print("invaild choice, try again!")
        choice = int(input("enter your choice (1-5): "))

    if choice == 1:
        data_type = input("enter data type (int/float/str): ")
        val = input("add element: ")

        if data_type == 'int':
            arr.insert(int(val))
            print(f"{val} is inserted!")

        elif data_type == 'float':
            arr.insert(float(val))
            print(f"{val} is inserted!")

        elif data_type == 'str':
            arr.insert(str(val))
            print(f"{val} is inserted!")


    elif choice == 2:
        _index_ = int(input("delete element from following index: "))
        arr.delete_from_index(_index_)


    elif choice == 3:
        arr.display()

    elif choice == 4:
        index_ = int(input("enter index to access the following element: "))
        arr.access(index_)

    elif choice == 5:
        print("************************")
        break
