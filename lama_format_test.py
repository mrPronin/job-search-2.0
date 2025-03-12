from crewai import LLM
from pydantic import BaseModel


class Dog(BaseModel):
    name: str
    age: int
    breed: str


llm = LLM(
    model="ollama/llama3.3",
    base_url="http://localhost:11434",
    format=Dog.model_json_schema(),
)

response = llm.call(
    "Analyze the following messages and return the name, age, and breed. "
    "Meet Kona! She is 3 years old and is a black german shepherd."
)

print(f"response: {response}")
dog = Dog.model_validate_json(response)
print(f"dog: {dog}")
