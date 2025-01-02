from typing import TypedDict, Literal

class ResourceInfo(TypedDict):
    is_valid: bool
    resource_type: Literal["file", "dir", "invalid"]
    download_required: bool

VALID_EXTENSIONS = ["AIFF"]
VALID_CONTENT_TYPES = ["audio/aiff"]

def classify_resource(
    url: str, 
    exists: bool, 
    is_dir: bool = False, 
    is_file: bool = False, 
    extension: str = None, 
    content_type: str = None, 
    location: Literal["local", "http"] = "local"
) -> ResourceInfo:
    """
    Classifies a resource (file or directory) based on its URL and properties.

    Args:
        url: The URL of the resource.
        exists: Whether the resource exists.
        is_dir: Whether the resource is a directory.
        is_file: Whether the resource is a file.
        extension: The file extension (if applicable).
        content_type: The content type (if applicable).
        location: The location of the resource ("local" or "http").

    Returns:
        A ResourceInfo object containing classification details.
    """
    match (exists, is_dir, is_file):
        case (True, True, _):  # It's a directory
            return {
                "is_valid": True,
                "resource_type": "dir",
                "download_required": location == "http" 
            }
        case (True, _, True):  # It's a file
            is_valid = (location == "http" and content_type in VALID_CONTENT_TYPES) or \
                       (location == "local" and extension in VALID_EXTENSIONS)
            return {
                "is_valid": is_valid,
                "resource_type": "file" if is_valid else "invalid",
                "download_required": location == "http" 
            }
        case _:  # Doesn't exist or invalid combination
            return {
                "is_valid": False,
                "resource_type": "invalid",
                "download_required": False
            }