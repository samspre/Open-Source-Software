# Part 1: Tutorial

    For Steps 1 and 2, include the modified code, tutorial.cxx, the CMakeLists.txt along with a screen shot of running the Tutorial code without input, with 10 and with 4294967296.
    For Step 3, include CMakeLists.txt and MathFunctions/CMakeLists.txt (most of your changes for Step3 will be in MathFunctions/CMakeLists.txt) along with a screen shot of running the Tutorial code without input, with 10 and with 4294967296
    For Step 4, include CMakeLists.txt and MathFunctions/CMakeLists.txt along with the output of running ctest -VV.
    For Step 5, include CMakeLists.txt and MathFunctions/CMakeLists.txt along with a screen shot of running the Tutorial code without input, with 10 and with 4294967296.


# Part 2: Makefile

https://github.com/rcos/CSCI-49XX-OpenSource/tree/master/Modules/BuildSystems/Lab-Example

    Write a Makefile for the code in that directory. Your solutions should:
        Create a static library from the code in the source directory.
        Create a shared library from the code in the source directory.
        Use the file program.c and the libraries you created to make two programs, one linked to the shared library and one linked to the static library. Give them different names. I recommend dynamic_block and static_block
        There are a lot of shortcuts you can use when generating Makefiles. Generally, I approve of using shortcuts so long as the code/Makefile/whatever is understandable. For this exercise, explicitly doing the compiles, links, etc., individually is required both to show us that you understand the material and to practice for the upcoming quiz.
    When you are done, do the same thing using CMake by creating aCMakeLists.txt file.
    Compare the sizes of the shared and static versions of your program using ls -la.
    In your lab report, paste in your Makefile, your CMakefile, the Makefile created by cmake, the relative size of your two executables, and the results of running your program.
