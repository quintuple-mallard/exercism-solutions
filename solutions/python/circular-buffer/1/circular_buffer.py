class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.cap = capacity
        self.start = 0
        self.n_elements = 0

    def read(self):
        if not self.n_elements: 
            raise BufferEmptyException("Circular buffer is empty")
        data = self.buffer[self.start % self.cap]
        self.buffer[self.start % self.cap] = None
        self.n_elements -= 1
        self.start += 1
        return data

    def write(self, data):
        if self.n_elements >= self.cap:
            raise BufferFullException("Circular buffer is full")
        self.buffer[(self.start + self.n_elements) % self.cap] = data
        self.n_elements += 1
        
    def overwrite(self, data):
        if self.n_elements < self.cap:
            self.write(data)
        else:
            self.buffer[self.start % self.cap] = data
            self.start += 1

    def clear(self):
        self.buffer = [None] * self.cap
        self.start = 0
        self.n_elements = 0
