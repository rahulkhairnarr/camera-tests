cmake_minimum_required(VERSION 2.6)

MESSAGE(STATUS "Looking for libv4l")
find_library(V4L2_LIBRARY v4l2)
if (V4L2_LIBRARY)
    MESSAGE(STATUS "Looking for libv4l - found")
else (V4L2_LIBRARY)
    MESSAGE(FATAL_ERROR "Looking for libv4l - not found.")
endif (V4L2_LIBRARY)

set(SOURCES v4l2ctrl.c)
set(HEADERS mainWindow.h previewSettings.h v4l2controls.h)
include_directories(${CMAKE_BINARY_DIR}/src)

add_executable(v4l2ctrl v4l2ctrl.c)
target_link_libraries(v4l2ctrl ${V4L2_LIBRARY})

install(TARGETS v4l2ctrl DESTINATION bin)
