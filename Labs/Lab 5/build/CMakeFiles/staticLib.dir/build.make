# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build"

# Include any dependencies generated for this target.
include CMakeFiles/staticLib.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/staticLib.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/staticLib.dir/flags.make

CMakeFiles/staticLib.dir/block.c.o: CMakeFiles/staticLib.dir/flags.make
CMakeFiles/staticLib.dir/block.c.o: block.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/staticLib.dir/block.c.o"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/staticLib.dir/block.c.o   -c "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build/block.c"

CMakeFiles/staticLib.dir/block.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/staticLib.dir/block.c.i"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build/block.c" > CMakeFiles/staticLib.dir/block.c.i

CMakeFiles/staticLib.dir/block.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/staticLib.dir/block.c.s"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build/block.c" -o CMakeFiles/staticLib.dir/block.c.s

CMakeFiles/staticLib.dir/block.c.o.requires:

.PHONY : CMakeFiles/staticLib.dir/block.c.o.requires

CMakeFiles/staticLib.dir/block.c.o.provides: CMakeFiles/staticLib.dir/block.c.o.requires
	$(MAKE) -f CMakeFiles/staticLib.dir/build.make CMakeFiles/staticLib.dir/block.c.o.provides.build
.PHONY : CMakeFiles/staticLib.dir/block.c.o.provides

CMakeFiles/staticLib.dir/block.c.o.provides.build: CMakeFiles/staticLib.dir/block.c.o


# Object files for target staticLib
staticLib_OBJECTS = \
"CMakeFiles/staticLib.dir/block.c.o"

# External object files for target staticLib
staticLib_EXTERNAL_OBJECTS =

libstaticLib.a: CMakeFiles/staticLib.dir/block.c.o
libstaticLib.a: CMakeFiles/staticLib.dir/build.make
libstaticLib.a: CMakeFiles/staticLib.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library libstaticLib.a"
	$(CMAKE_COMMAND) -P CMakeFiles/staticLib.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/staticLib.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/staticLib.dir/build: libstaticLib.a

.PHONY : CMakeFiles/staticLib.dir/build

CMakeFiles/staticLib.dir/requires: CMakeFiles/staticLib.dir/block.c.o.requires

.PHONY : CMakeFiles/staticLib.dir/requires

CMakeFiles/staticLib.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/staticLib.dir/cmake_clean.cmake
.PHONY : CMakeFiles/staticLib.dir/clean

CMakeFiles/staticLib.dir/depend:
	cd "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5" "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5" "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build" "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build" "/mnt/c/Users/sprecs/Documents/School/19-20 Junior/Open Source Software/Projects/Open-Source-Software/Labs/Lab 5/build/CMakeFiles/staticLib.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/staticLib.dir/depend

