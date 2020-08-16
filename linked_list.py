class Element:
    
    def __init__(self, value):
        self.value = value
        self.node_next = None
        self.node_previous= None

class LinkedList:

    def __init__ (self):
        self.head = None
        self.end = None

    def add (self, element):
        if self.head is None:
            self.head = element
            self.end = element
        
        else: 
            self.end.node_next = element
            element.node_previous = self.end
            self.end = element

    def remove (self, element):
        if element: 
            print("Removing ... " + element.value)

            if self.end == element:
                self.end = None
            else:
                element.node_next.node_previous = element.node_previous

            if self.head == element:
                self.head = None
            else:
                element.node_previous.node_next = element.node_next
                


    def __str__(self):
        return self.print_element(self.head)


    def print_element (self, element):
        if element is not None:
            return element.value + ' ' + self.print_element(element.node_next)
        return ''
        
            
    
e1 = Element("aaaaa")
e2 = Element("bbbbb")
e3 = Element("ccccc")
e4 = Element("ddddd")
e5 = Element("fffff")


list = LinkedList()
list.add(e1)
print(list)
list.remove(e1)
print(list)

list.add(e2)
list.add(e3)
list.add(e4)
list.add(e5)

print(list)
list.remove(e4)
print(list)

list.remove(e5)
print(list)

    

        



