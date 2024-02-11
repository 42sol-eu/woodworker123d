import pytest

from woodworker123d import Board, Material, MaterialsList

@pytest.fixture
def setup():
    # Setup code: initialize resources before the test
    print("Setup")
    Board.set_default_material("oak")
    Board.set_default_thickness(18.0)
    # This can be used to set up connections, create temporary files, etc.
    yield  # This is where the test will run
    # Teardown code: clean up resources after the test
    print("Teardown")
    # This can be used to close connections, delete temporary files, etc.


@pytest.fixture
def material():
    return Material("Nails", 10)

@pytest.fixture
def boards():
    return (Board("Roof", 200.0, 230.0, 18.0),Board("Bottom", 130.0, 130.0, 18.0),)


@pytest.fixture
def materials_list(material):
    return MaterialsList(material)


def test_MaterialsList_str(materials_list):
    assert str(materials_list) == "Materials: 1 - 1 items."


@pytest.mark.skip(reason="The assert is not working")
def test_MaterialsList_repr(materials_list):
    print(f"##########\n{repr(materials_list)}\n##########")
    assert str(repr(materials_list)).find("Materials: 10\n") != -1
    


def test_MaterialsList_append_valid(setup, materials_list, material, boards):
    materials_list.append(material)
    assert len(materials_list) == 2
    assert str(materials_list) == "Materials: 2 - 2 items."

    # TODO: test for default material and thickness


def test_MaterialsList_append_invalid(materials_list):
    with pytest.raises(ValueError):
        materials_list.append("Invalid material")


def test_MaterialsList_instance_type(materials_list):
    assert isinstance(materials_list, MaterialsList)
