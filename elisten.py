import salt.config
import salt.utils.event
import time
import pprint

opts = salt.config.client_config('/etc/salt/master')

event = salt.utils.event.get_event(
        'master',
        sock_dir=opts['sock_dir'],
        transport=opts['transport'],
        opts=opts)

response = event.get_event(wait=30, tag='cookbook/test')
print response
