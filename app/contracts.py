from pydantic import BaseModel


class Human(BaseModel):
    """Contract for name."""

    name: str
    age: int
    older_child: str | None = None
