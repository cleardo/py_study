import jenkins

from pprint import pprint

server = jenkins.Jenkins('http://192.168.230.91:8080', username='admin', password='admin')

version = server.get_version()

print version

jobs = server.get_jobs()

pprint(jobs)
