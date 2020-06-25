import ctypes


class DynamicArray:
    """
    DynamicArray: Class to create a dynamic array

    """

    def __init__(self):
        """
        Create object for class

        Attributes:
            :number_of_element - define initial number of elements in array , default 0
            :capacity - define capacity of array , default 1
            :custom_array - blank array of capacity 1

        """
        self.number_of_element = 0
        self.capacity = 1
        self.custom_array = self.make_array(self.capacity)

    def append(self, new_element: "new element to be appended") -> None:

        """
            Task:
                Appends given element to end of array

            Parameters:
                new_element (obj):New element to be appended.

            Returns:
                None

        """
        if self.capacity == self.number_of_element:
            new_list = self.make_array(self.capacity * 2)
            for i in range(self.capacity):
                new_list[i] = self.custom_array[i]
            self.custom_array = new_list
            self.capacity = self.capacity * 2
        self.custom_array[self.number_of_element] = new_element
        self.number_of_element += 1

    def check_index(self, index: "is this index in array") -> bool:

        """
            Task:
                Check if index is valid

            Parameters:
                index (int) : Index to be checked.

            Returns:
                True if index is valid else False

        """
        if 0 <= index < self.number_of_element:
            return True
        else:
            return False

    def remove(self, index: "remove this index from list") -> "Exception or None":
        """
            Task:
                remove elment from index

            Parameters:
                :index (int) : Index to be removed.

            Returns:
                :exception : if index is invalid
                :none
        """

        if not self.check_index(index):
            return IndexError("Index not Found")
        else:
            if self.number_of_element - 1 == self.capacity / 2:
                new_list = self.make_array(int(self.capacity / 2))
            else:
                new_list = self.make_array(self.capacity)
            for i in range(self.number_of_element):
                if i == index:
                    pass
                else:
                    new_list[i] = self.custom_array[i]
            self.custom_array = new_list
            self.number_of_element -= 1

    def clear(self) -> None:
        """
            Task:
                removes all elments from array

            Parameters:
                :none

            Returns:
                :none
        """
        self.number_of_element = 0
        self.capacity = 1
        self.custom_array = self.make_array(self.capacity)

    def isempty(self) -> bool:
        """
            Task:
                Check if array is empty

            Parameters:
                :none

            Returns:
                :bool : True if array is empty else false
        """

        if self.number_of_element != 0:
            return False
        else:
            return True

    def indexof(self, element: "search this element in array") -> "index or -1":
        """
            Task:
                get index of elements

            Parameters:
                :element (obj) : object to be searched.

            Returns:
                :index : if element found
                :-1 : if element not found
        """

        for i in range(self.number_of_element):
            if self.custom_array[i] == element:
                return i
        return -1

    def contains(self, element: "search this element in array") -> bool:
        """
            Task:
                Checks if array contain given element

            Parameters:
                :element (obj) : element to be searched

            Returns:
                :bool : True if element found in array else false
        """

        return self.indexof(element) != -1

    def size(self) -> "Returns number of element in list":
        """
            Task:
                return size of array

            Parameters:
                :none

            Returns:
                :number_of_elements (int) : number of elements in array
        """

        return self.number_of_element

    def get(self, index: "get this index from array") -> "element or IndexError":
        """
            Task:
                get element at specific index

            Parameters:
                :index (int) : Index to be grabbed.

            Returns:
                :element : if index is valid return element at that index
                :exception : if index is invalid return exception
        """

        if self.check_index(index):
            return self.custom_array[index]
        else:
            return IndexError("Out of Index !!")

    @staticmethod
    def make_array(capacity):
        """
            Task:
                make array of given capacity

            Parameters:
                :capacity (int) : capacity of which array needs to be created

            Returns:
                :array : returns a blank array
        """

        return (ctypes.py_object * capacity)()


arr = DynamicArray()
arr.append(10)
arr.append(12)
print("size", arr.size())
print("get", arr.get(1))
arr.remove(1)
arr.clear()
arr.append(100)
print("size", arr.size())

