#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from launchpadlib.launchpad import Launchpad
import os

cachedir = os.path.expanduser("~/.launchpadlib/")
launchpad = Launchpad.login_anonymously('test', 'production', cachedir)
emeseneppa = launchpad.people['emesene-team'].getPPAByName(name='emesene-stable')
print "Fetching data..."
binaries = emeseneppa.getPublishedBinaries()
printed_binaries = []
for binary in binaries:
    if binary.binary_package_version not in printed_binaries:
        print '{0:{width}}{1:{width2}}{2}'.format(binary.binary_package_name,
            binary.binary_package_version,
            str(binary.getDownloadCount()),
            width=20, width2=30)
        printed_binaries.append(binary.binary_package_version)
print "Done."
