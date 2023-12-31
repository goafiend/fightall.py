import pygame
pygame.mixer.init()# initialise the pygame

def play(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops=0)

def play_sound(library, event):
    try:
        play(f"sounds/{library}/{library} {event}.wav")
    except:
        try:
            play(f"sounds/Default/Default {event}.wav")
        except:
            print(f"sound not found: {library} {event}")

