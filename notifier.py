from gpiozero import LED
import logging
from time import sleep
import threading

class LEDNotifier:

	def __init__(self, ledPort):
		self._led = LED(ledPort)
		self._blink = False
		self._thread = threading.Thread(target=self._cycleLED)
		self._thread.start()

	def notifyAdmin(self):
		self._blink = True

	def standby(self):
		self._blink = False

	@classmethod
	def turnOffLED(cls, ledPort):
		led = LED(ledPort)
		led.off()

	def _cycleLED(self):
		while True:
			self._led.on()
			logging.debug('LED turned on')
			sleep(0.5)
			if self._blink:
				self._led.off()
				logging.debug('LED turned off')
				sleep(0.5)
