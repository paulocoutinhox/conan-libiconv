# use this to generate xcode project: -c tools.cmake.cmaketoolchain:generator=Xcode
# use this to generate xcode project: cmake -S . -B build/os-system/os-arch/target -G Xcode [...]

# build can be direct with cmake:
#     cmake -S . -B build/os-system/os-arch/target -DCMAKE_TOOLCHAIN_FILE=../conan/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Debug
#     cmake --build build/os-system/os-arch/target

.PHONY: help
help:       ## Show The Help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: clear
clear:      ## Clear Temporary Files.
	rm -rf build
	rm -rf conan/darwin-toolchain/test_package/build
	rm -rf CMakeUserPresets.json

.PHONY: tree
tree:       ## List Files With Tree.
	tree

.PHONY: ios
ios:        ## Setup And Build For iOS.
	cd conan/darwin-toolchain && \
		conan create . nativium/stable

	conan install libiconv/1.17@ -pr:b=default -pr:h=conan/profiles/ios_profile -s:h os=iOS -s:h os.version=11.0 -s:h arch=armv7 --build=missing --update

	@make tree
	@make build
