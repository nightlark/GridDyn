# LLNS Copyright Start
# Copyright (c) 2014-2018, Lawrence Livermore National Security
# This work was performed under the auspices of the U.S. Department
# of Energy by Lawrence Livermore National Laboratory in part under
# Contract W-7405-Eng-48 and in part under Contract DE-AC52-07NA27344.
# Produced at the Lawrence Livermore National Laboratory.
# All rights reserved.
# For details, see the LICENSE file.
# LLNS Copyright End

set(shared_library_test_headers)

set(shared_library_test_sources shared_library_tests.cpp basic_tests.cpp)

add_executable(
    shared_library_tests ${shared_library_test_sources}
    ${shared_library_test_headers}
)

target_include_directories(
    shared_library_tests SYSTEM
    PUBLIC ${Boost_INCLUDE_DIR}
)
target_include_directories(
    shared_library_tests
    PUBLIC ${PROJECT_SOURCE_DIR}/src/griddyn_shared
)

set_target_properties(shared_library_tests PROPERTIES FOLDER tests)

file(TO_NATIVE_PATH ${CMAKE_SOURCE_DIR}/test/test_files test_dir)

if(WIN32)
    # there are 4 slashes because cmake escapes "\" and regex escapes it so I need 4
    # this will probably fail on macs yet

    string(
        REGEX
        REPLACE
            "\\\\"
            "\\\\\\\\"
            test_dir
            ${test_dir}
    )
endif(WIN32)
# message(${test_dir})

target_compile_definitions(
    shared_library_tests PRIVATE -DGRIDDYN_TEST_DIRECTORY="${test_dir}"
)

target_link_libraries(
    shared_library_tests
    PUBLIC griddyn_shared_lib ${Boost_LIBRARIES_test}
)

if(VERSION_OPTION)
    if(MSVC)
        target_compile_options(shared_library_tests PUBLIC ${VERSION_OPTION})
    else()
        target_compile_options(
            shared_library_tests
            PUBLIC $<$<COMPILE_LANGUAGE:CXX>:${VERSION_OPTION}>
        )
    endif(MSVC)
endif(VERSION_OPTION)

target_link_libraries(shared_library_tests PUBLIC ${Boost_LIBRARIES_core})

add_test(NAME shared_library_tests COMMAND shared_library_tests)

set_target_properties(testExtra PROPERTIES FOLDER tests)

foreach(keyfile IN LISTS KEY_LIBRARY_FILES)
    add_custom_command(
        TARGET
        shared_library_tests
        POST_BUILD # Adds a post-build event to api tests
        COMMAND
            ${CMAKE_COMMAND}
            -E
            copy_if_different # which executes "cmake - E copy_if_different..."
            "${keyfile}" # <--this is in-file
            "$<TARGET_FILE_DIR:shared_library_tests>/"
    ) # <--this is out-file path
endforeach(keyfile)

add_custom_command(
    TARGET
    shared_library_tests
    POST_BUILD # Adds a post-build event to api tests
    COMMAND
        ${CMAKE_COMMAND}
        -E
        copy_if_different # which executes "cmake - E copy_if_different..."
        "$<TARGET_FILE:griddyn_shared_lib>" # <--this is in-file
        "$<TARGET_FILE_DIR:shared_library_tests>/"
) # <--this is out-file path
