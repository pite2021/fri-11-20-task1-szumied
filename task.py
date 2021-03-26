import numpy as np
from random import randrange


class Simulation:
    def __init__(self, car, road):
        self.car = car
        self.road = road

    def show_car_position():
        pass

    def Simulate(self, car, road):
        while(self.car.position[1] < self.road.roads_length):
            Car.Drive()


class Road:
    def __init__(self):
        self.layout = np.zeros((32, 3))
        self.roads_length = self.layout.shape[0]
        self.roads_width = self.layout.shape[1]
        self.generate_obstacles()

    def generate_obstacles(self, max_count_of_obstacles=3):
        obstacles_count = 0

        def generate_obstacle_coordinates():
            x = randrange(self.roads_width)
            y = randrange(self.roads_length)
            return (y, x)

        print("Obstacles coordinates:")
        while obstacles_count < max_count_of_obstacles:
            obstacle_coordinates = generate_obstacle_coordinates()
            print(obstacle_coordinates)
            self.layout[obstacle_coordinates] = 1
            obstacles_count = obstacles_count + 1

        print("\nObstacles layout:")
        self.print_layout()

        print("\Layout shape:")
        print(self.layout.shape)

    def print_layout(self):
        print(self.layout)


class Car:
    def __init__(self):
        self.wheel_angle = 0  # - 90 left, 90 right, 0 forward
        self.speed = 0
        self.position = (0, 1)

    def Drive():
        pass


def main():
    road = Road()
    car = Car()
    road = Road()
    Simulation(car, road)


if __name__ == "__main__":
    main()
