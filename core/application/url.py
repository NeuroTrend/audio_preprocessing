from adaptors.frameworks.url import URLAdaptor
from core.domain.url_rules import ResourceInfo, classify_resource
from config.logger import logger
from core.utils import identify_location

def process_url(url: str) -> ResourceInfo:
    """
    Processes a URL to determine its type, validity, and download requirements.

    Args:
        url: The URL to process.

    Returns:
        A ResourceInfo object containing classification details.
    """
    adaptor = URLAdaptor(url)
    logger.info(f"Identifying location of {url}")
    location = identify_location(url)
    logger.info(f"Location identified as {location}. Validating URL")

    exists, is_dir, is_file, extension, content_type = False, False, False, None, None

    if location == "local":
        exists = adaptor.localExists()
        is_dir = adaptor.localIsDir()
        is_file = adaptor.localIsFile()
        extension = adaptor.getExtension()
    elif location == "http":
        exists = adaptor.httpExists()
        is_dir = adaptor.httpIsDir()
        is_file = adaptor.httpIsFile()
        content_type = adaptor.getContentType()

    logger.info(f"URL validation complete. Generating rules")

    return classify_resource(url, exists, is_dir, is_file, extension, content_type, location)