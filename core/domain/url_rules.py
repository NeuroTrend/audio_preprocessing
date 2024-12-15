from typing import TypedDict, Literal

class ValidationResult(TypedDict):
    valid: bool
    type: Literal["file", "dir", "invalid"]
    downloadRequired: bool

VALID_EXTENSIONS = ["AIFF"]
VALID_CONTENT_TYPES = ["audio/aiff"]



class URLRules:
    def __init__(self, url: str, exists: bool, isDir = False, isFile = False, extension = None, content_type = None):
        self.url = url
        self.exists = exists
        self.isDir = isDir
        self.isFile = isFile
        self.extension = extension
        self.content_type = content_type

    def validateLocal(self) -> ValidationResult:
        match (self.exists, self.isDir, self.isFile):
            case (True, True, _):
                return {
                    "valid": True,
                    "type": "dir",
                    "downloadRequired": False
                }
            case (True, _, True):
                if self.extension in VALID_EXTENSIONS:
                    return {
                        "valid": True,
                        "type": "file",
                        "downloadRequired": False
                    }
            case _:
                return {
                    "valid": False,
                    "type": "invalid",
                    "downloadRequired": False
                }
        

    def validateHTTPS(self) -> ValidationResult:
        match (self.exists, self.isDir, self.isFile):
            case (True, True, _):
                return {
                    "valid": True,
                    "type": "dir",
                    "downloadRequired": True
                }
            case (True, _, True):
                if self.content_type in VALID_CONTENT_TYPES:
                    return {
                        "valid": True,
                        "type": "file",
                        "downloadRequired": True
                    }
            case _:
                return {
                    "valid": False,
                    "type": "invalid",
                    "downloadRequired": False
                }