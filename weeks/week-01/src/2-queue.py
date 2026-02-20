
class Queue:
    """Array-based Queue implementation using deque"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        first_item = self.items[0]
        if len(self.items)>1:
            self.items = self.items[1:]
        else:
            self.items = []
        
        return first_item
        
        #self.items =  self.items[1:] if len(self.items)>1 else []
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)
    
    def __str__(self):
        return f"Queue({list(self.items)})"
    
# Example usage of Queue 
def simulate_day_at_bank():
    """Simulate a day at the bank with a queue of customers"""
    bank_queue = Queue()
    
    # Customers arrive at the bank
    bank_queue.enqueue("Customer 1")
    bank_queue.enqueue("Customer 2")
    bank_queue.enqueue("Customer 3")
    
    print(bank_queue)  # Queue(['Customer 1', 'Customer 2', 'Customer 3'])
    
    # Serve customers
    while not bank_queue.is_empty():
        current_customer = bank_queue.dequeue()
        print(f"Serving {current_customer}")
    
    print(bank_queue)  # Queue([])

if __name__ == "__main__":
    simulate_day_at_bank()