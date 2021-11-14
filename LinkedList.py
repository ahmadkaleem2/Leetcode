class LinkedList:

  Head = None

  class Node:

    val = None
    node = None


  def create(self,val) -> None:

    if self.Head is None:
      newNode = self.Node()
      
      newNode.val = val
      self.Head = newNode

      return
    
    newNode = self.Node()
    newNode.val = val
    
    newNode.node = self.Head

    self.Head = newNode
    


  def add_to_tail(self,val)-> None:
    if self.Head is None:
      raise Exception("Linked list is empty, Head and Tail don't exist, can't add to tail")

    temp_head = self.Head

    prev = None

    while temp_head != None:
      prev = temp_head
      temp_head = temp_head.node
    newNode = self.Node()
    newNode.val = val
    prev.node = newNode




  def print_all(self) -> None:

    temp_head = self.Head

    while temp_head != None:

      print(temp_head.val)

      temp_head = temp_head.node

  def reverse_linkedlist(self)-> None:


    #keep prev node address
    prev = None

    # Head
    current = self.Head

    # if don't reach end keep iterating
    while current != None:
      
      # get the next address
      next = current.node

      
      # set the next address to prev address
      current.node = prev

      # set prev address to current address
      prev = current

      # get the next address from current to iterate
      current = next

    # reverse linked list Head
    self.Head = prev


  def delete_link(self,val):


    

    prev = None

    temp_head = self.Head

    if self.Head == None:
      return

    if self.Head.val == val:
      self.Head = self.Head.node
      return


    while temp_head != None:

      if temp_head.val == val:
        prev.node = temp_head.node


      prev = temp_head
      
      temp_head = temp_head.node

  def isPalindrome(self) -> bool:
    stack = []
    head = self.Head
    while (head):
              
      stack.append(head.val)
              
      head = head.node
          
          
    return stack[::] == stack[::-1]

  def hasCycle(self, head: Optional[ListNode]) -> bool:
        
    objects = []
        
        
    while head != None:
            
      if head in objects:
        return True
            
      objects.append(head)
      head = head.next
    return False
