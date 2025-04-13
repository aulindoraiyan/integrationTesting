"""
Tests for ../app.py

Run from the project directory (not the tests directory) with the invocation `pytest tests/tests.py`
"""
import streamlit as st
from streamlit.testing.v1 import AppTest

def test_button_increments_counter():
    """Test that the counter increments when the button is clicked."""
    at = AppTest.from_file("app.py").run()

    # Initialize the session state.
    # Note that we use at.session_state, not st.session_state. This is the testing session_state object.
    at.session_state.count = 1

    # Click the button
    at.button(key="increment").click().run()

    # Assert that the counter has been incremented
    assert at.session_state.count == 2

def test_button_decrements_counter(at):
    at.run()

    # First, increment twice so we can safely decrement
    at.button[0].click()  # +1
    at.button[0].click()  # +1
    assert at.text[0].value == "Total count is 2"

    # Click the decrement button
    at.button[1].click()  # -1
    assert at.text[0].value == "Total count is 1"

    at.button[1].click()  # -1
    assert at.text[0].value == "Total count is 0"

    # Should not go below zero
    at.button[1].click()  # -1
    assert at.text[0].value == "Total count is 0"


def test_button_increments_counter_ten_x(at):
    at.run()

    # Enable 10x mode
    with at.expander("Options"):
        at.checkbox[0].check()

    assert at.button[0].label == "plus 10"

    # Click increment
    at.button[0].click()
    assert at.text[0].value == "Total count is 10"

    # Click again
    at.button[0].click()
    assert at.text[0].value == "Total count is 20"


def test_button_decrements_counter_ten_x(at):
    at.run()

    # Enable 10x mode
    with at.expander("Options"):
        at.checkbox[0].check()

    # Pre-increment to 20 so we can decrement
    at.button[0].click()
    at.button[0].click()
    assert at.text[0].value == "Total count is 20"

    # Click decrement
    at.button[1].click()
    assert at.text[0].value == "Total count is 10"

    # Again
    at.button[1].click()
    assert at.text[0].value == "Total count is 0"

    # Try to go below 0
    at.button[1].click()
    assert at.text[0].value == "Total count is 0"

def test_output_text_correct():
    """Test that the text shows the correct value."""
    at = AppTest.from_file("app.py").run()

    # Initialize session state
    at.session_state.count = 0
    at.session_state.ten_x = False

    # Increment once at 1x, once at 10x.
    at.button(key="increment").click().run()
    at.checkbox(key="ten_x").check().run()
    at.button(key="increment").click().run()

    # Check text value
    assert at.markdown[0].value == "Total count is 11"
