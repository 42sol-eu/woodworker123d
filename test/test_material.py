import pytest
from woodworker123d import Material, UnitEnum, evaluate_name, evaluate_count, get_base_unit

# Define fixtures for the values used in the test cases
@pytest.fixture
def sample_material_data():
    return "oak", 10, UnitEnum.metric

@pytest.fixture
def invalid_name_material_data():
    return "", 10, UnitEnum.metric

@pytest.fixture
def invalid_count_material_data():
    return "wood", -1, UnitEnum.metric

# Test cases using fixtures
def test_material_creation(sample_material_data):
    name, count, unit = sample_material_data
    material = Material(name, count, unit)
    assert material.name == name
    assert material.count == count
    assert material.unit == unit

def test_material_generate_id():
    assert Material.generate_id() == 1
    assert Material.generate_id() == 2

def test_material_invalid_name(invalid_name_material_data):
    name, count, unit = invalid_name_material_data
    with pytest.raises(ValueError):
        Material(name, count, unit)

def test_material_invalid_count(invalid_count_material_data):
    name, count, unit = invalid_count_material_data
    with pytest.raises(ValueError):
        Material(name, count, unit)
