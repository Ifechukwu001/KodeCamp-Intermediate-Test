from typing import Any, Generator


def get_id() -> Generator[int, None, None]:
    id = 1
    while True:
        yield id
        id += 1


id = get_id()

Book: dict[int, dict[str, Any]] = dict()
