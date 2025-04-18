import time
import random
import pygame  # You might need to install this: pip install pygame

def play_sound(sound_file):
    """Plays the specified sound file."""
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    while pygame.mixer.get_busy():
        time.sleep(0.1)  # Keep the script alive while the sound plays
    pygame.mixer.quit()

if __name__ == "__main__":
    sound_file = "beepSwim.mp4"  # Replace with the path to your sound file

    try:
        while True:
            # Generate a random delay between 5 and 15 seconds (you can adjust the upper limit)
            delay = random.uniform(5, 15)
            print(f"Waiting for {delay:.2f} seconds...")
            time.sleep(delay)
            print("Playing sound...")
            play_sound(sound_file)
            print("Sound played.")

    except KeyboardInterrupt:
        print("\nScript stopped by user.")