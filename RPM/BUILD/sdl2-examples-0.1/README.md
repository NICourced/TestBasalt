SDL2 Examples
=============

[![sdl2-examples](https://github.com/xyproto/sdl2-examples/actions/workflows/main.yml/badge.svg)](https://github.com/xyproto/sdl2-examples/actions/workflows/main.yml)

"hello world" for SDL2 for various programming languages.

Each sample creates a window, displays an image, then waits two seconds and quits.

All executables should ideally build and run on Linux, macOS, Windows, BSD* and more, but they should at least work on Linux. Most subdirectories contains `README.md` files with more details, and a `Makefile` to have one way of building each sample.

For newer versions of macOS, the programs also appear to need an event loop for the window to show up, so I'm in the process of adding that to each example. The window just isn't shown if there is no event loop.


Requirements
------------

* The SDL 2 library.
* See the README.md file per sample for more information.


Requirements for some of the languages
--------------------------------------

* C compiler that supports C89 (ANSI C), C99 or C11, for the C samples
* A C++ compiler for the C++ sample
* GCC 4.8 or later (or clang++) for the C++11 sample
* Go 1.1 or later and the sdl2 go package (`go get github.com/veandco/go-sdl2/sdl`)
* MRuby with SDL2 added to the configuration file
* Nim 0.9.4 and sdl2 installed with babel
* Python 2 or 3 and PySDL2
* FPC 2.6.4 (or later than 2.4.0, must have Uint8, Uint16 and Uint32)
* Lua (tested with Lua 5.3) and lua-sdl2
* If `tcc` is used for compiling one of the C examples, make sure to add [`-DSDL_DISABLE_IMMINTRIN_H=1`](https://www.mail-archive.com/tinycc-devel@nongnu.org/msg08821.html).


Languages that are not added yet
--------------------------------

- [ ] Ada (but there is an `ada` branch if you wish to give it a spin. Please create a PR if it works on Arch Linux and/or the Linux CI test passes!).
- [ ] C3 (but there is a `c3` branch with "Hello World" in C3).
- [ ] Fortran
- [ ] Scheme

Pull requests are welcome.


General information
----------------------

* License: BSD-3
