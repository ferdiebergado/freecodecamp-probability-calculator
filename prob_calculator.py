import copy
import random
from typing import Dict, List

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = [color for color, count in kwargs.items() for _ in range(count)]

    def draw(self, num_balls: int) -> List[str]:

        if num_balls > len(self.contents):
            return self.contents

        balls: List[str] = []

        for _ in range(num_balls):
            random_index = random.randrange(len(self.contents))
            ball = self.contents.pop(random_index)
            balls.append(ball)

        return balls


def experiment(
    hat: Hat, expected_balls: Dict[str, int], num_balls_drawn: int, num_experiments: int
) -> float:

    matches = 0

    for _ in range(num_experiments):

        hat_copy = copy.deepcopy(hat)

        balls = hat_copy.draw(num_balls_drawn)

        drawn_balls: Dict[str, int] = {}

        for ball in balls:
            if drawn_balls.get(ball):
                drawn_balls[ball] += 1
            else:
                drawn_balls[ball] = 1

        match = True

        for color, count in expected_balls.items():

            drawn = drawn_balls.get(color)

            if not drawn or drawn < count:
                match = False
                break

        if match:
            matches += 1

    return matches / num_experiments
