import pygame
from time import sleep
import random

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 800
FPS = 120

global display, arr
arr =[]
arr += [random.randint(1, 700) for _ in range(200)]

def bubbleSort():
    """Sorts a list using bubble sort algorithm."""
    global arr
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                drawRects()
                #sleep(0.)  
                print(f"Current array: {arr}")

def mergeSortVisual(arr):
    def merge(arr, l, m, r):
        left = arr[l:m]
        right = arr[m:r]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            drawRects()
            yield arr
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            drawRects()
            yield arr
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            drawRects()
            yield arr
    def mergeSortGen(arr, l, r):
        if r - l > 1:
            m = (l + r) // 2
            yield from mergeSortGen(arr, l, m)
            yield from mergeSortGen(arr, m, r)
            yield from merge(arr, l, m, r)
    return mergeSortGen(arr, 0, len(arr))
    

def drawRects():
    global display, arr
    rectWith = (WINDOW_WIDTH - 100) / arr.__len__()
    X = 50 - rectWith
    display.fill((0, 0, 0))
    for rectHight in arr:
        X += rectWith
        rect = pygame.Rect((X, WINDOW_HEIGHT - 100 - rectHight), (rectWith, rectHight))
        pygame.draw.rect(display, "Green", rect)
    pygame.display.flip()





def main():
    """Main program entry point."""
    global display, arr
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    display.fill((0, 0, 0))
    sort_gen = mergeSortVisual(arr)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        try:
            next(sort_gen)
        except StopIteration:
            pass
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()


