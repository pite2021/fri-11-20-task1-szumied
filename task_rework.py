from dataclasses import dataclass
from typing import Callable
from typing import List


class Car:
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

    def wait(self, time):
        print(f"[Speed: {self.speed}, wheel angle: {self.wheel_angle}] Waiting {time}.")

    def avoid_obstacle(self):
        angle = 45
        self.set_angle(angle)
        self.set_angle(-angle)
        self.set_angle(0)


@dataclass
class Event:
    type: str
    time: int
    actions: List[Callable]


events_list = [
    Event("Drive Normally", 0, [lambda car: car.set_speed(50)]),
    Event("Red Light", 3, [lambda car: car.set_speed(0), lambda car: car.wait(10)]),
    Event("Fantasize about street racing", 4, [lambda car: car.modify_speed(100)]),
    Event(
        "Remember phone's in the kitchen",
        8,
        [lambda car: car.set_angle(180), lambda car: car.set_angle(0)],
    ),
    Event("Obstacle", 12, [lambda car: car.avoid_obstacle()]),
]


def main():
    car1 = Car()
    [car1.act(event) for event in events_list]


if __name__ == "__main__":
    main()
