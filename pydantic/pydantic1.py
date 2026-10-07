from pydantic import BaseModel, ValidationError, validator



class User(BaseModel):
    id: int
    name: str
    is_active:bool

input_data={"id": 1, "name": "John Doe", "is_active":False}

user = User(**input_data)

print(user.id)  # Output: 1
print(user.name)  # Output: John Doe
print(user.is_active)  # Output: False

print(user)
print(user.name.upper())  # Output: JOHN DOE


