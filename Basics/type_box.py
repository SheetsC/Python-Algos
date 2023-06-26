# Generics allow a class, interface, or method to operate on typed parameters. 
# This helps in ensuring type safety. Generics can also improve performance, 
# especially in languages like Java and C#, as they eliminate the need for 
# typecasting and runtime type checks.

from typing import Generic, TypeVar

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content
        
    def get_content(self) -> T:
        return self.content
