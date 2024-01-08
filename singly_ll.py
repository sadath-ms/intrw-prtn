class Node:
    
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.next = None

class SinglyLL:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    

    def insert_circular(self, val: int):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # make it circular to pointing back to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        
    
    def circular_ll_insert(self, vals: list):
        for val in vals:
            self.insert_circular(val)
        
    
    def insert(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.tail = new_node
            self.length += 1
    
    def insert_lst(self, vals: list) -> None:
        if not vals:
            return None
        
        self.head = Node(vals[0])
        current = self.head
        len = 1
        for val in vals[1:]:
            new_node = Node(val)
            current.next = new_node
            current = current.next
            self.tail = new_node
            len += 1
        
        self.length += len
    
    def append(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pop(self) -> None:
        pre = self.head
        temp = pre

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre.next
        pre.next = None
        self.length -= 1
        

    def prepend(self, val: int) -> None:
        new_node = Node(val)
        temp = self.head
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.head.next = temp
        self.length += 1


    def pop_first(self) -> None:
        if not self.head:
            return None
        
        current = self.head
        self.head = current.next
        self.length -= 1

    def get(self, index: int) -> int:

        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next 

        return temp

    def set(self, index: int, val: int) -> None:
        temp = self.get(index)
        while temp:
            temp.val = val
            return True
        return False

    def remove(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1

    def reverse(self) -> None:
        """ 1 -> 2 -> 3 -> 4 -> None"""
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    
    def reverse_k_nodes(self, head: object, k: int) -> object:
        current_node = head
        prev_node = None
        next_node = None
        count = 0

        while current_node is not None and count < k:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            count += 1
        
        if next_node is not None:
            head.next = self.reverse_k_nodes(next_node, k)
        
        return prev_node

    
    def merge_two_sorted_list(self, list1: list, list2: list) -> None:
        if not list1 and list2:
            return None
        
        dummy_node = Node()
        current = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        current.next = list1 or list2
        self.head = dummy_node.next
    
    def find_middle_node(self) -> int:
        """
        Apporach : To find the middle node of the linked list, can use
                 two-pointers approach, one moving with twice the speed of
                 other, when fater pointer reached end of the list,the slower
                 pointer will be at the middle.
                 slow-pointer moves one step at a time
                 fast-pointer moves two steps at a time
        Time complexity = 0(n) 
        """
        if not self.head:
            return None
        
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return slow_pointer.val
    
    def has_loop(self) -> bool :
        """
        You can use the "two-pointer" approach to detect a loop in a linked list.
        If there is a loop, the slow and fast pointers will eventually meet. If there is no loop, the fast pointer will reach the end of the list.
        """
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False
    
    def remove_duplicates(self):
        prev = None
        current = self.head
        seen = set()

        while current:
            if current.val in seen:
                prev.next = current.next
            else:
                seen.add(current.val)
                prev = current
            current = current.next

        
    def print_ll(self) -> None:
        print(f'Length of the linked list : {self.length}')
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
            if current == self.head:
                break
    
    def display_ll(self, head: object) -> None:
        print(f'Length of the linked list : {self.length}')
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
    

if __name__ == "__main__":
    ss = SinglyLL()
    lst = [1,2,3,2]
    # ss.circular_ll_insert(lst)
    ss.insert_lst(lst)
    # ss.insert(1)
    # ss.insert(2)
    # ss.insert(4)
    # ss.insert(6)
    print(ss.print_ll())
    # ss.append(3)
    # print(ss.print_ll())
    # ss.pop()
    # print(ss.print_ll())
    # ss.pop_first()
    # print(ss.print_ll())

    # ss.prepend(32)
    # print(ss.print_ll())
    # print(ss.get(32))
    # ss.set(0,1)
    # print(ss.print_ll())
    # ss.remove(2)
    # print(ss.print_ll())

    # ss.reverse()
    # print(ss.print_ll())

    # ss.head = ss.reverse_k_nodes(ss.head,2)
    # print(ss.print_ll())

    # ss1 = SinglyLL()
    # ss1.insert_lst([1,2,7])
    # print(ss1.print_ll())

    # ss1.merge_two_sorted_list(ss.head, ss1.head)
    # print(ss1.print_ll())

    # print(ss.find_middle_node())
    # print(ss.has_loop())
    ss.remove_duplicates()
    print(ss.print_ll())





    











  

