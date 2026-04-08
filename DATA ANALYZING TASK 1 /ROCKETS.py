import pygame
import math
import sys
import random

# --- 1. INITIALIZATION ---
pygame.init()
pygame.mixer.init() # For the background music

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Space Launch Simulation")

# Colors
DARK_SPACE = (15, 15, 30)
MOON_YELLOW = (240, 230, 140)
ROCKET_RED = (220, 60, 60)
ROCKET_BLUE = (60, 120, 220)
WHITE = (255, 255, 255)
FLAME_ORANGE = (255, 140, 0)

# Fonts for our text
my_font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 80)


# --- 2. ROCKET CLASS ---
class MyRocket:
    def __init__(self, name, start_x, start_y, color, speed):
        self.name = name
        self.pos_x = start_x
        self.pos_y = start_y
        self.color = color
        self.speed = speed
        
        self.distance_flown = 0.0
        self.landed = False

    def draw_me(self, surface):
        # Draw the engine flame (only if it's still flying!)
        if not self.landed:
            # Quick trick to make the flame flicker using the game clock
            flicker = pygame.time.get_ticks() % 15
            flame = [
                (self.pos_x - 5, self.pos_y + 15), 
                (self.pos_x + 5, self.pos_y + 15), 
                (self.pos_x, self.pos_y + 30 + flicker)
            ]
            pygame.draw.polygon(surface, FLAME_ORANGE, flame)
        
        # Draw Rocket body (a simple rectangle)
        pygame.draw.rect(surface, self.color, (self.pos_x - 10, self.pos_y - 10, 20, 25))
        
        # Draw Rocket nose (a white triangle on top)
        nose = [
            (self.pos_x - 10, self.pos_y - 10), 
            (self.pos_x + 10, self.pos_y - 10), 
            (self.pos_x, self.pos_y - 25)
        ]
        pygame.draw.polygon(surface, WHITE, nose)
        
        # Put the name tag under the rocket
        text = my_font.render(self.name, True, WHITE)
        surface.blit(text, (self.pos_x - 35, self.pos_y + 45))

    # --- 3. MOVEMENT AND COLLISION LOGIC ---
    def fly_to_moon(self, target_x, target_y, other_ship):
        if self.landed:
            return # Stop moving if we hit the moon
        
        # Math to figure out distance to the moon
        diff_x = target_x - self.pos_x
        diff_y = target_y - self.pos_y
        dist_to_target = math.sqrt(diff_x**2 + diff_y**2)
        
        # Check if we touched the moon (radius is about 40)
        if dist_to_target < 40: 
            self.landed = True
            return
            
        # Get the direction vector
        dir_x = diff_x / dist_to_target
        dir_y = diff_y / dist_to_target
        
        # Collision Avoidance: Check how close we are to the other rocket
        dist_to_other = math.sqrt((self.pos_x - other_ship.pos_x)**2 + (self.pos_y - other_ship.pos_y)**2)
        
        if dist_to_other < 65 and not other_ship.landed:
            # Push away from the other ship slightly
            push_x = self.pos_x - other_ship.pos_x
            push_y = self.pos_y - other_ship.pos_y
            
            dir_x += (push_x / dist_to_other) * 1.5
            dir_y += (push_y / dist_to_other) * 1.5
            
            # Fix the vector length back to normal
            new_len = math.sqrt(dir_x**2 + dir_y**2)
            dir_x /= new_len
            dir_y /= new_len
            
        # Move the rocket
        move_x = dir_x * self.speed
        move_y = dir_y * self.speed
        
        self.pos_x += move_x
        self.pos_y += move_y
        
        # Add to total distance counter
        self.distance_flown += math.sqrt(move_x**2 + move_y**2)


# --- 4. MAIN GAME LOOP ---
def start_simulation():
    clock = pygame.time.Clock()
    
    # Moon position in the top center
    moon_x = WIDTH // 2
    moon_y = 100
    
    # Create the rockets at rough starting positions
    # I gave them slightly different speeds as a bonus feature!
    rocket1 = MyRocket("Ernest", random.randint(200, 300), 500, ROCKET_RED, 2.4)
    rocket2 = MyRocket("Kernest", random.randint(500, 600), 500, ROCKET_BLUE, 2.7)
    
    # Try to play music (will just skip if you don't have the file)
    try:
        pygame.mixer.music.load("space_music.mp3")
        pygame.mixer.music.play(-1) # -1 means loop forever
    except:
        print("Note: 'space_music.mp3' not found. Running without music.")
        
    # The Countdown Phase
    for count in ["3", "2", "1", "LAUNCH!"]:
        screen.fill(DARK_SPACE)
        
        # Draw moon and rockets early so they are visible during countdown
        pygame.draw.circle(screen, MOON_YELLOW, (moon_x, moon_y), 45)
        rocket1.draw_me(screen)
        rocket2.draw_me(screen)
        
        # Show the countdown text
        msg = big_font.render(count, True, WHITE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
        
        pygame.display.flip()
        pygame.time.delay(1000) # Wait exactly 1 second
        
    # The Action Phase
    keep_playing = True
    while keep_playing:
        
        # --- 5. EVENT HANDLING ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
                
        # --- 6. RENDERING & UPDATING ---
        screen.fill(DARK_SPACE)
        pygame.draw.circle(screen, MOON_YELLOW, (moon_x, moon_y), 45) # The Moon
        
        # Move them
        rocket1.fly_to_moon(moon_x, moon_y, rocket2)
        rocket2.fly_to_moon(moon_x, moon_y, rocket1)
        
        # Draw them
        rocket1.draw_me(screen)
        rocket2.draw_me(screen)
        
        # --- UI / DISPLAY UPDATES ---
        # Show real-time distance
        info1 = my_font.render(f"Ernest Dist: {int(rocket1.distance_flown)}", True, ROCKET_RED)
        info2 = my_font.render(f"Kernest Dist: {int(rocket2.distance_flown)}", True, ROCKET_BLUE)
        screen.blit(info1, (20, 20))
        screen.blit(info2, (20, 60))
        
        # Notifications when they hit the moon
        if rocket1.landed:
            msg1 = my_font.render(f"Ernest reached the moon! (Total Dist: {int(rocket1.distance_flown)})", True, ROCKET_RED)
            screen.blit(msg1, (20, HEIGHT - 90))
            
        if rocket2.landed:
            msg2 = my_font.render(f"Kernest reached the moon! (Total Dist: {int(rocket2.distance_flown)})", True, ROCKET_BLUE)
            screen.blit(msg2, (20, HEIGHT - 40))
            
        pygame.display.flip()
        clock.tick(60) # Keep game at 60 Frames Per Second
        
    pygame.quit()
    sys.exit()

# Run the program
if __name__ == "__main__":
    start_simulation()