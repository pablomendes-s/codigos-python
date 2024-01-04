def main():
    import pygame
    pygame.init()
    arquivo = "exer021.mp3"
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()
    input (pygame.event.wait)

main()
