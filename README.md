[![Build Status](https://travis-ci.org/jgsogo/conan-tgbot.svg)](https://travis-ci.org/jgsogo/conan-tgbot)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/jgsogo/conan-tgbot)](https://ci.appveyor.com/project/jgsogo/conan-tgbot)


# conan-tgbot


[Conan](https://bintray.com/conan-community/conan/tgbot%3Aconan) package for ZLIB library. Thanks to Tim Lebedkov for the MinGW integration help! :)


## Basic setup

    $ conan install tgbot/b35438d@conan/stable
    
## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    tgbot/b35438d@conan/stable

    [options]
    tgbot:shared=True # False
    
    [generators]
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* with all the 
paths and variables that you need to link with your dependencies.
