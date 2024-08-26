import pygame as py
#vars
screenWith = 1280                                                   #Screen Widh
screenHight = 720                                                   #screenHight
screenSCALE = screenWith,screenHight                                #Screen dimensions
DscreenWith = screenWith * (1/3)                                    #Screen With / 3 becouse only 1/3 is the are where the tiles wil be           
gridRect = (DscreenWith,0),(DscreenWith,screenHight)                
blockRect = (DscreenWith/10),(screenHight/20)

TileWidth = 20                                                      #pixel sizes for grid squares
TileHeight = 20                                                    
TileMargin = 4                                                      



py.font.init()
FONT = py.font.SysFont("monospace", 50)