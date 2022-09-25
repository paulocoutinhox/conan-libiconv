# Conan Recipe Test: libiconv

This is a test project to check problems with conan recipes.

<p align="left">
    <a href="https://github.com/paulocoutinhox/conan-libiconv/actions/workflows/ios.yml"><img src="https://github.com/paulocoutinhox/conan-libiconv/actions/workflows/ios.yml/badge.svg"></a>    
</p>

## How to build for iOS

Execute on terminal:

`make ios`

## Tree

This is the project structure when run `make tree`:

```
.
├── Makefile
├── README.md
├── conan
│   ├── darwin-toolchain
│   │   ├── README.md
│   │   ├── build.py
│   │   ├── conanfile.py
│   │   └── test_package
│   │       ├── CMakeLists.txt
│   │       ├── conanfile.py
│   │       └── hello.c
│   └── profiles
│       └── ios_profile
└── requirements.txt

4 directories, 10 files
```

## Error

Link:

https://github.com/paulocoutinhox/conan-libiconv/actions/runs/3120666891/jobs/5061418134#step:11:544

Log:

```
libiconv/1.17: Applying build-requirement: darwin-toolchain/1.0.0@nativium/stable
libiconv/1.17: Configuring sources in /Users/runner/.conan/data/libiconv/1.17/_/_/source

libiconv/1.17: Copying sources to build folder
libiconv/1.17: Building your package in /Users/runner/.conan/data/libiconv/1.17/_/_/build/752ce28eb3c3549ba590898f66aebf396a34e2c1
libiconv/1.17: Generator txt created conanbuildinfo.txt
libiconv/1.17: Aggregating env generators
libiconv/1.17: Calling build()
libiconv/1.17: Calling:
 > ./configure '--enable-static' '--disable-shared' '--prefix=/Users/runner/.conan/data/libiconv/1.17/_/_/package/752ce28eb3c3549ba590898f66aebf396a34e2c1' '--bindir=${prefix}/bin' '--sbindir=${prefix}/bin' '--libexecdir=${prefix}/bin' '--libdir=${prefix}/lib' '--includedir=${prefix}/include' '--oldincludedir=${prefix}/include' '--datarootdir=${prefix}/share' --build=x86_64-apple-darwin --host=arm-apple-ios
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for arm-apple-ios-strip... no
checking for strip... strip
configure: WARNING: using cross tools not prefixed with host triplet
checking for a race-free mkdir -p... ./build-aux/install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make sets $(MAKE)... (cached) yes
checking for arm-apple-ios-gcc... no
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether gcc accepts -g... yes
checking for gcc option to enable C11 features... none needed
rm: conftest.dSYM: is a directory
checking whether gcc understands -c and -o together... yes
checking whether the compiler is clang... yes
checking for compiler option needed when checking for declarations... -Werror=implicit-function-declaration
checking whether make supports the include directive... yes (GNU style)
checking dependency style of gcc... none
checking how to run the C preprocessor... /lib/cpp
configure: error: in `/Users/runner/.conan/data/libiconv/1.17/_/_/build/752ce28eb3c3549ba590898f66aebf396a34e2c1/source_subfolder':
configure: error: C preprocessor "/lib/cpp" fails sanity check
See `config.log' for more details
libiconv/1.17: 
WARN: sdl_image/2.0.5: requirement sdl/2.0.20 overridden by hello/0.1 to sdl/2.24.0 
libiconv/1.17: ERROR: Package '752ce28eb3c3549ba590898f66aebf396a34e2c1' build failed
libiconv/1.17: WARN: Build folder /Users/runner/.conan/data/libiconv/1.17/_/_/build/752ce28eb3c3549ba590898f66aebf396a34e2c1
ERROR: libiconv/1.17: Error in build() method, line 140
	autotools = self._configure_autotools()
while calling '_configure_autotools', line 126
	autotools.configure(args=configure_args, host=host, build=build)
	ConanException: Error 1 while executing ./configure '--enable-static' '--disable-shared' '--prefix=/Users/runner/.conan/data/libiconv/1.17/_/_/package/752ce28eb3c3549ba590898f66aebf396a34e2c1' '--bindir=${prefix}/bin' '--sbindir=${prefix}/bin' '--libexecdir=${prefix}/bin' '--libdir=${prefix}/lib' '--includedir=${prefix}/include' '--oldincludedir=${prefix}/include' '--datarootdir=${prefix}/share' --build=x86_64-apple-darwin --host=arm-apple-ios
make: *** [ios] Error 1
```
