import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

text_surf = test_font.render('My game', False, (64,64,64))
text_rect = text_surf.get_rect(center= (400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom =(600,300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity =-20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom ==300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen,'#c0e8ec',text_rect,)
        pygame.draw.rect(screen,'#c0e8ec',text_rect,10)
        screen.blit(text_surf,text_rect)

        snail_rect.left -= 3
        if snail_rect.right < 0: snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)


        #Player

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >=300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # colission

        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        pass

    pygame.display.update()
    clock.tick(60)