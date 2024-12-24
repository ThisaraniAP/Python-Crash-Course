import pygame

pygame.init()

class MySounds:
    """Play the game sounds."""
        
    def play_sound(file_name):
        """Play the sound"""
        effect = pygame.mixer.Sound(file_name)
        effect.play()

#MySounds.play_sound('bulletw.wav')
