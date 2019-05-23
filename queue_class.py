# Creating a queue class to insert and 
# remove an element

class Queue:
    def __init__(self):
        self.queue = []

    def add_elem(self, elem):
        return self.queue.insert(0, elem)

    def rem_elem(self):
        return self.queue.pop()

    def disp_queue(self):
        print(self.queue)

    def clear_queue(self):
        self.queue.clear()

q1 = Queue()
q1.add_elem(1)
q1.add_elem(2)
q1.add_elem(3)

q1.disp_queue()
q1.rem_elem()
q1.disp_queue()
