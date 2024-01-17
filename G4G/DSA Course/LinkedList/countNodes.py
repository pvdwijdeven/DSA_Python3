#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def listFromString(self, slist):
        llist = [int(x) for x in slist.split("->")]
        prev = Node(None)
        head = prev
        for x in llist:
            cur = Node(x)
            prev.next = cur # type: ignore
            prev = cur
        self.head = head.next
        return head.next
    
    def printList(self,head):
        array = []
        curr = head
        while True:
            array.append(curr.data)
            if curr.next == None:
                break
            curr = curr.next
        return array

    def getCount(self, head):
        cur = head
        count = 1
        while cur.next != None:
            count+=1
            cur = cur.next
        return count

    def sumOfElements(self, head):
        cur = head
        total = cur.data
        while cur.next != None:
            cur = cur.next
            total+= cur.data
        return total        

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        print(head_node)
        #code here
        return
    
sol = Solution()

l1 = "1->2->3->4->5"
l2 = "2->4->6->7->5->1->0"

L1 = LinkedList()
L1.listFromString(l1)
print(L1.printList(L1.head))
print(L1.getCount(L1.head))
print(L1.sumOfElements(L1.head))