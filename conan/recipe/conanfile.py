import os

from conan.tools.apple import is_apple_os
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain
from conan.tools.files import copy

from conan import ConanFile


class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Generators
    generators = "CMakeToolchain", "CMakeDeps"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        generators_dir = os.path.join(
            "build",
            "os-system",
            "os-arch",
            "conan",
            "generators",
        )

        build_dir = os.path.join("build", "os-system", "os-arch", "target")

        self.folders.root = os.path.join("..", "..")
        self.folders.source = "."
        self.folders.build = build_dir
        self.folders.generators = generators_dir

    def export_sources(self):
        pass

    def generate(self):
        # generator
        generator = None

        if is_apple_os(self):
            print("INFO: Using Xcode Generator")
            generator = "Xcode"

        # toolchain
        tc = CMakeToolchain(self, generator=generator)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        pass

    def requirements(self):
        self.requires("sdl/2.24.0")
        self.requires("sdl_image/2.0.5")
        self.requires("libiconv/1.17")

    def configure(self):
        if self.settings.os == "Macos":
            self.options["sdl"].opengles = False
            self.options["sdl"].vulkan = False

        self.options["sdl_image"].bmp = False
        self.options["sdl_image"].gif = False
        self.options["sdl_image"].lbm = False
        self.options["sdl_image"].pcx = False
        self.options["sdl_image"].pnm = False
        self.options["sdl_image"].tga = False
        self.options["sdl_image"].xcf = False
        self.options["sdl_image"].xpm = False
        self.options["sdl_image"].xv = False
        self.options["sdl_image"].with_libjpeg = True
        self.options["sdl_image"].with_libtiff = True
        self.options["sdl_image"].with_libpng = True
        self.options["sdl_image"].with_libwebp = False
