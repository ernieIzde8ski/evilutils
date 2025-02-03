from eviltyping import name

INDENT = " " * 8
END = "\n"


class UnwrapError(Exception):
    error: Exception | None = None

    def __init__(self, received: object, expected: object) -> None:
        message = [name(type(self)), "could not unwrap value:"]
        if expected is None:
            message += (" ", repr(received))
        else:
            message += (END, f"{INDENT}{expected = }{END}", f"{INDENT}{received = }")
        super().__init__("".join(message))
