# Part 1: Tutorial

##### Step 1
![Step 1](step1.png)
##### Step 2
![Step 3](step3.png)
##### Step 4
![Step 4p1](step4Part1.png)
![Step 4p2](step4Part2.png)
![Step 4p3](step4Part3.png)
##### Step 5
![Step 5](step5.png)


# Part 2: Makefile

NOTE: Cmake won't upload to github

https://github.com/rcos/CSCI-49XX-OpenSource/tree/master/Modules/BuildSystems/Lab-Example

    Write a Makefile for the code in that directory. Your solutions should:
        Create a static library from the code in the source directory.
        Create a shared library from the code in the source directory.
        Use the file program.c and the libraries you created to make two programs, one linked to the shared library and one linked to the static library. Give them different names. I recommend dynamic_block and static_block
        There are a lot of shortcuts you can use when generating Makefiles. Generally, I approve of using shortcuts so long as the code/Makefile/whatever is understandable. For this exercise, explicitly doing the compiles, links, etc., individually is required both to show us that you understand the material and to practice for the upcoming quiz.
    When you are done, do the same thing using CMake by creating aCMakeLists.txt file.
    Compare the sizes of the shared and static versions of your program using ls -la.
    In your lab report, paste in your Makefile, your CMakefile, the Makefile created by cmake, the relative size of your two executables, and the results of running your program.
