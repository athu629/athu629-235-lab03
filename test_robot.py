import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_east_turn(robot):
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.EAST

def test_illegal_move_south(robot):
    robot.turn();
    robot.turn();
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_north_turn(robot):
    robot._state.direction = Direction.WEST
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.NORTH

def test_south_turn(robot):
    robot._state.direction = Direction.EAST
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.SOUTH

def test_west_turn(robot):
    robot._state.direction = Direction.SOUTH
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.WEST

def test_move_east(robot):
    robot._state.direction = Direction.EAST
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2

def test_move_south(robot):
    robot._state.direction = Direction.SOUTH
    robot._state.row = 1
    robot.move()
    state = robot.state()
    assert state['row'] == 2
    assert state['col'] == 1

def test_move_west(robot):
    robot._state.direction = Direction.WEST
    robot._state.col = 2
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1

def test_illegal_move_north(robot):
    robot._state.row = 1
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_move_east(robot):
    robot.turn()
    robot._state.col = 10
    with pytest.raises(IllegalMoveException):
        robot.move()

def test_illegal_move_west(robot):
    robot.turn();
    robot.turn();
    robot.turn();
    with pytest.raises(IllegalMoveException):
        robot.move()

