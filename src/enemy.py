import random


class Enemy:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move_towards(self, target_x, target_y, grid):
        if random.random() < 0.4:  # 40% chans att röra sig
            dx = 0
            dy = 0
            x_diff = target_x - self.pos_x
            y_diff = target_y - self.pos_y

            if abs(x_diff) > abs(y_diff):
                dx = 1 if x_diff > 0 else -1
            else:
                dy = 1 if y_diff > 0 else -1

            new_x = self.pos_x + dx
            new_y = self.pos_y + dy
            if grid.get(new_x, new_y) != grid.wall:
                self.pos_x = new_x
                self.pos_y = new_y
