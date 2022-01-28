from conans import ConanFile, AutoToolsBuildEnvironment, tools
import re
import os

class MainProject(ConanFile):
    name = "robotkernel_service_helper"
    author = "Robert Burger <robert.burger@dlr.de>"
    license = "GPLv3"
    url = f"https://rmc-github.robotic.dlr.de/robotkernel/{name}"
    description = "robotkernel_service_helper is used to generate service definition from robotkernel yaml definitions."
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = ["*", "!.gitignore"] + ["!%s" % x for x in tools.Git().excluded_files()]
    generators = "pkg_config"

    def build(self):
        pass

    def package(self):
        self.copy("scripts/*")
        self.copy("share/*")
        self.copy("src/*")

    def package_info(self):
        self.cpp_info.bindirs = ['src']
        self.env_info.PATH.append(os.path.join(self.package_folder, 'src'))
        self.env_info.PYTHONPATH.append(os.path.join(self.package_folder, 'src'))
