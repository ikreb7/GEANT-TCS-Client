
import httpx


class GEANTTCSClient:

    def __init__(self):
        self.client = httpx.Client()

    def connect(self):
        return self.client
