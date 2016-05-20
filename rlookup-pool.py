#!/usr/bin/env python

__author__ = 'buzzsurfr'
__version__ = '0.2'

#  Standard Library
import sys
import re

#  Related Third-Party
import getpass

#  Local Application/Library Specific
from f5.bigip import ManagementRoot

if len(sys.argv) < 4:
	print "\n\n\tUsage: %s host user pool" % sys.argv[0]
	sys.exit()

#  Get login password from CLI
userpass = getpass.getpass()

#  Connect to BIG-IP
mgmt = ManagementRoot(sys.argv[1], sys.argv[2], userpass)

#  Pool to search for
pool = sys.argv[3]
if len(pool) < 8 or pool[:8] != '/Common/':
	pool = '/Common/'+pool
print "Virtual Servers using Pool "+pool

#  Get list of virtual servers
virtual_servers = mgmt.tm.ltm.virtuals.get_collection()

#  Iterate through pool member list (has a list of members per pool referenced) looking for node
for vs in virtual_servers:
	if pool == vs.pool:
		print "\t"+vs.name
