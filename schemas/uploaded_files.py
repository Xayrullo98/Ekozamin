from fastapi import UploadFile,File
from pydantic import BaseModel,FilePath


class Uploaded_fileBase(BaseModel):
	source: str


class Uploaded_fileCreate(Uploaded_fileBase):
	source_id: int
	user_id: int
	file: UploadFile = File()

class Uploaded_fileOut(Uploaded_fileBase):
	id: int
