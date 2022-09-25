# Conan Recipe Test: libiconv

This is a test project to check problems with conan recipes.

<p align="center">
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
