import logging
import multiprocessing
import sys
from monitor import RandomSiteMonitor
from monitor import SiteMonitor
from notifier import LEDNotifier
from time import sleep

CHECK_INTERVAL_SECONDS = 30
LED_PORTS = [18, 15]

def _checkServer(domain, ledPort):
	notifier = LEDNotifier(ledPort)
	siteMonitor = SiteMonitor()

	while True:
		if siteMonitor.isSiteAvailable(domain):
			notifier.standby()
		else:
			notifier.notifyAdmin()

		sleep(CHECK_INTERVAL_SECONDS)


def _checkServers():
	try:
		logging.basicConfig(level=logging.INFO)
		domains = sys.argv[1:]
		domainLEDPorts = []
		for (i, domain) in enumerate(domains):
			domainLEDPorts.append((domain, LED_PORTS[i]))
			if len(domainLEDPorts) == len(LED_PORTS):
				break

		with multiprocessing.Pool(len(domains)) as pool:
			pool.starmap(_checkServer, domainLEDPorts)
	except KeyboardInterrupt:
		_shutdown()


def _shutdown():
	for ledPort in LED_PORTS:
		LEDNotifier.turnOffLED(ledPort)


if __name__ == '__main__':
	_checkServers()
