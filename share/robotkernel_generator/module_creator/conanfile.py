from conan import ConanFile

class {mod_name}_conanfile(ConanFile):
    python_requires = "conan_template/[~5]@robotkernel/stable"
    python_requires_extend = "conan_template.RobotkernelConanFile"
    name = "module_{mod_name}tty"
    description = ""
    exports_sources = ["*", "!.gitignore"]

    tool_requires = [
        "robotkernel_generator/[~6]@robotkernel/unstable",
    ]

    requires = [
        "robotkernel/[~6]@robotkernel/unstable",
    ]

    def source(self):
        self.run(f"sed 's|PACKAGE_VERSION|{self.version}|' configure.ac.in > configure.ac")

