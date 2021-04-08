"""Module containing events and car objects."""

import random
import time
from dataclasses import dataclass
from typing import Callable
from typing import List


class Car:
    """Car object with 3 basic parameters: speed, angle, status."""

    def __init__(self):
        self.speed = 0
        self.wheel_angle = 0
        self.status = ""

    def print_status(self):
        msg = f"[Speed: {self.speed}, wheel angle: {self.wheel_angle}] {self.status}"
        print(msg)

    def update_status(self, status):
        self.status = status
        self.print_status()

    def act(self, event):
        self.update_status(f"**EVENT: {event.type}.**")
        [action(self) for action in event.actions]

    def set_speed(self, speed):
        self.speed = speed
        self.update_status(f"Set speed to {speed}")

    def modify_speed(self, speed):
        self.speed = self.speed + speed
        self.update_status(f"Adjust speed by {speed}")

    def set_angle(self, angle):
        self.wheel_angle = angle
        self.update_status(f"Set wheel angle to {angle}")

    def wait(self, wait_time):
        print(
            f"[Speed: {self.speed}, wheel angle: {self.wheel_angle}] Waiting {wait_time}."
        )

    def avoid_obstacle(self):
        angle = 45
        self.set_angle(angle)
        self.set_angle(-angle)
        self.set_angle(0)


@dataclass
class Event:
    """An event for Car to act upon"""

    type: str
    time: int
    actions: List[Callable]


EVENTS_LIST = [
    Event("Drive Normally", 0, [lambda car: car.set_speed(50)]),
    Event(
        "Red Light",
        3,
        [
            lambda car: car.set_speed(0),
            lambda car: car.wait(10),
            lambda car: car.set_speed(50),
        ],
    ),
    Event("Fantasize about street racing", 4, [lambda car: car.modify_speed(100)]),
    Event(
        "Remember phone's left behind",
        8,
        [lambda car: car.set_angle(180), lambda car: car.set_angle(0)],
    ),
    Event("Obstacle", 12, [lambda car: car.avoid_obstacle()]),
]


class Simulation:
    """Contains the simulation method. Could use asyncio, or threading module later on."""

    step_time = 1

    def __init__(self, car):
        self.car = car

    def run(self):
        while True:
            random_event = random.choice(EVENTS_LIST)
            self.car.act(random_event)
            time.sleep(self.step_time)


def main():
    car1 = Car()
    Simulation(car1).run()


if __name__ == "__main__":
    main()
