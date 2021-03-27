
import urllib.parse


class PersonResource:

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.login = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def find_person_id_by_email(self, email: str):
        """ Find person ID by email

        Args:
            email (str): Person e-mail. Must be formatted as valid e-mail string. Also might need to be properly
            encoded as required by URL syntax standard. For example, the '@' character should be replaced with
            the %40 code, '.' - with %2E and so on.

        Returns:
            personId (int): Person ID

        Example:
            {"personId":910}
        """

        email = urllib.parse.quote(email)
        # replace hyphen(%2D), period(%2E),underscore(%5F), or tilde(%7E), see RFC3986
        email = email.replace("-", "%2D").replace(".", "%2E").replace("_", "%5F").replace("~", "%7E")

        url = f"/person/{self.version}/id/byEmail/{email}"
        headers = {"Accept": "application/json", "login": self.username, "customerUri": self.custom_uri,
                   "password": self.password}
        response = self.client.get(url, headers=headers)
        return response

    def find_person_id(self, person_id: int):
        """ Find person by ID

        Args:
            person_id (str): Person ID

        Returns:
            id (int): Person ID
            organizationID (int): Organization ID
            email (str): Person e-mail
            firstName (str): Person firstname
            middleName (str): Person lastname
            lastName (str): Person middlename
            validationType (str): Person validation type. Values: [STANDARD, HIGH]
            phone (str): Person Phone
            commonName (str): Person CommonName
            secondaryEmails (List[str]): Person Secondary Emails

        Example:
            {"id":909,"firstName":"Tester","middleName":"","lastName":"","email":"14375_nobody@nobody.comodo.od.ua",
            "organizationId":10398,"validationType":"STANDARD","phone":"123456789",
            "secondaryEmails":["321nobody@nobody.comodo.od.ua","123@email.com"],"commonName":"Tester"}
        """

        url = f"/person/{self.version}/{person_id}"
        headers = {"Accept": "application/json;charset=UTF-8", "customerUri": self.custom_uri, "login": self.username,
                   "password": self.password}
        response = self.client.get(url, headers=headers)
        return response

    def create_new_person(self, first_name: str, middle_name: str, last_name: str, email: str, validation_type: str,
                          organization_id: int, phone: str, common_name: None, secondary_emails: [str]):
        """ Create new person

        Args:
            first_name (str): Person's first name [Must not be blank, Size must be between 1 and 64 inclusive]
            last_name (str): Person's middle name [Must not be blank, Size must be between 1 and 64 inclusive]
            middle_name (str): Person's last name [Size must be between 0 and 64 inclusive]
            email (str): Person's email [Must be a well-formed email address, Must not be empty, Size must be between 0 and 128 inclusive]
            validation_type (str): Person’s validation type. Values: [STANDARD, HIGH] [Must not be null]
            organization_id (int): Organization ID [Must be at least 1, Must not be null]
            phone (str): Person Phone [Must match the regular expression: [#|0-9|\(|\)|\-|\+| x]*, Size must be between 0 and 32 inclusive]
            common_name (str): Person commonName [Size must be between 0 and 64 inclusive]
            secondary_emails (List[str]): Person Secondary Emails

        Example:
            {"firstName":"First Name","middleName":"Middle Name","lastName":"Last Name","email":"test@email.com",
            "organizationId":10390,"validationType":"STANDARD","phone":"","secondaryEmails":[],"commonName":null}
        """

        data = {"firstName": first_name, "middleName": middle_name, "lastName": last_name, "email": email,
                "organizationId": organization_id, "validationType": validation_type, "phone": phone,
                "secondaryEmails": secondary_emails, "commonName": common_name}

        url = f"/person/{self.version}"
        headers = {"login": self.username, "customerUri": self.custom_uri,
                   "Content-Type": "application/json;charset=UTF-8", "password": self.password}
        response = self.client.post(url, data=data, headers=headers)
        return response

    def update_person(self, person_id: int, first_name: str, middle_name: str, last_name: str, email: str,
                      validation_type: str, organization_id: int, phone: str, common_name: str,
                      secondary_emails: [str]):
        """ Update person

        Args:
            first_name (str): Person's first name [Must not be blank, Size must be between 1 and 64 inclusive]
            middle_name (str): Person's last name [Size must be between 0 and 64 inclusive]
            last_name (str): Person's middle name [Must not be blank, Size must be between 1 and 64 inclusive]
            email (str): Person's email [Must be a well-formed email address, Must not be empty, Size must be between 0 and 128 inclusive]
            validation_type (str): Person’s validation type. Values: [STANDARD, HIGH] [Must not be null]
            organization_id (int): Organization ID [Must be at least 1, Must not be null]
            phone (str): Person Phone [Must match the regular expression: [#|0-9|\(|\)|\-|\+| x]*, Size must be between 0 and 32 inclusive]
            common_name (str): Person commonName [Size must be between 0 and 64 inclusive]
            secondary_emails (List[str]): Person Secondary Emails

        Example:
            {"firstName":"First Name","middleName":"Middle Name","lastName":"Last Name","email":"test@email.com",
            "organizationId":10420,"validationType":"STANDARD","phone":null,
            "secondaryEmails":["321nobody@nobody.comodo.od.ua","123@email.com"],"commonName":null}
        """

        url = f"/person/{self.version}/{person_id}"

        data = {"firstName": first_name, "middleName": middle_name, "lastName": last_name, "email": email,
                "organizationId": organization_id, "validationType": validation_type, "phone": phone,
                "secondaryEmails": secondary_emails, "commonName": common_name}
        headers = {"login": self.username, "customerUri": self.custom_uri,
                   "Content-Type": "application/json;charset=UTF-8", "password": self.password}

        response = self.client.put(url, data=data, headers=headers)
        return response

    def delete_person(self, person_id):
        """ Delete Person

        Args:
            person_id (int): Person ID being deleted

        """

        url = f"/person/{self.version}/{person_id}"
        headers = {"login": self.username, "customerUri": self.custom_uri, "password": self.password}

        response = self.client.delete(url, headers=headers)
        return response

    def list_persons(self, **parameter):
        """ List Person

        Args:
            position (int): Position shift
            size (int): Count of entries
            name (str): Person name (url encoded)
            organization_id (int): Organization ID
            email (str): Person email
            common_name (str): Person commonName
            phone (str): Person phone
            secondary_email (List[str]): Person Secondary Email

        Returns:
            [] (List[Dict]): List of persons
            [].id (int): Person ID
            [].organizationId (int): Organization ID
            [].email (str): Person e-mail
            [].firstName (str): Person firstname
            [].lastname (str): Person lastname
            [].middlename (str): Person middlename
            [].validationTyle (str): Person validation type
            [].phone (str): Person Phone
            [].commonName (str): Person CommonName
            [secondaryEmails (List[str]): Person Secondary Emails

        Example:
            [{"id":913,"firstName":"Tester","middleName":"","lastName":"","email":"14399_nobody@nobody.comodo.od.ua",
            "organizationId":10406,"validationType":"STANDARD","phone":"123456789",
            "secondaryEmails":["321nobody@nobody.comodo.od.ua","123@email.com"],"commonName":"Tester"}]
        """

        url = f"/person/{self.version}/"
        if parameter:
            key, value = parameter.popitem()
            url = f"{url}?{key}={value}"
            for para in parameter:
                url = f"{url}&{para}={parameter[para]}"

        headers = {"customerUri": self.custom_uri, "login": self.username, "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def import_client_certificate_with_private_key(self, person_id: int, p12: str, password: str, custom_fields: [str]):
        """ Import client certificate with private key for person

        Args:
            p12 (str): Base64 encoded pkcs12 file []
            password (str): Password to access pkcs12 file [Optional]
            customFields (List): An array of custom fields if required [Optional]

        Example:
            {"p12": ""MIIc9AIBAzCCHK...KMCAgQA", "password":"11","customFields":[]}

        Returns:
            id (int): ID of created certificate based on imported payload

        """

        url = f"/person/{self.version}/{person_id}/import-key "
        data = {"p12": p12, "password": password, "customFields": custom_fields}
        headers = {"customerUri": self.custom_uri, "Content-Type": "application/json;charset=UTF-8",
                   "login": self.username, "password": self.password}

        response = self.client.post(url, data=data, headers=headers)
        return response
