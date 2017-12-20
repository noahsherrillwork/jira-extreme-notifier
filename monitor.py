import logging
import socket
import http.client
import random

class RandomSiteMonitor:

	def isSiteAvailable(self):
		siteCoin = random.randint(0, 1)
		if siteCoin == 0:
			logging.info('Site is down')
			return False
		else:
			logging.info('Site is up')
			return True


class SiteMonitor:

	def isSiteAvailable(self, domain):
		googleAvailable = self._isSiteAvailable('www.google.com')
		siteAvailable = self._isSiteAvailable(domain)

		if siteAvailable or not googleAvailable:
			logging.info('%s is up' % domain)
			self._recordStatus(True)
			return True
		else:
			logging.info('%s is down' % domain)
			self._recordStatus(False)
			return False

	def _isSiteAvailable(self, domain):
		try:
			httpsConnection = http.client.HTTPSConnection(domain, timeout=5)
			httpsConnection.request('GET', '')
			response = httpsConnection.getresponse()
			siteAvailable = (response.status == 200)
			logging.debug(('Response code for %s = %d' % (domain, response.status)))
		except Exception:
			siteAvailable = False
			logging.debug('Exception occurred when attempting to reach %s' % domain)
		finally:
			httpsConnection.close()

		return siteAvailable

	def _recordStatus(self, siteAvailable):
		with open('site_status.txt', 'w') as siteStatusFile:
			if siteAvailable:
				siteStatusFile.write('true')
			else:
				siteStatusFile.write('false')

