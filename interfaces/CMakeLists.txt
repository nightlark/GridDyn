cmake_minimum_required(VERSION 3.5)

if (NOT DISABLE_SWIG)
	FIND_PACKAGE(SWIG REQUIRED 3.0)
	INCLUDE(${SWIG_USE_FILE})
endif()

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})
INCLUDE_DIRECTORIES("${PROJECT_SOURCE_DIR}/src/griddyn_shared")
INCLUDE_DIRECTORIES("${CMAKE_INSTALL_PREFIX}/include")
INCLUDE_DIRECTORIES("${CMAKE_INSTALL_PREFIX}/include/griddyn/griddyn_shared")
link_directories(${CMAKE_INSTALL_PREFIX}/lib)
message("libraries = ${CMAKE_INSTALL_PREFIX}/lib")

if(WITH_SELFCONTAINED OR (WIN32 AND NOT CYGWIN))
    set(DEF_LIB_PREFIX griddyn)
    set(DEF_BIN_PREFIX griddyn)
    set(DEF_CMAKE_PREFIX griddyn/cmake)
    set(DEF_PYTHON_PREFIX) # Note: Files installed in a griddyn subdirectory
    set(DEF_MATLAB_PREFIX griddyn)
    set(DEF_INCLUDE_PREFIX griddyn/include)
else()
    set(DEF_LIB_PREFIX lib)
    set(DEF_BIN_PREFIX bin)
    set(DEF_CMAKE_PREFIX lib/cmake/griddyn)
    set(DEF_PYTHON_PREFIX python)
    set(DEF_MATLAB_PREFIX matlab)
    set(DEF_INCLUDE_PREFIX include)
endif()

# Installation directories are cache entries that can be modified
set(LIB_PREFIX ${DEF_LIB_PREFIX} CACHE PATH "Installation directory for libraries")
set(BIN_PREFIX ${DEF_BIN_PREFIX} CACHE PATH "Installation directory for executables")
set(INCLUDE_PREFIX ${DEF_INCLUDE_PREFIX} CACHE PATH "Installation directory for header files")
set(CMAKE_PREFIX ${DEF_CMAKE_PREFIX} CACHE PATH "Installation directory for CMake files")
set(PYTHON_PREFIX ${DEF_PYTHON_PREFIX} CACHE PATH "Installation directory for Python files")
set(MATLAB_PREFIX ${DEF_MATLAB_PREFIX} CACHE PATH "Installation directory for MATLAB/Octave files")

set_property(SOURCE griddyn.i PROPERTY CPLUSPLUS ON)
set_property(SOURCE griddyn.i  PROPERTY SWIG_MODULE_NAME griddyn)

if(BUILD_PYTHON_INTERFACE)
       add_subdirectory(python)
endif()
if(BUILD_MATLAB_INTERFACE)
       add_subdirectory(matlab)
endif()

if(BUILD_OCTAVE_INTERFACE)
       add_subdirectory(octave)
endif()


if(BUILD_JAVA_INTERFACE)
       add_subdirectory(java)
endif()

