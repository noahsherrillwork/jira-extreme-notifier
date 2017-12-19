import random

class JIRAMonitor:

	def isJIRAAvailable(self):
		if random.randint(0, 1) == 0:
			return False
		else:
			return True
