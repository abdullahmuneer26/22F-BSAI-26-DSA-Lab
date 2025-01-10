#Define the node class
class Node():
    def __init__(self,value=0,next=None):
        self.value = value 
        self.next = next

def reverse_linked_list(head: Node) -> Node:
    if not head:
        return None  #if the list is empty then return None
    stack = []
    current = head
        
    #push all nodes onto the stack 
    while current:
            stack.append(current) 
            current = current.next 
            
    #pop nodes from the stack and rebuild the list
    new_head = stack.pop()
    current = new_head
    
    while stack:
        current.next = stack.pop()
        current = current.next 
        
    current.next = None  #set the next of the last node to None
    return new_head

    #Helper functiom to print a linkedlist
def display_linked_list(head: Node):
    current = head
    while current:
        print(current.value, end= "->" if current.next else "\n")
        current = current.next
        
#Example usage :
#Creating linkedlist : 1->2->3->4->5

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print("original list: ") 
    display_linked_list(head)        
              
    #Rverse the linkedlist
    reversed_head = []
    reverse_linked_list(head)
    
    print("reversed list: ") 
    display_linked_list(reversed_head)       
               
        