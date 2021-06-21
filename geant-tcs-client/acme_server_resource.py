
class ACMEServerResource:
    """ ACME server resource """

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.username = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def list_acme_servers(self, position: int, size: int, active: str, name: str, url: str, cert_validation_type: str,
                          ca_id: int):
        """ List ACME servers.

        Args:
            position (int): Position shift
            size (int): Count of entries
            active (str): ACME server active state
            name (str): ACME server name
            url (str): ACME server URL
            cert_validation_type (str): ACME server validation type. Values: [DV, OV, EV]
            ca_id (int) ACME server CA ID

        Return:
            [] (list): List of ACME servers
            [].active (bool): ACME server active state
            [].name (str): ACME server name
            [].certValidationType (str): ACME server validation type. Values: [DV, OV, EV]
            [].url (str): ACME server URL
            [].caId (int): ACME server CA ID
            [].singleProductId (int): ACME server single product ID
            [].multiProductId (int): ACME server multi product ID
            [].wcProductId (int): ACME server WC product ID

        Example:
            [{"active":true,"url":"https:/acmeserverfortest-OV","caId":40485,"name":"OV ACME Server",
            "singleProductId":66362,"multiProductId":23234,"wcProductId":14608,"certValidationType":"OV"}]
        """

        url = f"/acme/{self.version}/server?postion={position}&size={size}&active={active}&name={name}&url={url}" \
              f"&certValidationType={cert_validation_type}&caId={ca_id}"
        headers = {"login": self.username, "password": self.password, "customerUri": self.custom_uri,}

        response = self.client.get(url, headers=headers)
        return response
