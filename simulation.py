import pygame
import math
from Territories.territory import Territory
from Drone.drone import Drone
from MazeBuilder.mazeBuilder import *

WIDTH, HEIGHT = 1000, 1000
CELL_SIZE = 5
DRONE_NUMBER = 10
PHEROMONE_INTENSITY = 0
OBSTACLE_COLOR = (63, 60, 60)
DRONE_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Directional Pheromone Walk Simulation")

def draw_territory(territory):
    for i in range(0, len(territory)):
        for j in range(0, len(territory)):
            if territory[i][j].value == 1:
                pygame.draw.rect(WIN, OBSTACLE_COLOR, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)
            else:
                cellQuality = territory[i][j].cellQuality
                if(territory[i][j].visited == "F"):
                    pheromoneColor = WHITE
                else:
                        pheromoneColor = (76, 229, 229)
                pygame.draw.rect(WIN, pheromoneColor, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def draw_drone(pos_x, pos_y):
    pygame.draw.rect(WIN, DRONE_COLOR, pygame.Rect(pos_x*CELL_SIZE,pos_y*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def main():
    run = True
    clock = pygame.time.Clock()
    maze = createMaze(600)
    write_maze_to_txt_file(maze,"maze.txt")
    newTerritory = Territory("maze.txt")
    territory = newTerritory.matrix

    drones = []

    for i in range(1, DRONE_NUMBER + 1):
        if i%4 == 0:
            drone = Drone("north",0,0)
        elif i%3 == 0:
            drone = Drone("south",0,0)
        elif i%2 == 0:
            drone = Drone("east",0,0)
        else:
            drone = Drone("west",0,0)
        drones.append(drone)


    missingCells = True
    counter = 0

    while run:
        clock.tick(60)
        WIN.fill((255,255,255))

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if missingCells:
            counter = counter + 1
            missingCells = False
            for drone in drones:
                drone.move(territory)
                territory = drone.markVisitedCell(territory)
                territory = drone.reduceCellQuality(territory)
            for row in territory:
                for cell in row:
                    cell.reduceQuality()
                    if cell.visited == "F":
                        missingCells = True
        else:
            print("Iterations: ", counter)
        

        
        draw_territory(territory)
        for drone in drones:
            draw_drone(drone.positionX, drone.positionY)
        pygame.display.update()
    
    pygame.quit()

main()