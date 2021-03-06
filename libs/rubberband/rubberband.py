import info

from Package.MSBuildPackageBase import *
from Package.AutoToolsPackageBase import *

class subinfo(info.infoclass):
    def registerOptions(self):
        self.parent.package.categoryInfo.platforms = CraftCore.compiler.Platforms.NotMacOS

    def setTargets( self ):
        for ver in ["1.8.2"]:
            self.targets[ ver] = f"https://github.com/breakfastquay/rubberband/archive/v{ver}.tar.gz"
            self.targetInstSrc[ ver ] = f"rubberband-{ver}"
        self.targetDigests["1.8.2"] = (['0bb058710b476712480cf6b3e1c1178c6237e9e8e3c98092f00e31632a011d15'], CraftHash.HashAlgorithm.SHA256)
        self.patchToApply['1.8.2'] = [("no-jni-to-install.patch", 0)]
        if CraftCore.compiler.isWindows or CraftCore.compiler.isMacOS:
            self.patchToApply['master'] = [("fftw3-linking.patch", 0), ("fftw-config-1.patch", 0), ("fftw-config-2.patch", 0)]
        self.svnTargets['master'] = "https://github.com/breakfastquay/rubberband.git"

        self.description = "An audio time-stretching and pitch-shifting library and utility program"
        self.webpage = "http://breakfastquay.com/rubberband/"
        self.defaultTarget = "master"

    def setDependencies( self ):
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/libfftw"] = None
        self.runtimeDependencies["libs/libsamplerate"] = None
        self.runtimeDependencies["libs/libsndfile"] = None


class PackageAutoTools(AutoToolsPackageBase):
    def __init__(self, **args):
        AutoToolsPackageBase.__init__(self)
        self.subinfo.options.configure.args += " --disable-programs  --disable-vamp --disable-ladspa"

class PackageMSVC(MSBuildPackageBase):
    def __init__(self, **args):
        MSBuildPackageBase.__init__(self)
        self.subinfo.options.configure.projectFile = os.path.join(self.sourceDir(), "rubberband.sln")
        self.msbuildTargets = ["rubberband-dll"]


if CraftCore.compiler.isGCCLike():
    class Package(PackageAutoTools):
        def __init__(self):
            PackageAutoTools.__init__(self)
            self.subinfo.options.useShadowBuild = False

else:
    class Package(PackageMSVC):
        def __init__(self):
            PackageMSVC.__init__(self)
