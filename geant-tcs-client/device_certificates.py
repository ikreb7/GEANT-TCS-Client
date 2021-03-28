
import urllib.parse


class DeviceCertificates:
    """ Client resource is used to perform operation on Client Certificates """

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.login = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def device_certificate_types(self, ):
        """ The certain combinations of certificate parameters such as key usage, extended key usage, certificate term
            etc created by the administrators one of which the users with relevant access will have to use for their
            new Device certificate requests.

        Returns:
            [] (List): An array of available DEVICE types
            [].name (str): Name of DEVICE type
            [].id (int): ID of DEVICE type
            [].term (int): Term(days) for DEVICE type
            [].ku[] (List): Key Usages available for the certificate type
            [].eku[] (List): Extended Key Usages available for the certificate type

        Example:
            [{"id":136,"name":"Test device type","term":1,"ku":["Digital Signature"],"eku":["1.3.6.1.5.5.7.3.2"]}]
         """

        url = f"/device/{self.version}/types"
        headers = {"login": self.username, "Accept": "application/json",  "customerUri": self.custom_uri,
                  "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def custom_fields_for_device_certificate(self):
        """ Special fields that enable the administrator to add their own identification reference(s) on the Device
            certificates requested through SCM.

        Returns:
            [] (List): An array of custom fields
            [].name (str): Custom field name
            [].mandatory (bool): Is field mandatory
            [].id (int): Custom field id

        Example:
            [{"id":166,"name":"testName","mandatory":true}]
        """

        url = f"/device/{self.version}/customFields"
        headers = {"Accept": "application/json", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.get(url, headers=headers)
        return response

    def enroll_device_certificate(self, org_id: int, csr: str, cert_type: int, **custom_fields: dict,
                                  **optional_fields: dict):
        """ Creation and submission of a request for a new Device certificate.

        Args:
            org_id (int): Organization ID [Must be at least 1,Must not be null]
            csr (str): Certificate signing request [Must not be null,Size must be between 100 and 2147483647 inclusive]
            cert_type (int): Certificate type ID [Must be at least 1]
            custom_fields[] (List): Custom fields to be applied to requested certificate. Must contain mandatory custom
                                    fields.
            custom_fields[].name (str): Name of an enabled custom field.
            custom_fields[].value (str): Value of the custom field.
	        optional_fields[] (List): Optional fields to be applied to requested certificate
	        optional_fields[].name (str): Name of supported optional field. [Must be one of the following values:
	        [commonName, surname, countryName, localityName, stateOrProvinceName, streetAddress, organizationName,
	        organizationalUnitName, title, description, postalCode, postOfficeBox, telephoneNumber, givenName, initials,
	        emailAddress, DocumentoNacionaldeIdentidad, serialNumber, SIRENE, collectionEmailAddress, rfc822Name,
	        subjectUniqueIdentifier, uniqueIdentifier, PermIdAscentMediaNetSecDept, PermIdAscentMediaEngHomeNet,
	        sAMAccountName, userId, userPrincipalName, unstructuredName, domainComponent, dnsName, servicePrincipalName]
	        optional_fields[].value (str): Value of the optional field.

        Returns:
            orderNumber (int): Order number

        Example:
            {"orderNumber":15420}
        """

        url = f"/device/{self.version}/enroll"
        headers = {"customerUri": self.custom_uri, "login": self.username,
        "Content-Type": "application/json;charset=utf-8", "password": self.password}

        data = {"orgId": org_id, "csr": csr, "certType": cert_type, "customFields": custom_fields,
                "optionalFields": optional_fields}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def collect_device_certificate(self, order_number: int, format_type: str):
        """ Delivering the newly issued Device certificate from CA to the administrator for download.

        Args:
            order_number (int): Certificate ID
            format_type (str): Format type name for certificate. If not specified, PKCS#7 Base64 encoded is default.
                               Allowed values: 'x509' - for Certificate (w/ chain), PEM encoded, 'x509CO' - for
                               Certificate only, PEM encoded, 'base64' - for PKCS#7, PEM encoded, 'bin' - for PKCS#7,
                               'x509IO' - for Root/Intermediate(s) only, PEM encoded, 'x509IOR' - for Intermediate(s)/
                               Root only, PEM encoded, 'pem' - for Certificate (w/ chain), PEM encoded, 'pemco' - for
                               Certificate only, PEM encoded
        """

        url = f"/device/{self.version}/collect/{order_number}/{format_type}"
        headers = {"customerUri": self.custom_uri, "login": self.username, "password": self.password}

        response = self.client.post(url, headers=headers)
        return response

    def revoke_device_certificate_by_order_number(self, order_number: int, reason: str):
        """ Sending a request to CA to add the Device certificate under the particular order number to certificate
            revocation list.

        Args:
            order_number (int): Certificate Order Number
            reason (str)

        :return:
        """

        url = f"/device/{self.version}/revoke/order/{order_number}"
        headers = {"customerUri": self.custom_uri, "Content-Type": "application/json;charset=utf-8",
                   "login": self.username, "password": self.password}
        data = {"reason": reason}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def revoke_device_certificate_by_serial_number(self, serial_number: int, reason: str):
        """ Sending a request to CA to add the Device certificate under the particular serial number to certificate #
            revocation list.

        Args:
            serial_number (int): Certificate Serial Number
            reason (str):
        """

        url = f"/device/{self.version}/revoke/serial/{serial_number}"
        headers = {"login": self.username, "Content-Type": "application/json;charset=utf-8",
                   "customerUri": self.custom_uri, "password": self.password}
        data = {"reason": reason}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def renew_device_certificate_by_order_number(self, order_number: int):
        """ Submission of a request for a new Device certificate using the CSR and parameters of the initial Device
            certificate. The initial certificate is defined by its order number.

        Args:
            order_number (int): Order Number of certificate which you are going to renew.

        Example:
            {"orderNumber":15435}
        """

        url = f"/device/{self.version}/renew/order/{order_number}"
        headers = {"Content-Type": "application/json;charset=utf-8", "customerUri": self.custom_uri,
                   "login": self.username, "password": self.password}

        response = self.client.post(url, headers=headers)
        return response

    def renew_device_certificate_by_serial_number(self, serial_number: int):
        """ Submission of a request for a new Device certificate using the CSR and parameters of the initial Device
            certificate. The initial certificate is defined by its serial number.

        Args:
            serial_number (int): Serial Number of certificate which you are going to renew.

        Example:
            {"orderNumber":15462}
        """

        url = f"/device/{self.version}/renew/serial/{serial_number}"
        headers = {"login": self.username, "Content-Type": "application/json;charset=utf-8",
                   "customerUri": self.custom_uri, "password": self.password}

        response = self.client.post(url, headers=headers)
        return response

    def replace_device_certificate_by_order_number(self, order_number: int, csr: str, reason: str, revoke: bool):
        """ Submission of a request for a replace of a Device certificate using new CSR and the parameters of the
            initial Device certificate. The initial certificate is defined by its order number.

        Args:
            order_number (int): Order Number of certificate which you are going to replace.
            csr (str): Certificate signing request related to new key pair [Must not be empty, Size must be between 100
                       and 2147483647 inclusive]
            reason (str): Short message explaining why certificate needs to be replaced [Must not be empty]
            revoke (bool): Previous certificate will be revoked if true [Must not be null]
        """

        url = f"/device/{self.version}/replace/order/{order_number}"
        headers = {"login": self.username, "Content-Type": "application/json;charset=utf-8",
                   "customerUri": self.custom_uri, "password": self.password}
        data = {"csr": csr, "reason": reason, "revoke": revoke}

        response = self.client.post(url, headers=headers, data=data)
        return response
