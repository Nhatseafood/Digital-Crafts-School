import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))

x = 200
y = 200

pygame.draw.rect(
  screen,
  (255, 0, 0),
  (200, 200, 100, 100),
  0
)
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()