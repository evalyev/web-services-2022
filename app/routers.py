from fastapi import APIRouter

from app import contracts

router = APIRouter()


@router.get("/")
async def get_hello():
    return "Hello, world!"


@router.get("/name/{name}")
async def get_hello_name(name: str):
    return f"Hello, {name}!"


@router.get("/name-query/")
async def get_hello_name_query(name: str, q: str | None = None):
    if q:
        return f"Hello, {name}! {q}"
    return f"Hello, {name}!"


@router.post("/")
async def create_item(human: contracts.Human):
    if human.older_child:
        return f"Hello, {human.name}! You are {human.age} years old. Your eldest child's name is {human.older_child}."
    return f"Hello, {human.name}! You are {human.age} years old."
