#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdl2 import *

# There are more pythonic ways of doing this, by using the sdl2.ext module.

def main():
    SDL_Init(SDL_INIT_VIDEO)

    win = SDL_CreateWindow(b"Hello World!", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 620, 387, SDL_WINDOW_SHOWN)
    ren = SDL_CreateRenderer(win, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
    bmp = SDL_LoadBMP(b"../img/grumpy-cat.bmp")
    tex = SDL_CreateTextureFromSurface(ren, bmp)
    SDL_FreeSurface(bmp)

    for i in range(20):
        SDL_RenderClear(ren)
        SDL_RenderCopy(ren, tex, None, None)
        SDL_RenderPresent(ren)
        SDL_Delay(100)

    SDL_DestroyTexture(tex)
    SDL_DestroyRenderer(ren)
    SDL_DestroyWindow(win)
    SDL_Quit()


if __name__ == "__main__":
    main()
