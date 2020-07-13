###############################################################################
# file: QueueLtk.py                                                           #
# author: Pedro Adolfo de Souza Junior                                        #
# brief: This file include the source code to implement a simple Queue to     #
#        save the frames captured by Face Recognition module                  #
###############################################################################

class QueueLtk:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
