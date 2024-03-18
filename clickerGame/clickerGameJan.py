import pygame, time
temp, temp1, screen, font, score, running, lastClicked = pygame.init(), pygame.font.init(), pygame.display.set_mode((1280, 720)), pygame.font.SysFont("monospace", 50), 0, True, -1000
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: temp = pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP: lastClicked, score = pygame.time.get_ticks(), score + 1 
    temp, temp1, temp2, temp3, temp4 = screen.fill("yellow"), pygame.draw.circle(screen, (197, 176, 136), (1280/2, 720/2), max(lastClicked - pygame.time.get_ticks() + 200, 0) / 10 + 200), screen.blit(font.render(f"Score: {score}", False, (0, 0, 0)), (100, 100)), pygame.display.flip(), time.sleep(1/60) 