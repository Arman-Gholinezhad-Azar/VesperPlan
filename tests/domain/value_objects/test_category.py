import pytest
from domain.value_objects.category import Category


# All happy paths
@pytest.mark.parametrize("category_input, expected", [
    ("work", "work"),
    ("Personal", "personal"),  # Lowercased
    ("   Health   ", "health"),  # Stripped and lowercased
    ("work_house", "work_house"),
    ("work-house", "work-house"),
    ("work house", "work house"),
    ("a", "a"),
    ("a" * 15, "a" * 15),
    ("  LEARNING  ", "learning"),
    ("Shopping", "shopping"),
    ("123", "123"),
])
def test_category_valid_inputs(category_input, expected):
    category = Category(category_input)
    assert str(category) == expected


# All failure paths
@pytest.mark.parametrize("invalid_input, expected_error, match_text", [
    (123, TypeError, "Category should be string"),
    (None, TypeError, "Category should be string"),
    (True, TypeError, "Category should be string"),
    ([], TypeError, "Category should be string"),
    ("", ValueError, "category cannot be empty!"),
    ("   ", ValueError, "category cannot be empty!"),
    ("\t\n", ValueError, "category cannot be empty!"),
    ("a" * 16, ValueError, "category cannot be more than 15 characters"),
    ("hello@world", ValueError, "invalid category pattern"),
    ("wow!", ValueError, "invalid category pattern"),
    ("#tag", ValueError, "invalid category pattern"),
    ("hello$", ValueError, "invalid category pattern"),
])
def test_category_invalid_inputs(invalid_input, expected_error, match_text):
    with pytest.raises(expected_error, match=match_text):
        Category(invalid_input)