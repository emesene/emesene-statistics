#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from launchpadlib.launchpad import Launchpad
import os

ubuntu_versions = ['lucid', 'maverick', 'natty', 'oneiric']
ubuntu_flavours = ['i386', 'amd64']

cachedir = os.path.expanduser("~/.launchpadlib/")
launchpad = Launchpad.login_anonymously('test', 'production', cachedir)
emeseneppa = launchpad.people['emesene-team'].getPPAByName(name='emesene-stable')
print "Fetching data..."
for ver in ubuntu_versions:
    for flav in ubuntu_flavours:
        desired_dist_and_arch = "https://api.launchpad.net/1.0/ubuntu/" + ver +"/" + flav
        print ">>> " + ver + " " + flav
        for individualemesene in \
            emeseneppa.getPublishedBinaries(distro_arch_series=desired_dist_and_arch):
            print individualemesene.binary_package_name + "\t" + \
              individualemesene.binary_package_version + "\t" + \
              str(individualemesene.getDownloadCount())
print "Done."

