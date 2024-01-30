from conan import ConanFile, conan_version
from conan.tools.scm import Version
from conan.tools.files import copy
import os

class MainProject(ConanFile):
    package_type = "build-scripts"
    name = "robotkernel_service_helper"
    author = "Robert Burger <robert.burger@dlr.de>"
    license = "GPLv3"
    url = f"https://rmc-github.robotic.dlr.de/robotkernel/{name}"
    description = "robotkernel_service_helper is used to generate service definition from robotkernel yaml definitions."
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = ["*", "!.gitignore"]

    def build(self):
        pass

    def package(self):
        copy(self,"scripts/*", self.source_folder, self.package_folder)
        copy(self,"share/*", self.source_folder, self.package_folder)
        copy(self,"src/*", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.bindirs = ['src']
        if Version(conan_version) < "2.0.0":
            self.env_info.PATH.append(os.path.join(self.package_folder, 'src'))
            self.env_info.PYTHONPATH.append(os.path.join(self.package_folder, 'src'))
        self.runenv_info.append_path("PATH", os.path.join(self.package_folder, 'src'))
        self.runenv_info.append_path("PYTHONPATH", os.path.join(self.package_folder, 'src'))
