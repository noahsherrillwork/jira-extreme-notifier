import logging
from jira import RandomJIRAMonitor
from jira import JIRAMonitor
from notifier import LEDNotifier
from time import sleep

logging.basicConfig(level=logging.DEBUG)

jiraMonitor = JIRAMonitor()
notifier = LEDNotifier()

while True:
	if jiraMonitor.isJIRAAvailable():
		notifier.standby()
	else:
		notifier.notifyAdmin()

	sleep(5)
