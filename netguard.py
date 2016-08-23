#!/usr/bin/env python2.7
#coding=UTF-8

# Copyright (c) 2016 Angelo Moura
#
# NetGUARD is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

import os
from core.NetGUARD import NetGUARD

version = "0.9"

if os.geteuid() != 0:
	sys.exit("[-] Should be run as root.")

if __name__ == "__main__":
	netguard = NetGUARD()
	try:
		netguard.backgroundstart()
	except Exception as e:
		print "[!] Exception caught: {}".format(e)
