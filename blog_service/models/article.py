  
from typing import List, Optional

from pydantic import Schema, Field
from .base import DBModelMixin, ObjectIdStr

class Article(DBModelMixin):
    title: str
    description: str
    body: str
    tags: List[str]
    author_id: Optional[ObjectIdStr]
    like_count: int