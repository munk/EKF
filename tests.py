#GPLv3
from process import move
from numpy import array_equiv, pi
from numpy.testing import assert_array_almost_equal

def test_move_no_motion():
    position = [0,0,0]
    control = [0,0]
    result = move(position, control)
    assert array_equiv(result, [0, 0, 0])

def test_move_linear_x():
    position = [0,0,0]
    control = [1,0]
    result = move(position, control)
    assert array_equiv(result, [1, 0, 0])

def test_move_linear_y():
    position = [0, 0, pi/2]
    control = [1, 0]
    result = move(position, control)
    assert_array_almost_equal(result, [0, 1, pi/2])


