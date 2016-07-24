##########################################################
#
#
# Sikuli Img Python Wrapper 
#
#
##########################################################
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})
LINK_DIRECTORIES("${CMAKE_CURRENT_SOURCE_DIR}/..")

FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)
FIND_PACKAGE(Boost COMPONENTS python3)

INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
LINK_LIBRARIES(${Boost_LIBRARIES} ${PYTHON_LIBRARIES}) # Deprecated but so convenient!

PYTHON_ADD_MODULE(pysikuli_img pyfinder.cpp)
TARGET_LINK_LIBRARIES(pysikuli_img sikuli_img)
