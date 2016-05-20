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
	print "\n\n\tUsage: %s host user node" % sys.argv[0]
	sys.exit()

#  Get login password from CLI
userpass = getpass.getpass()

#  Connect to BIG-IP
mgmt = ManagementRoot(sys.argv[1], sys.argv[2], userpass)

#  Get list of pools and pool members
pools = mgmt.tm.ltm.pools.get_collection()

#  Node to search for
node = sys.argv[3]
if len(node) < 8 or node[:8] != '/Common/':
	node = '/Common/'+node
print "Pools using Node "+node

#  Iterate through pool member list (has a list of members per pool referenced) looking for node
for pool in pools:
    member_nodes = [member.fullPath.split(':')[0] for member in pool.members_s.get_collection()]
    if node in member_nodes:
        print "\t"+pool.name
