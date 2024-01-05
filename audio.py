import pygame
pygame.mixer.init()# initialise the pygame

pygame.mixer.set_num_channels(5)

def play(sound):
    sound.play()


def play_sound(library, event):
    try:
        sound = pygame.mixer.Sound(f"sounds/{library}/{library} {event}.wav")
        play(sound)
    except:
        try:
            sound = pygame.mixer.Sound(f"sounds/Default/Default {event}.wav")
            play(sound)
        except:
            print(f"sound not found: {library} {event}")
