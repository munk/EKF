#GPLv3
import numpy as np

def move(position, control):
    """Calculate change in pose given a 2d control vector"""
    heading = position[2]
    velocity = control[0]
    dx = velocity * np.cos(heading)
    dy = velocity * np.sin(heading)
    result = [dx, dy, heading]
    return result
