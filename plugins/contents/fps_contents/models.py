from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Checkpoint(BaseModel):
    id: str
    last_modified: str


class SaveContent(BaseModel):
    content: Union[str, Dict]
    format: str
    path: str
    type: str


class Content(BaseModel):
    name: str
    path: str
    last_modified: Optional[str]
    created: str
    content: Optional[Union[str, List[Dict]]]
    format: Optional[str]
    mimetype: Optional[str]
    size: Optional[int]
    writable: bool
    type: str