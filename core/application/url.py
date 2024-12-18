from adaptors.frameworks.url import URLAdaptor
from core.domain.url_rules import URLRules, ValidationResult
from config.logger import logger

class URLProcessor:
    def process_url(self, url: str) -> ValidationResult:
        adaptor = URLAdaptor(url)
        logger.info(f"Identifying location of {url}")
        location = adaptor.identify_location()
        logger.info(f"Location identified as {location}. Validating URL")
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
        else:
            exists = False
            is_dir = False
            is_file = False
        logger.info(f"URL validation complete. Generating rules")

        rules = URLRules(url, exists, is_dir, is_file, extension, content_type)
        if location == "local":
            logger.info("Validating local URL")
            return rules.validateLocal()
        logger.info("Validating HTTPS URL")
        return rules.validateHTTPS()
