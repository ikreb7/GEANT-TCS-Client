

class ACMEEVDetailsResource:
    """ ACME EV details resource """

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.username = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def list_acme_servers(self, org_name: str, org_country: str, post_office_box: str, org_address_1: str,
                          org_address_2, org_address_3, org_locality: str, org_state_or_province: str,
                          org_postal_code: str, org_joi_state: str, org_joi_locality: str, assumed_name: str,
                          business_category: str, date_of_incorporation: str, company_number: str):
        """ List ACME servers.

        Args:
            org_name (str): EV organization name [Must not be blank, Size must be between 0 and 128 inclusive]
            org_country (str): EV organization country [Size must be between 2 and 2 inclusive]
            post_office_box (str): EV organization post office box [Size must be between 0 and 40 inclusive]
            org_address_1 (str): EV organization address 1 [Size must be between 0 and 128 inclusive]
            org_address_2 (str): EV organization address 2 [Size must be between 0 and 128 inclusive]
            org_address_3 (str): EV organization address 3 [Size must be between 0 and 128 inclusive]
            org_locality (str): EV organization city [Size must be between 0 and 128 inclusive]
            org_state_or_province (str): EV organization state/province [Size must be between 0 and 128 inclusive]
            org_postal_code (str): EV organization postal code [Size must be between 0 and 40 inclusive]
            org_joi_state (str): EV organization state or province of incorporation [Size must be between 0 and 128
                                 inclusive]
            org_joi_locality (str): EV organization jurisdiction of incorporation city or town [Size must be between 0
                                    and 128 inclusive]
            assumed_name (str): EV organization assumed name [Size must be between 0 and 128 inclusive]
            business_category (str): EV organization business category. Values: [PrivateOrganization, GovernmentEntity,
                                     BusinessEntity, NonCommercialEntity]
            date_of_incorporation (str): EV organization date of incorporation [Size must be between 8 and 8 inclusive]
            company_number (str): EV organization registration number [Size must be between 0 and 25 inclusive]

        Return:
            domains[] (list): ACME account domains
            domains[].name (str): ACME account domain name

        Example:
            {"domains":[{"name":"domain.ccmqa.com"},{"name":"sub.domain.ccmqa.com"}]}
        """