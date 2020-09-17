'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #Co-ordinates
        x, y = 0, 0
        #To pick the instructions
        direct = 0
        moves = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        instructions = instructions*4
        for instruction in instructions:
            if instruction == 'G':
                x += moves[direct][0]
                y += moves[direct][1]
            elif instruction == 'L':
                direct = (direct+1)%4
            elif instruction == 'R':
                direct = (direct+3)%4
        #Its indications that Robot is inside the circle
        return (x == 0 and y == 0)
