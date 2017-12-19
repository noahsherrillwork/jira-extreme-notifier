import logging
import socket
import http.client
import random

class RandomJIRAMonitor:

	def isJIRAAvailable(self):
		jiraCoin = random.randint(0, 1)
		if jiraCoin == 0:
			logging.info('JIRA is down')
			return False
		else:
			logging.info('JIRA is up')
			return True


class JIRAMonitor:

	def isJIRAAvailable(self):
		googleAvailable = self._isSiteAvailable('www.google.com')
		jiraAvailable = self._isSiteAvailable('issues.liferay.com')

		if jiraAvailable or not googleAvailable:
			logging.info('JIRA is up')
			self._recordStatus(True)
			return True
		else:
			logging.info('JIRA is down')
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

	def _recordStatus(self, jiraAvailable):
		with open('jira_status.txt', 'w') as jiraStatusFile:
			if jiraAvailable:
				jiraStatusFile.write('true')
			else:
				jiraStatusFile.write('false')

