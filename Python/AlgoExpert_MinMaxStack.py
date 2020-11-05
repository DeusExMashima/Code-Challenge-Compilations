class MinMaxStack:
	def __init__(self):
		self.storage = []
		self.minimum = None
		self.maximum = None
    def peek(self):
        # Write your code here.
        return self.storage[-1]
    def pop(self):
        # Write your code here.
		if len(self.storage) == 0:
			return self.storage
		popped = self.storage[-1]
		try:
			self.storage = self.storage[:-1]
			if len(self.storage) == 1:
				self.minimum = self.storage[0]
				self.maximum = self.storage[0]
		except IndexError:
			return self.storage
		if popped == self.maximum:
			try:
				self.maximum = max(self.storage)
			except ValueError:
				self.maximum = None
		elif popped == self.minimum:
			try:
				self.minimum = min(self.storage)
			except ValueError:
				self.minimum = None
		return popped
    def push(self, number):
        # Write your code here.
		if len(self.storage) == 0: 
			self.minimum = number
			self.maximum = number
		if number > self.maximum:
			self.maximum = number
		elif number < self.minimum:
			self.minimum = number
        self.storage.append(number)
    def getMin(self):
        # Write your code here.
        return self.minimum
    def getMax(self):
        # Write your code here.
        return self.maximum