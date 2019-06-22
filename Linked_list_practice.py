'''
Reference: Udacity(Data Structures - Python)
Code Visualization: http://www.pythontutor.com/visualize.html#mode=edit
'''

class Element(object):
    def __init__(self,value):
        self._value = value
        self._next = None

class LinkedList(object):
    def __init__(self,head = None):
        self._head = head

    def append(self, new_element):
        current = self._head
        if self._head:
            while current._next:
                current = current._next
            current._next = new_element

        else:
            self._head = new_element

    def get_position(self,position):
        counter = 1
        current = self._head

        if position < 1:
            return None

        while current and counter <= position:
            if counter == position:
                return current
            current = current._next
            counter += 1

        return None

    def insert(self,new_element, position):
        counter = 1
        current = self._head

        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element._next = current._next
                    current._next = new_element
                current = current._next
                counter += 1
        elif position == 1:
            new_element._next = self._head
            self._head = new_element

    def delete(self,value):
        current = self._head
        previous = None

        while current._value != value and current._next:
            previous = current
            current = current._next

        if current._value == value:
            if previous:
                previous._next = current._next
            else:
                self._head = current._next

# Set up some elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up LinkedList
l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)

# Test get position
print(l1._head._next._next._value)
print(l1.get_position(3)._value)

# Test insert
l1.insert(e4,3)
print(l1.get_position(3)._value)

# Test delete
l1.delete(1)
print(l1.get_position(1)._value)
print(l1.get_position(2)._value)
print(l1.get_position(3)._value)
