"""Core functionality."""


def greet(name: str) -> str:
    """Return a greeting for ``name``.

    Raises:
        ValueError: if ``name`` is empty or whitespace.
    """
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
