class SessionStateModel:
    """Small wrapper around a session-state-like store.

    Example:
        >>> state = SessionStateModel(st.session_state)
        >>> state.ensure("characters", [])
        []
    """

    def __init__(self, state_store):
        self._state_store = state_store

    def ensure(self, key, default_value):
        if key not in self._state_store:
            self._state_store[key] = default_value
        return self._state_store[key]

    def get(self, key, default=None):
        return self._state_store.get(key, default)

    def set(self, key, value):
        self._state_store[key] = value
        return value

    def __contains__(self, key):
        return key in self._state_store

    def __getitem__(self, key):
        return self._state_store[key]

    def __setitem__(self, key, value):
        self._state_store[key] = value
