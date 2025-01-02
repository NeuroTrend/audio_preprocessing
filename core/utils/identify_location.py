def identify_location(url) -> str:
        if url.startswith("/") or url.startswith("./"):
            return "local"
        elif url.startswith("http://"):
            return "http"
        else:
            return "invalid"