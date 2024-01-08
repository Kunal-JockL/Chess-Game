import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Transparent Rect with Blue Glow")

# Constants
rect_width, rect_height = 200, 150
rect_color = (0, 0, 255, 128)  # Blue color with alpha (R, G, B, A)

# Create a transparent surface for the rectangle
transparent_rect = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
pygame.draw.rect(transparent_rect, rect_color, (0, 0, rect_width, rect_height), border_radius=10)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the transparent rectangle
    screen.blit(transparent_rect, ((width - rect_width) // 2, (height - rect_height) // 2))

    # Draw blue glow in the corners
    pygame.draw.circle(screen, (0, 0, 255, 128), (width // 2, height // 2), 20, 0)
    pygame.draw.circle(screen, (0, 0, 255, 128), (width // 2 + rect_width, height // 2), 20, 0)
    pygame.draw.circle(screen, (0, 0, 255, 128), (width // 2, height // 2 + rect_height), 20, 0)
    pygame.draw.circle(screen, (0, 0, 255, 128), (width // 2 + rect_width, height // 2 + rect_height), 20, 0)

    # Update the display
    pygame.display.flip()
