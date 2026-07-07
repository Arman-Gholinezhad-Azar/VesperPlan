import pytest
from domain.value_objects.task_discription import TaskDiscription


# All happy paths
@pytest.mark.parametrize("description_input, expected", [
    ("Buy groceries for dinner", "Buy groceries for dinner"),
    ("   hello world   ", "hello world"),
    ("A", "A"),
    ("a" * 500, "a" * 500),
    ("  Task with spaces  ", "Task with spaces"),
    ("", ""),  # Empty is allowed for description
    ("   ", ""),  # Whitespace only becomes empty
    ("Normal task description", "Normal task description"),
    ("Task with symbols @#$%^&*()", "Task with symbols @#$%^&*()"),
    ("1234567890", "1234567890"),
    ("Task with\nnewlines", "Task with\nnewlines"),
    ("Task with\ttabs", "Task with\ttabs"),
])
def test_task_discription_valid_inputs(description_input, expected):
    description = TaskDiscription(description_input)
    assert str(description) == expected


# All failure paths
@pytest.mark.parametrize("invalid_input, expected_error, match_text", [
    (123, TypeError, "Task discription should be string!"),
    (None, TypeError, "Task discription should be string!"),
    (True, TypeError, "Task discription should be string!"),
    ([], TypeError, "Task discription should be string!"),
    (45.67, TypeError, "Task discription should be string!"),
    ({}, TypeError, "Task discription should be string!"),
    ("a" * 501, ValueError, "Discripion is too long."),
    ("a" * 1000, ValueError, "Discripion is too long."),
])
def test_task_discription_invalid_inputs(invalid_input, expected_error, match_text):
    with pytest.raises(expected_error, match=match_text):
        TaskDiscription(invalid_input)