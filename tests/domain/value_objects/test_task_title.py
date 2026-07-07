import pytest
from domain.value_objects.task_title import TaskTitle


# all happy paths
@pytest.mark.parametrize("title_input, expected", [
    ("Buy groceries", "Buy groceries"),
    ("   hello   ", "hello"),
    ("task_1.0-final", "task_1.0-final"),
    ("a", "a"),
    ("a" * 15, "a" * 15),
    ("  Task  ", "Task"),
    ("task123", "task123"),
    ("Buy groceries now", "Buy groceries now"),
])
def test_task_title_valid_inputs(title_input, expected):
    title = TaskTitle(title_input)
    assert str(title) == expected


# all failure paths
@pytest.mark.parametrize("invalid_input, expected_error, match_text", [
    (123, TypeError, "Task title should be string!"),
    (None, TypeError, "Task title should be string!"),
    (True, TypeError, "Task title should be string!"),
    ([], TypeError, "Task title should be string!"),
    ("", ValueError, "Task name should not be empty."),
    ("   ", ValueError, "Task name should not be empty."),
    ("\t\n", ValueError, "Task name should not be empty."),
    ("a" * 31, ValueError, "Task name should not be more than 30 characters."),
    ("hello@world", ValueError, "Task name cannot use special characters"),
    ("wow!", ValueError, "Task name cannot use special characters"),
    ("#task", ValueError, "Task name cannot use special characters"),
    ("50%done", ValueError, "Task name cannot use special characters"),
    ("price$", ValueError, "Task name cannot use special characters"),
])
def test_task_title_invalid_inputs(invalid_input, expected_error, match_text):
    with pytest.raises(expected_error, match=match_text):
        TaskTitle(invalid_input)