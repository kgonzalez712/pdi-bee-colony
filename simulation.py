import pygame
import math
import sys
from Territories.territory import Territory
from Drone.drone import Drone
from Drone.bee import BeeDrone
from Drone.ant import AntDrone
from MazeBuilder.mazeBuilder import *
import datetime


WIDTH, HEIGHT = 1100, 1100

CELL_SIZE = 5
PHEROMONE_INTENSITY = 500
OBSTACLE_COLOR = (63, 60, 60)
DRONE_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Directional Pheromone Walk Simulation")

def drawTerritory(territory, algorithm):
    for i in range(0, len(territory)):
        for j in range(0, len(territory)):
            if territory[i][j].value == 1:
                pygame.draw.rect(WIN, OBSTACLE_COLOR, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)
            else:
                cellQuality = territory[i][j].cellQuality
                if(territory[i][j].visited == "F"):
                    pheromoneColor = WHITE
                else:
                    if algorithm == 1:
                        if cellQuality in range(337, 501):
                            pheromoneColor = (229, 66 + (500 - cellQuality), 66)
                        elif cellQuality in range(174, 337):
                            pheromoneColor = (cellQuality - 109, 229, 66)
                        elif cellQuality in range(11, 174):
                            pheromoneColor = (66, 229, 66 + (173 - cellQuality))
                        elif cellQuality in range (1, 11):
                            pheromoneColor = (66 + (10 - cellQuality), 229, 229)
                        else:
                            pheromoneColor = (76, 229, 229)
                    else:
                        pheromoneColor = (76, 229, 229)
                pygame.draw.rect(WIN, pheromoneColor, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def drawDrone(pos_x, pos_y):
    pygame.draw.rect(WIN, DRONE_COLOR, pygame.Rect(pos_x*CELL_SIZE,pos_y*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def askForParameters():
    """Prompts the user to enter values for the simulation parameters.

    Returns:
        A tuple containing the following values:
            * `drone_number`: The number of drones to simulate.
            * `algorithm`: The algorithm to use.
    """
    size = int(input("Enter the size of the map (150 / 300 / 600): "))
    while size != 150 and size != 300 and size != 600:
        print("Invalid size. Please choose from 150, 300 or 600.")
        size = int(input("Enter the size of the map (150 / 300 / 600): "))

    mapType = int(input("Do you want the map to ve completly random? 1 - YES  2 - NO :  "))
    while mapType != 1 and mapType != 2:
        print("Invalid map type number. Please enter 1 for YES or 2 for NO.")
        mapType = int(input("Do you want the map to ve completly random? 1 - YES  2 - NO :  "))

    droneNumber = int(input("Enter the number of drones (values should be from 1 to 100): "))
    while droneNumber < 1 or droneNumber > 100:
        print("Invalid number of drones. Please enter a value between 1 and 100.")
        droneNumber = int(input("Enter the number of drones (values should be from 1 to 100): "))

    algorithm = int(input("Enter the number of the algorithm you want to use. 1 - ACO  2 - BCO : "))
    while algorithm != 1 and algorithm != 2:
        print("Invalid algorithm number. Please enter 1 for ACO or 2 for BCO.")
        algorithm = int(input("Enter the number of the algorithm you want to use. 1 - ACO  2 - BCO : "))

    return size, mapType, droneNumber, algorithm


def write_log_file(algorithm, drones, mapType, size, duration, iterations):
    """Writes a log file containing the parameters used, duration of the run, and number of iterations.

    Args:
        parameters: A dictionary containing the parameters used in the simulation.
        duration: The duration of the simulation in seconds.
        iterations: The number of iterations in the simulation.
    """

    # Get the current time.
    now = datetime.datetime.now()

    # Create the log file name.
    log_file_name = "Run_{}.log".format(now.strftime("%Y-%m-%d_%H-%M-%S"))
    with open(log_file_name, "w") as f:
    # Open the log file for writing.
        if(algorithm == 1):
            f.write("Algorithm Used: Ant Colony Optimization (ACO)")
        else:
            f.write("Algorithm Used: Bee Colony Optimization (BCO)")

        f.write("Map Size Used: "+  str(size) +"\n")

        if(algorithm == 1):
            f.write("Map Type Used: Completly Random Terrain")
        else:
            f.write("Map Type Used: Random Building Terrain")
    
        f.write("Number of Drones Used: "+  str(drones) +"\n")
        f.write("Duration: {} seconds\n".format(duration))
        f.write("Iterations: {}\n".format(iterations))

def main():
     # Start the simulation.
    start_time = datetime.datetime.now()
    size, mapType, droneNumber, algorithm = askForParameters()
    run = True
    clock = pygame.time.Clock()
    maze = createMaze(size, mapType)
    write_maze_to_txt_file(maze,"maze.txt")
    newTerritory = Territory("maze.txt")
    territory = newTerritory.matrix

    drones = []
    if (algorithm == 2):
        for i in range(1, droneNumber + 1):
            if i%4 == 0:
                drone = BeeDrone("north",0,0)
            elif i%3 == 0:
                drone = BeeDrone("south",0,0)
            elif i%2 == 0:
                drone = BeeDrone("east",0,0)
            else:
                drone = BeeDrone("west",0,0)
            drones.append(drone)
    else:
        for i in range(1, droneNumber + 1):
            if i%4 == 0:
                drone = AntDrone("north",0,0,PHEROMONE_INTENSITY)
            elif i%3 == 0:
                drone = AntDrone("south",0,0,PHEROMONE_INTENSITY)
            elif i%2 == 0:
                drone = AntDrone("east",0,0,PHEROMONE_INTENSITY)
            else:
                drone = AntDrone("west",0,0,PHEROMONE_INTENSITY)
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
                if algorithm == 2:
                    territory = drone.markVisitedCell(territory)
                    territory = drone.reduceCellQuality(territory)
                else:
                    territory = drone.depositPheromone(territory)
            for row in territory:
                for cell in row:
                    if algorithm == 2:
                        cell.reduceQuality()
                    else:
                        cell.evaporatePheromone()
                    if cell.visited == "F":
                        missingCells = True
        else:
            break
        

        
        drawTerritory(territory, algorithm)
        for drone in drones:
            drawDrone(drone.positionX, drone.positionY)
        pygame.display.update()
    
        # Stop the simulation.
    end_time = datetime.datetime.now()

    # Calculate the duration of the simulation.
    duration = (end_time - start_time).total_seconds()
    # Write the log file.
    write_log_file(algorithm, droneNumber, mapType, size, duration, counter)
    pygame.quit()

main()