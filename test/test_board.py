import pytest
from enum import Enum

from woodworker123d import Board, Material

def test_board():
    b = Board(1, "Test 1", 10, 20, 1, "oak")
    assert b is not None
    assert isinstance(b, Board)
    assert isinstance(b, Material)
    assert b.id == 1
    assert b.name == "Test 1"
