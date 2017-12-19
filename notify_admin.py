from jira import JIRAMonitor
from notifier import LEDNotifier

jiraMonitor = JIRAMonitor()
notifier = LEDNotifier()

while True:
	if jiraMonitor.isJIRAAvailable():
		notifier.standby()
	else:
		notifier.notifyAdmin()