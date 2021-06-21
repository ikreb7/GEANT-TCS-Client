
import urllib.parse


class ClientCertificates:
    """ Client resource is used to perform operation on Client Certificates """

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.login = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def listing_client_certificate_types(self):
        """ A GET request will list all of SSL types.

        Returns:
            [] (List): An array of available Client types
            [].name (str): Name of Client type
            [].id (int): ID of Client type
            [].terms (List): An array of term(days) for Client type

        Example:
            [{"id":7786,"name":"Standard Persona Validated Cert","terms":[365,730,1095,1460,1825]},
            {"id":7787,"name":"High Persona Validated Cert","terms":[365,730,1095,1460,1825]}]
         """

        url = f"/smime/{self.version}/types"
        headers = {"login": self.username, "Accept": "application/json",  "customerUri": self.custom_uri,
                  "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def custom_fields_for_client_certificate(self):
        """ Special fields that enable the administrator to add their own identification reference(s) on Client
            certificates requested through SCM.

        Returns:
            [] (List): An array of custom fields
            [].name (str): Custom field name
            [].mandatory (bool): Is field mandatory
            [].id (int): Custom field id

        Example:
            [{"id":167,"name":"testName","mandatory":true}]
        """

        url = f"/smime/{self.version}/customFields"
        headers = {"Accept": "application/json", "customerUri": self.custom_uri, "login": self.username,
                   "password": self.password}
        response = self.client.get(url, headers=headers)
        return response

    def enroll_client_certificate(self, org_id: int, csr: str, cert_type: int, term: int, email: str, phone: str,
                                  secondary_emails: list, first_name: str, middle_name: str, last_name: str,
                                  custom_fields: list):
        """ Creation and submission of a request for a new Client certificate.

        Args:
            org_id (int): Organization ID [Must be at least 1]
            csr (str): Certificate signing request
            cert_type (int): Certificate type ID [Must be at least 1]
            term (int): Certificate validity period in days [Must be at least 1]
            email (str): Person e-mail [Must be a well-formed email address, Must not be empty, Size must be between 0
                         and 128 inclusive]
            phone (str): Person telephone [Must match the regular expression: [#|0-9|\(|\)|\-|\+| x]*, Size must be
                         between 0 and 32 inclusive]
            secondary_emails (List): Person secondary e-mails
            first_name (str): Person first name [firstName must not be empty, firstName + ' ' + middleName + ' ' +
                              lastName must be in range of 1 to 64 characters]
            middle_name (str): Person middle name
            last_name (str): Person last name [lastName must not be empty, firstName + ' ' + middleName + ' ' + lastName
                             must be in range of 1 to 64 characters]
            custom_fields (List): Custom fields to be applied to requested certificate

        Returns:
            orderNumber (int): Order number

        Example:
            {"orderNumber":16180}
        """

        url = f"/smime/{self.version}/enroll"
        headers = {"login": self.username, "Content-Type": "application/json;charset=utf-8",
                   "customerUri": self.custom_uri, "password": self.password}
        data = {"orgId": org_id, "csr": csr, "certType": cert_type, "term": term, "email": email, "phone": phone,
                "secondaryEmails": secondary_emails, "firstName": first_name, "middleName": middle_name,
                "lastName": last_name, "customFields": custom_fields}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def collect_client_certificate(self, order_number: int):
        """ Delivering the newly issued Client certificate from CA to the administrator for download.

        Args:
            order_number (int): Order number
        """

        url = f"/smime/{self.version}/collect/{order_number}"
        headers = {"login": self.username, "customerUri": self.custom_uri, "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def renew_client_certificate_by_order_number(self, order_number: int):
        """ Submission of a request for a new Client certificate using the CSR and parameters of the initial Client
            certificate. The initial certificate is defined by its order number.

        Args:
            order_number (int): Order number. Must be greater than or equal to 1.
        """

        url = f"/smime/{self.version}/renew/order/{order_number}"
        headers = {"Accept": "application/json", "login": self.username, "customerUri": self.custom_uri,
                   "password": self.password}
        response = self.client.get(url, headers=headers)
        return response

    def renew_client_certificate_by_serial_number(self, serial: int):
        """ Submission of a request for a new Client certificate using the CSR and parameters of the initial Client
            certificate. The initial certificate is defined by its serial number.

        Args:
            serial (int): Serial number.
        """

        url = f"/smime/{self.version}/renew/serial/{serial}"
        headers = {"Accept": "application/json", "customerUri": self.custom_uri, "login": self.username,
                   "password": self.password}

        response = self.client.post(url, headers=headers)
        return response

    def replace_client_certificate_by_order_number(self, order_number: int, csr: str, reason: str, revoke: bool):
        """ Submission of a request for a replace of a Client certificate using new CSR and the parameters of the
            initial Client certificate. The initial certificate is defined by its order number.

        Args:
            order_number (int): Order Number of certificate which you are going to replace.
            csr (str): CSR related to new key pair [Must not be empty, Size must be between 100 and 2147483647 inclusive]
            reason (str): Short message explaining why certificate needs to be replaced [Must not be empty, Size must be
                          between 1 and 512 inclusive]
            revoke (bool): Previous certificate will be revoked if true [Must not be null]
        """

        url = f"/smime/{self.version}/replace/order/{order_number}"
        headers = {"customerUri": self.custom_uri,  "Content-Type": "application/json;charset=utf-8",
                   "login": self.username, "password": self.password}
        data = {"csr": csr, "reason": reason, "revoke": revoke}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def revoke_client_certificate_by_order_number(self, order_number: int, reason: str):
        """ Sending a request to CA to add the particular Client certificate in certificate revocation list.

        Args:
            order_number (int): Order number. Must be greater than or equal to 1.
            reason (str):
        """

        url = f"/smime/{self.version}/revoke/order/{order_number}"
        headers = {"Accept": "application/json", "customerUri": self.custom_uri, "login": self.username,
                   "password": self.password}
        data = {"reason": reason}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def revoke_client_certificate_by_serial_number(self, serial_number: int, reason: str):
        """ Sending a request to CA to add the Client certificate under the particular serial number in certificate
            revocation list.

        Args:
            serial_number (int): Order number. Must be greater than or equal to 1.
            reason (str):
        """

        url = f"/smime/{self.version}/revoke/serial/{serial_number}"
        headers = {"Accept": "application/json", "login": self.username, "customerUri": self.custom_uri,
                   "password": self.password}
        data = {"reason": reason}

        response = self.client.get(url, headers=headers, data=data)
        return response

    def revoke_all_client_certificate_related_to_email(self, reason: str, email: str):
        """ Sending a request to CA to add all Client certificates issued for the person with the particular email
            address in certificate revocation list.

        Args:
            reason (str): Short message explaining why certificate needs to be revoked
            email (str): Person e-mail address
        """

        url = f"/smime/{self.version}/revoke"
        headers = {"Accept": "application/json", "customerUri": self.custom_uri,
                   "Content-Type": "application/json;charset=utf-8", "login": self.username, "password": self.password}
        data = {"email": email, "reason": reason}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def list_client_certificates_by_person_id(self, pid: int):
        """ A GET request will return list of all Client certificates for a person with given ID.

        Args:
            pid (int): Person ID. Must be greater than or equal to 1.

        Returns (v2):
            [] (List): An array of Client certificate properties
            [].id (int): Certificate ID
            [].subject (str): Certificate subject
            [].state (str): Certificate state
            [].order_number (int): Certificate order number
            [].serial_number (str): Certificate serial number

        Example:
            [{"id":1,"subject":"S/MIME Subject string","state":"issued",
            "serialNumber":"C3:DB:6F:88:E7:20:DF:99:71:70:59:FB:D0:2D:29:B0","orderNumber":16190}]

        Returns (v1):
            [] (List): An array of Client certificate properties
            [].id (int): Certificate ID
            [].subject (str): Certificate subject
            [].state (str): Certificate state

        Example:
            [{"id":1,"subject":"S/MIME Subject string","state":"issued"}]
        """

        url = f"/smime/{self.version}/byPersonId/{pid}"
        headers = {"Accept": "application/json", "login": self.username, "customerUri": self.custom_uri,
                   "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def list_client_certificates_by_person_email(self, email: str):
        """ A GET request will return list of all Client certificates for a person with given email.

        Args:
            email (str): Person e-mail. Must be formatted as valid e-mail string. Also might need to be properly encoded
                         as required by URL syntax standard. For example, the '@' character should be replaced with the
                         %40 code, '.' - with %2E and so on.

        Returns (v2):
            [] (List): An array of Client certificate properties
            [].id (int): Certificate ID
            [].subject (str): Certificate subject
            [].state (str): Certificate state
            [].orderNumber (int): Certificate order number
            [].serialNumber (str): Certificate serial number

        Example:
            [{"id":1,"subject":"S/MIME Subject string","state":"issued",
            "serialNumber":"C3:DB:6F:88:E7:20:DF:99:71:70:59:FB:D0:2D:29:B0","orderNumber":16190}]

        Returns (v1):
            [] (List): An array of Client certificate properties
            [].id (int): Certificate ID
            [].subject (str): Certificate subject
            [].state (str): Certificate state

        Example:
            [{"id":1,"subject":"S/MIME Subject string","state":"issued"}]
        """

        email = urllib.parse.quote(email)
        # replace hyphen(%2D), period(%2E),underscore(%5F), or tilde(%7E), see RFC3986
        email = email.replace("-", "%2D").replace(".", "%2E").replace("_", "%5F").replace("~", "%7E")

        url = f"/smime/{self.version}/byPersonEmail/{email}"
        headers = {"Accept": "application/json", "login": self.username, "customerUri": self.custom_uri,
                   "password": self.password}

        response = self.client.get(url, headers=headers)
        return response
