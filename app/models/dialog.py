from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DialogInInput(BaseModel):
    limit: int = 20
    offset_date: Optional[datetime] = None
    ignore_pinned: Optional[bool] = False
    ignore_migrated: Optional[bool] = True
    archived: Optional[bool] = False


class DialogInResponse(BaseModel):
    chat: str
    from_user: str
    message: str
