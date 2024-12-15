from typing import TypedDict, Literal

class ValidationResult(TypedDict):
    valid: bool
    type: Literal["file", "dir", "invalid"]
    downloadRequired: bool

class IdentificationResult(TypedDict):
    type: Literal["local", "http", "invalid"]
    url: str

valid_extensions = ["AIFF"]



class URLRules:

    def identify(self, url: str) -> str:
        """
        Identifies if a URL is local or an HTTP URL.

        Args:
          url: The URL to identify.

        Returns:
          "local" if the URL is a local file path, "http" if it's an HTTPs URL, 
          or "invalid" if it's neither.
        """

        if url.startswith("/") or url.startswith("./"):
            return {
                "type": "local",
                "url": url
            }
        elif url.startswith("http://"):
            return {
                "type": "http",
                "url": url
            }
        else:
            return {
                "type": "invalid",
                "url": url
            }

    def validateLocal(self, url: str, exists: bool, isDir: bool, isFile: bool) -> ValidationResult:
        """
        Validates a local URL.

        Args:
          url: The local URL to validate.
          exists: Whether the file exists.
          isDir: Whether the file is a directory.
          isFile: Whether the file is a regular file.

        Returns:
          True if the URL is a valid local file path, False otherwise.
        """
        match (exists, isDir, isFile):
            case (True, True, _):
                return {
                    "valid": True,
                    "type": "dir",
                    "downloadRequired": False
                }
            case (True, _, True):
                extension = url.split('.').pop()
                if extension in valid_extensions:
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
        

    def validateHTTPS(self, url: str, exists: bool, isDir: bool, isFile: bool) -> bool:
        """
        Validates an HTTPs URL.

        Args:
          url: The HTTPs URL to validate.

        Returns:
          True if the URL is a valid HTTPs URL, False otherwise.
        """
        match (exists, isDir, isFile):
            case (True, True, _):
                return {
                    "valid": True,
                    "type": "dir",
                    "downloadRequired": True
                }
            case (True, _, True):
                extension = url.split('.').pop()
                if extension in valid_extensions:
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