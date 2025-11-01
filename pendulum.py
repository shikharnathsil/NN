# This is a comment
# draw a double pendulum
import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Double Pendulum")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pendulum properties
pivot_x = WIDTH // 2
pivot_y = 200
length1 = 200  # Length of first pendulum
length2 = 150  # Length of second pendulum
angle1 = math.pi / 4  # Initial angle of first pendulum
angle2 = math.pi / 6  # Initial angle of second pendulum
angular_velocity1 = 0
angular_velocity2 = 0
gravity = 9.81
damping = 1.01

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Physics calculation for first pendulum
    angular_acceleration1 = -(gravity / length1) * math.sin(angle1)
    angular_velocity1 += angular_acceleration1
    angular_velocity1 *= damping
    angle1 += angular_velocity1

    # Calculate first bob position
    bob1_x = pivot_x + length1 * math.sin(angle1)
    bob1_y = pivot_y + length1 * math.cos(angle1)

    # Physics calculation for second pendulum
    angular_acceleration2 = -(gravity / length2) * math.sin(angle2)
    angular_velocity2 += angular_acceleration2
    angular_velocity2 *= damping
    angle2 += angular_velocity2

    # Calculate second bob position (relative to first bob)
    bob2_x = bob1_x + length2 * math.sin(angle2)
    bob2_y = bob1_y + length2 * math.cos(angle2)

    # Draw
    screen.fill(WHITE)
    if angular_velocity1 < -0.5: 
        angular_velocity1 = -.1
    if angular_velocity2 < -0.5:
        angular_velocity2 = -.1  # Reset velocities if too negative
    # Draw pivot point
    pygame.draw.circle(screen, BLACK, (pivot_x, pivot_y), 5)
    
    # Draw first rod and bob
    pygame.draw.line(screen, BLACK, (pivot_x, pivot_y), (bob1_x, bob1_y), 2)
    pygame.draw.circle(screen, BLACK, (int(bob1_x), int(bob1_y)), 15)

    # Draw second rod and bob
    pygame.draw.line(screen, BLACK, (bob1_x, bob1_y), (bob2_x, bob2_y), 2)
    pygame.draw.circle(screen, BLACK, (int(bob2_x), int(bob2_y)), 20)

    pygame.display.flip()
    clock.tick(6)

pygame.quit()
