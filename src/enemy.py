import random

class Enemy:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def move_towards(self, target_x, target_y, grid):
        """Flytta fienden mot spelaren"""
        dx = target_x - self.pos_x
        dy = target_y - self.pos_y

        if abs(dx) > abs(dy):
            if dx > 0:
                self.pos_x += 1
            else:
                self.pos_x -= 1
        else:
            if dy > 0:
                self.pos_y += 1
            else:
                self.pos_y -= 1

        # Förhindra fienden från att gå igenom väggar
        if grid.get(self.pos_x, self.pos_y) == grid.wall:
            self.pos_x -= dx
            self.pos_y -= dy