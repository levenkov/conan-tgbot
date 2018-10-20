from conans import ConanFile, CMake, tools
from conans import tools


class TgbotConan(ConanFile):
    name = "tgbot"
    version = "0.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Tgbot here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def requirements(self):
        self.requires("OpenSSL/1.1.1@conan/stable")
        self.requires("boost/1.68.0@conan/stable")

    def source(self):
        self.run("git clone https://github.com/reo7sp/tgbot-cpp.git")
        self.run("cd tgbot-cpp && git checkout master")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("tgbot-cpp/CMakeLists.txt", "project(TgBot)",
                              '''project(TgBot)
set(CMAKE_CXX_STANDARD 11)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="tgbot-cpp")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="tgbot-cpp/include")
        self.copy("*TgBot.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["TgBot"]

