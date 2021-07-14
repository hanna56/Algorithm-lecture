
def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        if pos == 1:
            curr = self.head
            if self.nodeCount == 1:
                self.head = None
                self.tail = None
                
            else:
                self.head = curr.next
                
            self.nodeCount -= 1
            return curr.data            
        
        else:
            prev = self.getAt(pos - 1)
            curr = prev.next
            
            if pos == self.nodeCount:
                prev.next = None
                self.tail = prev
                self.nodeCount -= 1
                return curr.data
            
            else:
                prev.next=curr.next
                self.nodeCount -= 1
                return curr.data
