from gpiozero import LED
from time import sleep

class LEDNotifier:

	def notifyAdmin(self):
		led = LED(17)
		led.on()
		sleep(5)
		led.off()

	def standby(self):
		pass
