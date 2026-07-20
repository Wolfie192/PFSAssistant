import unittest

from src.state import SessionStateModel


class SessionStateModelTests(unittest.TestCase):
    def test_ensure_initializes_missing_value(self):
        raw_state = {}
        state = SessionStateModel(raw_state)

        self.assertEqual(state.ensure("foo", 1), 1)
        self.assertEqual(raw_state["foo"], 1)

    def test_get_and_set_roundtrip(self):
        raw_state = {"foo": "bar"}
        state = SessionStateModel(raw_state)

        self.assertEqual(state.get("foo"), "bar")
        state.set("hello", "world")
        self.assertEqual(raw_state["hello"], "world")


if __name__ == "__main__":
    unittest.main()
