cmake_minimum_required(VERSION 2.8)

ENABLE_LANGUAGE(CXX)
ENABLE_LANGUAGE(C)

SET(CMAKE_CXX_FLAGS_RELEASE "-O1")

SET(CMAKE_VERBOSE_MAKEFILE 1)

SET(CMAKE_MODULE_PATH "../cmake_modules/")
INCLUDE("../cmake_modules/common.cmake")

SET(LIBRARY_OUTPUT_PATH ${BINARY_LIB_DIR})

##########################################################
#
#
# Sikuli Img  
#
#
##########################################################
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})

FIND_PACKAGE(OpenCV REQUIRED)
INCLUDE_DIRECTORIES(${OPENCV_INCLUDE_DIR})
LINK_DIRECTORIES(${OpenCV_LIBRARY_DIR})

FIND_LIBRARY(TIFF_LIBS NAMES tiff)
LIST(APPEND OpenCV_LIBS ${TIFF_LIBS})
LINK_DIRECTORIES(${TIFF_LIB_DIR})

FIND_PACKAGE(Tesseract REQUIRED)
INCLUDE_DIRECTORIES(${Tesseract_INCLUDE_DIR})
LINK_DIRECTORIES(${Tesseract_LIBRARY_DIR})

SET(source_list
   TimingBlock.cc
   cvgui.cpp
   finder.cpp
   imgdb.cpp
   pyramid-template-matcher.cpp
   tessocr.cpp
   vision.cpp
   sikuli-debug.cpp
   ${TESSERACT_SOURCES}
) 

add_library(sikuli_img SHARED ${source_list} )
target_link_libraries (sikuli_img ${OpenCV_LIBS} ${Tesseract_LIBRARY})

##########################################################
#
#
# Sikuli Img Python Wrapper 
#
#
##########################################################
FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)
FIND_PACKAGE(Boost COMPONENTS python3)

INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
LINK_LIBRARIES(${Boost_LIBRARIES} ${PYTHON_LIBRARIES}) # Deprecated but so convenient!

PYTHON_ADD_MODULE(pysikuli_img pyfinder.cpp)
TARGET_LINK_LIBRARIES(pysikuli_img sikuli_img)
