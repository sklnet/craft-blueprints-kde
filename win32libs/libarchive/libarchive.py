import info


class subinfo(info.infoclass):
    def setTargets(self):
        for v in ['2.7.0', '2.8.4', '3.3.1']:
            self.targets[v] = 'https://github.com/libarchive/libarchive/archive/v' + v + '.tar.gz'
            self.targetInstSrc[v] = 'libarchive-' + v
            self.patchLevel[v] = 2
        self.targetDigests['2.8.4'] = 'b9cc3bbd20bd71f996be9ec738f19fda8653f7af'
        self.patchToApply['2.8.4'] = ("libarchive-2.8.4-20101205.diff", 1)
        self.patchToApply['3.3.1'] = ("libarchive-no-fatal-warnings-in-debug-mode.diff", 1)
        self.description = "C library and command-line tools for reading and writing tar, cpio, zip, ISO, and other archive formats"
        self.defaultTarget = '3.3.1'

    def setDependencies(self):
        self.buildDependencies["win32libs/liblzma"] = "default"
        self.buildDependencies["win32libs/libbzip2"] = "default"
        self.buildDependencies["win32libs/zlib"] = "default"
        self.buildDependencies["win32libs/openssl"] = "default"
        self.buildDependencies["win32libs/libxml2"] = "default"
        self.runtimeDependencies["virtual/base"] = "default"
        #        self.runtimeDependencies["win32libs/expat"] = "default"

from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
