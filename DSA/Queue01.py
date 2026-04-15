class Queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.maxSize=size
        self.front=-1
        self.rear=-1
        
    def enQueue(self,x):
        if self.isFull():
            print('Queue is Full')
        else:
            if self.front==-1:
                self.front=0
            self.rear=self.rear+1
            self.queue[self.rear]=x
            
    def deQueue(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            element=self.queue[self.front]
            if (self.front>=self.rear):
                self.front=-1
                self.rear=-1
            else:
                self.front=self.front+1
            print('Removing front element :',element)
            
    def isEmpty(self):
        return self.front==-1
    
    def isFull(self):
        return (self.rear==self.maxSize-1)
    
    def peek(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            print(self.queue[self.front])
            
    def displayElements(self):
        if self.isEmpty():
            print('Queue is Empty')
        else:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
                
queueObj=Queue(3)
queueObj.enQueue(1)
queueObj.enQueue(2)
queueObj.enQueue(3)

queueObj.displayElements()

print(queueObj.isFull())
queueObj.deQueue()
queueObj.displayElements()
print(queueObj.isEmpty())
queueObj.peek()