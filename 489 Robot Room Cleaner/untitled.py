# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.visited = set()
        self.robot = robot
        i, j = 0, 0
        direction = 1

        self.robot.clean()
        self.visited.add((i, j))
        self.robot.turnLeft()
        for _ in range(4):
            direction = (direction + 1) % 4
            if self.robot.move():
                self.clean(direction + 2 % 4, *self.update(i, j, direction))
            else:
                self.robot.turnLeft()
                self.robot.turnLeft()

    def clean(self, direction, i, j):
        if (i, j) not in self.visited:
            self.robot.clean()
            self.visited.add((i, j))
            self.robot.turnLeft()
            for _ in range(3):
                direction = (direction + 1) % 4
                if self.robot.move():
                    self.clean(direction + 2 % 4, *self.update(i, j, direction))
                else:
                    self.robot.turnLeft()
                    self.robot.turnLeft()
        else:
            self.robot.turnLeft()
            self.robot.turnLeft()
            self.robot.move()

    def update(i, j, direction):
        if direction == 0:
            return i, j + 1 
        if direction == 1:
            return i - 1, j
        if direction == 2:
            return i, j - 1
        if direction == 3:
            return i + 1, j


