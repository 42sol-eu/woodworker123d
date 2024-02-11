import pytest
from enum import Enum

from woodworker123d import UnitEnum, get_base_unit, set_default_unit


def test_UnitEnum():
    assert UnitEnum.metric.value == "mm"
    assert UnitEnum.imperial.value == "inch"


def test_set_default_unit():
    set_default_unit(UnitEnum.imperial)
    assert get_base_unit() == UnitEnum.imperial

    set_default_unit(UnitEnum.metric)
    assert get_base_unit() == UnitEnum.metric


def test_get_base_unit():
    # Ensure that the default unit is returned initially
    assert get_base_unit() == UnitEnum.metric

    # Change the default unit and check if it's returned correctly
    set_default_unit(UnitEnum.imperial)
    assert get_base_unit() == UnitEnum.imperial

    # Change the default unit back to the initial value and check
    set_default_unit(UnitEnum.metric)
    assert get_base_unit() == UnitEnum.metric
