cmake_minimum_required(VERSION 3.17)
project(shoutjs)

# --- MSVC Flag Fix ---
if(MSVC)
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /NODEFAULTLIB:libcmtd")
endif()

add_library(shoutjs SHARED src/Shout.cpp)

if(WIN32)
    # Define absolute paths explicitly
    set(SHOUT_LIB "E:/Torrentz/libshout-node-master/deps/lib/shout.lib")
    set(INCLUDE_DIRS "E:/Torrentz/libshout-node-master/deps/include")
    
    # Link the specific file path
    set(LIBRARIES ${SHOUT_LIB} ws2_32 wsock32)
else()
    find_package(PkgConfig REQUIRED)
    pkg_check_modules(SHOUT REQUIRED shout)
    set(LIBRARIES ${SHOUT_LIBRARIES})
    set(INCLUDE_DIRS ${SHOUT_INCLUDE_DIRS})
endif()

if(CMAKE_JS_VERSION)
    set(INCLUDE_DIRS ${INCLUDE_DIRS} ${CMAKE_JS_INC} "E:/Torrentz/libshout-node-master/node_modules/nan")
    set(LIBRARIES ${LIBRARIES} ${CMAKE_JS_LIB})
    set_target_properties(shoutjs PROPERTIES PREFIX "" SUFFIX ".node")
else()
    set(INCLUDE_DIRS ${INCLUDE_DIRS} ${NODE_INSTALL_DIR}/include/node "E:/Torrentz/libshout-node-master/node_modules/nan")
endif()

target_include_directories(shoutjs PRIVATE ${INCLUDE_DIRS})
target_link_libraries(shoutjs PRIVATE ${LIBRARIES})