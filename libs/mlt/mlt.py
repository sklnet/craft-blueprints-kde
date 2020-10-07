import info

class subinfo(info.infoclass):
    def setTargets( self ):
        self.description = "Open source multimedia framework"
        self.webpage = "https://www.mltframework.org"
        for ver in ['6.20.0', '6.22.0']:
            self.targets[ ver ] = f"https://github.com/mltframework/mlt/archive/v{ver}.tar.gz"
            self.targetInstSrc[ ver ] = "mlt-" + ver
        self.targetDigests['6.20.0'] = (['ab211e27c06c0688f9cbe2d74dc0623624ef75ea4f94eea915cdc313196be2dd'], CraftHash.HashAlgorithm.SHA256)
        self.svnTargets["master"] = "https://github.com/mltframework/mlt.git"
        self.patchLevel['master'] = 20200924
        self.defaultTarget = "master"

    def setDependencies( self ):
        self.buildDependencies["dev-utils/pkg-config"] = None
        self.runtimeDependencies["libs/libxml2"] = None
        self.runtimeDependencies["libs/ffmpeg"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = None
        self.runtimeDependencies["libs/libfftw"] = None
        self.runtimeDependencies["libs/libsamplerate"] = None
        # self.runtimeDependencies["libs/exiv2"] = None

        if OsUtils.isWin():
            self.runtimeDependencies["libs/dlfcn-win32"] = None
        self.runtimeDependencies["libs/frei0r-plugins"] = None
        self.runtimeDependencies["libs/libsdl2"] = None
        self.runtimeDependencies["libs/vidstab"] = None
        self.runtimeDependencies["libs/rubberband"] = None
        self.runtimeDependencies["libs/opencv/opencv"] = None
        # self.runtimeDependencies["libs/jack"] = None
        # self.runtimeDependencies["libs/ladspa-sdk"] = None
        # self.runtimeDependencies["libs/ladspa-cmt"] = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self, **args ):
        CMakePackageBase.__init__(self)
