# 11. Книга и авторы

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Book:
    title: str
    authors: List[str] = field(default_factory=list)
    year: int | None = None

    def formatted(self) -> str:
        year_part = f"({self.year})" if self.year is not None else "(No year)"
        authors_part = ", ".join(self.authors) if self.authors else "Unknown author"
        return f"{self.title} {year_part} — {authors_part}"

b1 = Book("Python 101", ["John Doe"], 2020)
b2 = Book("Безымянная книга")
b3 = Book("Совместный труд", ["Alice", "Bob"])

for b in (b1, b2, b3):
    print(b.formatted())