from Data_Structures.Linked_List import singly_linked_list

sample_sll = singly_linked_list.LinkedList()
sample_sll.traverse_list()
sample_sll.insert_at_start(10)
print("new ll ")
sample_sll.traverse_list()
print("-----------")

sample_sll.insert_at_start(20)
sample_sll.insert_at_start(30)
sample_sll.insert_at_start(40)
print("new ll ")
sample_sll.traverse_list()
print("-----------")
sample_sll.insert_at_end(55)
print("new ll ")
sample_sll.traverse_list()
print("-----------")
sample_sll.insert_before_item(10, 555)
print("new ll ")
sample_sll.traverse_list()
print("-----------")
sample_sll.insert_after_item(10, 111)
print("new ll ")
sample_sll.traverse_list()
print("-----------")

sample_sll.get_count()
sample_sll.search_item(525)

sample_sll.delete_at_start()
print("new ll ")
sample_sll.traverse_list()
print("-----------")

print("new ll ")
sample_sll.traverse_list()
print("-----------")
sample_sll.delete_element_by_value(30)
print("new ll ")
sample_sll.traverse_list()
print("-----------")

sample_sll.reverse_linkedlist()
print("new ll ")
sample_sll.traverse_list()
print("-----------")