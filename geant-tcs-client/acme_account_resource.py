
class ACMEAccountResource:
    """ ACME account resource """

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.username = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def find_acme_account_by_id(self, id: int):
        """ Find ACME account by ID.

        Args:
            id (int): ACME account entity ID

        Returns:
            id (int): ACME account entity ID
            name (str): ACME account name
            status (str): ACME account status
            macKey (str): ACME account HMAC key
            macId (str): ACME account key ID
            acmeServer (str): ACME account server name
            organizationId (int): ACME account organization ID
            certValidationType (str): ACME account server validation type. Values: [DV, OV, EV]
            accountID (str): ACME account ID
            ovOrderNumber (int): OV order number
            contacts (str): ACME account contacts
            evDetails (object): ACME account EV details
            evDetails.orgName (str): EV organization name
            evDetails.orgCountry (str): EV organization country
            evDetails.postOfficeBox (str): EV organization post office box
            evDetails.orgAddress1 (str): EV organization address 1
            evDetails.orgAddress2 (str): EV organization address 2
            evDetails.orgAddress3 (str): EV organization address 3
            evDetails.orgLocality (str): EV organization city
            evDetails.orgStateOrProvince (str): EV organization state/province
            evDetails.orgPostalCode (str): EV organization postal code
            evDetails.orgJoiState (str): EV organization state or province of incorporation
            evDetails.orgJoiCountry (str): EV organization country of incorporation
            evDetails.orgJoiLocality (str): EV organization jurisdiction of incorporation city or town
            evDetails.assumedName (str): EV organization assumed name
            evDetails.businessCategory (str): EV organization business category. Values: [PrivateOrganization, GovernmentEntity, BusinessEntity, NonCommercialEntity]
            evDetails.dateOfIncorporation (str): EV organization date of incorporation
            evDetails.companyNumber (str): EV organization registration number
            domains[] (list): ACME account domains
            domains[].name (str): ACME account domain name

        Example:
            {"id":76,"name":"EV ACME Account","status":"Pending","macKey":"bf174674-6534-4e59-af6e-594bd2f7e1bd",
            "macId":"82efe740-50f0-4685-b1a3-2e8599748855","acmeServer":"EV ACME Server","organizationId":1873,
            "certValidationType":"EV","accountId":"82efe740-50f0-4685-b1a3-2e8599748855","ovOrderNumber":0,
            "contacts":"email@ccmqa.com","evDetails":{"orgName":"org4Test","orgCountry":"UA",
            "postOfficeBox":"PostOfficeBox","orgAddress1":"Deribasovskaya 1","orgAddress2":"Street 2",
            "orgAddress3":"Street 3","orgLocality":"Odesa","orgStateOrProvince":"Odeska oblast",
            "orgPostalCode":"65059","orgJoiState":"Odeska oblast","orgJoiCountry":"UA","orgJoiLocality":"Odesa",
            "assumedName":"Name DBA","businessCategory":"PrivateOrganization","dateOfIncorporation":"1970-01-01",
            "companyNumber":"23459823565"},"domains":[{"name":"domain.ccmqa.com"}]}
         """

        url = f"/acme/{self.version}/account/{id}"
        headers = {"login": self.username, "Accept": "application/json;charset=UTF-8",  "customerUri": self.custom_uri,
                  "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def create_new_acme_account(self, **parameter):
        """ Find ACME account by ID.

        Args:
            name (int): ACME account name [Must not be blank, Size must be between 1 and 128 inclusive]
            acmeServer (str): ACME account name
            organizationId (int): ACME account organization ID [Must be at least 1, Must not be null]
            evDetails.orgName (str): EV organization name [Must not be blank, Size must be between 0 and 128 inclusive]
            evDetails.orgCountry (str): EV organization country [Size must be between 2 and 2 inclusive]
            evDetails.postOfficeBox (str): EV organization post office box [Size must be between 0 and 40 inclusive]
            evDetails.orgAddress1 (str): EV organization address 1 [Size must be between 0 and 128 inclusive]
            evDetails.orgAddress2 (str): EV organization address 2 [Size must be between 0 and 128 inclusive]
            evDetails.orgAddress3 (str): EV organization address 3 [Size must be between 0 and 128 inclusive]
            evDetails.orgLocality (str): EV organization city [Size must be between 0 and 128 inclusive]
            evDetails.orgStateOrProvince (str): EV organization state/province [Size must be between 0 and 128 inclusive]
            evDetails.orgPostalCode (str): EV organization postal code [Size must be between 0 and 40 inclusive]
            evDetails.orgJoiState (str): EV organization state or province of incorporation [Size must be between 0 and  128 inclusive]
            evDetails.orgJoiCountry (str): EV organization country of incorporation [Size must be between 2 and 2 inclusive]
            evDetails.orgJoiLocality (str): EV organization jurisdiction of incorporation city or town [Size must be between 0 and 128 inclusive]
            evDetails.assumedName (str): EV organization business category. Values: [PrivateOrganization, GovernmentEntity, BusinessEntity, NonCommercialEntity] []
            evDetails.dateOfIncorporation (str): EV organization date of incorporation [Size must be between 8 and 8 inclusive]
            evDetails.companyNumber (str): EV organization registration number [Size must be between 0 and 25 inclusive]

        Example:
            {"name":"EV ACME Account","acmeServer":"EV ACME Server","organizationId":1869,
            "evDetails":{"orgName":"org4Test","orgCountry":"UA","postOfficeBox":"PostOfficeBox",
            "orgAddress1":"Deribasovskaya 1","orgAddress2":"Street 2","orgAddress3":"Street 3","orgLocality":"Odesa",
            "orgStateOrProvince":"Odeska oblast","orgPostalCode":"65059","orgJoiState":"Odeska oblast",
            "orgJoiCountry":"UA","orgJoiLocality":"Odesa","assumedName":"Name DBA",
            "businessCategory":"PrivateOrganization","dateOfIncorporation":"1970-01-01","companyNumber":"23459823565"}}

        Returns:
            HTTP/1.1 201 Created
            Location: https://cert-manager.com/api/acme/v1/account/72
        """
        data = parameter

        url = f"/acme/{self.version}/account/"
        headers = {"login": self.username, "Accept": "application/json;charset=UTF-8", "customerUri": self.custom_uri,
                   "password": self.password}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def update_acme_account(self, id: int):
        """ Update ACME account.

        Args:
            id (int): ACME account entity ID
            name (str): ACME account name [Must not be blank, Size must be between 1 and 128 inclusive]

        Example:
            {"name":"EV ACME Account Updated"}

        Example:
            HTTP/1.1 200 OK
        """

        url = f"/acme/{self.version}/account/{id}"
        headers = {"Content-Type": "application/json;charset=UTF-8", "login": self.username,
                   "customerUri": self.custom_uri, "password": self.password}

        response = self.client.put(url, headers=headers)
        return response

    def add_domains_to_acme_account(self, id: int, domains: list):
        """ Add domains to ACME account.

        Args:
            id (int): ACME account entity ID
            domains[] (list): Domains list [Must not be empty]
            domains[].name (str): Domain name [Must not be blank, Size must be between 1 and 1024 inclusive]

        Example:
            {"domains":[{"name":"domain.ccmqa.com"},{"name":"sub.domain.ccmqa.com"}]}

        Returns:
            notAddedDomains[] (list): Domains not added to the ACME account upon update operation

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 40

            {"notAddedDomains":["domain.ccmqa.com"]}
        """
        data = {"domains": domains}

        url = f"/acme/{self.version}/account/{id}/domains"
        headers = {"Content-Type": "application/json;charset=UTF-8", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def remove_domains_from_acme_account(self, id: int, domains: list):
        """ Remove domains from ACME account.

        Args:
            id (int): ACME account entity ID
            domains[] (list): Domains list [Must not be empty]
            domains[].name (str): Domain name [Must not be blank, Size must be between 1 and 1024 inclusive]

        Example:
            {"domains":[{"name":"domain.ccmqa.com.ua"},{"name":"sub.domain.ccmqa.com"}]}

        Returns:
            notAddedDomains[] (list): Domains not added to the ACME account upon update operation

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 45

            {"notRemovedDomains":["domain.ccmqa.com.ua"]}
        """
        data = {"domains": domains}

        url = f"/acme/{self.version}/account/{id}/domains"
        headers = {"Content-Type": "application/json;charset=UTF-8", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.delete(url, headers=headers, data=data)
        return response

    def delete_acme_account(self, id: int):
        """ Delete ACME account.

        Args:
            id (int): ACME account entity ID

        Response-Example:
            HTTP/1.1 204 No Content
        """

        url = f"/acme/{self.version}/account/{id}"
        headers = {"login": self.username, "password": self.password, "customerUri": self.custom_uri}

        response = self.client.delete(url, headers=headers)
        return response

    def list_acme_accounts(self, position: int, size: int, organization_id: int, name: str, acme_server: str,
                           cert_validation_type: str, status: str):
        """ Delete ACME account.

        Args:
            position (int): Position shift
            size (int): Count of entries
            organization_id (int): Organization ID
            name (str): ACME account name
            acme_server (str): ACME account server name
            cert_validation_type (str): ACME account server validation type. Values: [DV, OV, EV]
            status (str): ACME account status

        Returns:
            [] (list): List of ACME accounts
            [].id (int): ACME account entity ID
            [].name (str): ACME account name
            [].status (str): ACME account status
            [].macKey (str): ACME account HMAC key
            [].macId (str): ACME account key ID
            [].acmeServer (str): ACME account server name
            [].organizationId (int): ACME account organization ID
            [].certValidationType (str): ACME account server validation type. Values: [DV, OV, EV]
            [].accountId (str): ACME account ID
            [].ovOrderNumber (int): OV order number
            [].contacts (str): ACME account contacts
            [].evDetails (object): ACME account EV details
            [].domains[] (list): ACME account domains
            [].domains[].name (str): ACME account domain name

        Example:
            [{"id":80,"name":"OV ACME Account","status":"Pending","macKey":"cf44dee6-4fd5-4b9c-a74f-9e637a52d007",
            "macId":"ffc748a3-5994-4d7f-aab1-2838b53688f6","acmeServer":"OV ACME Server","organizationId":1875,
            "certValidationType":"OV","accountId":"ffc748a3-5994-4d7f-aab1-2838b53688f6","ovOrderNumber":1946394478,
            "contacts":"email@ccmqa.com","evDetails":{},
            "domains":[{"name":"domain.ccmqa.com"},{"name":"sub.domain.ccmqa.com"}]}]

        """

        url = f"/acme/{self.version}/account?position={position}&size={size}&organizationID={organization_id}&" \
              f"name={name}&acmeServer={acme_server}&certValidationType={cert_validation_type}&status={status}"
        headers = {"login": self.username, "password": self.password, "customerUri": self.custom_uri}

        response = self.client.get(url, headers=headers)
        return response
