cmake_minimum_required(VERSION 3.3)
project(block)

add_library(staticLib block.c)
add_library(sharedLib SHARED block.c)

add_executable(static_block program.c)
add_executable(dynamic_block program.c)

target_link_libraries(static_block staticLib)
target_link_libraries(dynamic_block sharedLib)
