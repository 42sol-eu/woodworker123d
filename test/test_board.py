import pytest
from enum import Enum

from woodworker123d import Board, Material

def test_board():
    b = Board("Test 1 - valid", 10, 20, 1, "oak")
    assert b is not None
    assert isinstance(b, Board)
    assert isinstance(b, Material)
    assert b.id == 1
    assert b.name == "Test 1 - valid"

    b = Board("Test 2 - valid", 5, 20, 1, "spruce")
    assert b is not None
    assert isinstance(b, Board)
    assert isinstance(b, Material)
    assert b.id == 2
    assert b.name == "Test 2 - valid"


# Define fixtures for the values used in the test cases
@pytest.fixture
def invalid_name():
    return ""

@pytest.fixture
def valid_dimensions():
    return 10, 20, 1

@pytest.fixture
def valid_material():
    return "oak"

# Test case using fixtures
def test_board_invalid(invalid_name, valid_dimensions, valid_material):
    width, height, thickness = valid_dimensions
    
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
    assert b.id == 1
    assert b.name == "Test 1 - valid"
    