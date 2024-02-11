import pytest
from enum import Enum

from woodworker123d import Board, Material

@pytest.fixture
def valid_dimensions():
    return 20, 5, 1


@pytest.fixture
def default_material():
    return "birch"

@pytest.fixture
def another_material():
    return "spruce"

def test_board(valid_dimensions, default_material, another_material):

    width, height, thickness = valid_dimensions
    

    b = Board("Test 1 - valid", height, width, thickness, default_material)
    assert b is not None
    assert isinstance(b, Board)
    assert isinstance(b, Material)
    assert b.id == 1
    assert b.name == "Test 1 - valid"

    b = Board("Test 2 - valid", width, height, thickness, another_material)
    assert b is not None
    assert isinstance(b, Board)
    assert isinstance(b, Material)
    assert b.id == 2
    assert b.name == "Test 2 - valid"

    
    Board.set_default_material(default_material)
    b = Board("Test 3 - valid", width, height, thickness)
    assert b is not None
    assert isinstance(b, Board)
    assert b.material == default_material

    Board.set_default_thickness(thickness)
    b = Board("Test 3 - valid", width, height)
    assert b is not None
    assert isinstance(b, Board)
    assert b.material == default_material
    assert b.thickness == thickness
    assert Board.get_default_material() == default_material
    assert Board.get_default_thickness() == thickness


# Define fixtures for the values used in the test cases
@pytest.fixture
def invalid_name():
    return ""


@pytest.fixture
def valid_material():
    return "oak"

# Test case using fixtures
def test_board_invalid(invalid_name, valid_dimensions, valid_material):
    width, height, thickness = valid_dimensions
    
    next_id = Material._next_id 

    with pytest.raises(ValueError):
        b = Board(invalid_name, width, height, thickness, valid_material)  # Invalid name

    with pytest.raises(ValueError):
        b = Board(42, width, height, thickness, valid_material)  # Invalid name
    
    with pytest.raises(ValueError):
        b = Board("width - wrong type", "10", height, thickness, valid_material)

    with pytest.raises(ValueError):
        b = Board("width - wrong type", width, "10", thickness, valid_material)

    with pytest.raises(ValueError):
        b = Board("width - negative", -width, height, thickness, valid_material)

    with pytest.raises(ValueError):
        b = Board("height - negative", width, -height, thickness, valid_material)

    with pytest.raises(ValueError):
        b = Board("thickness - negative", width, height, -thickness, valid_material)

    with pytest.raises(ValueError):
        b = Board("thickness invalid coefficient", 1, 1, 1, valid_material)

    # ID is still 1
    b = Board("Test 1 - valid", 10, 20, 1, "oak")
    assert b is not None
    assert isinstance(b, Board)
    assert isinstance(b, Material)
    assert b.id == next_id
    assert b.name == "Test 1 - valid"
    