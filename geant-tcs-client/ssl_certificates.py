

class SSLCertificates:

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.login = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def listing_ssl_certificates(self, **parameter):  # TODO
        """ Create client admin’s account.

        Args:
            size (int): Count of returned entries
            position (int): Position shift
            commonName (str): Common Name filter
            subjectAlternativeName (str): Subject Alternative Name filter
            status (str): Status filter. Possible values: 'Invalid', 'Requested', 'Approved', 'Declined', 'Applied',
                          'Issued', 'Revoked', 'Expired', 'Replaced', 'Rejected', 'Unmanaged', 'SAApproved', 'Init'
            discoveryStatus (str): Discovery status filter. Possible values: 'NotDeployed', 'Deployed'
            vendor (str): Vendor filter
            orgId (str): Organization ID filter
            installStatus (str): Install status filter. Possible values: 'NOT_SCHEDULED', 'SCHEDULED', 'STARTED',
                                 'SUCCESSFUL', 'FAILED'
            renewalStatus (str): Renewal status filter. Possible values: 'NOT_SCHEDULED', 'SCHEDULED', 'STARTED',
                                 'SUCCESSFUL', 'FAILED'
            issuer (str): Issuer filter
            serialNumber (str): Serial Number filter
            requester (str): Requester filter
            externalRequester (str): External Requester filter
            signatureAlgorithm (str): Signature Algorithm filter
            keyAlgorithm (str): Key Algorithm filter
            keySize (str): Key Size filter
            sha1Hash (str): SHA1 Hash filter
            md5Hash (str): MD5 Hash filter
            keyUsage (str): Key Usage filter
            extendedKeyUsage (str): Extended Key Usage filter
            requestedVia (str): Requested Via filter. Possible values: 'WEB_FORM', 'CLIENT_ADMIN', 'API', 'DISCOVERY',
                                'IMPORTED', 'SCEP', 'CD_AGENT', 'MS_AGENT', 'MS_CA', 'BULK_REQUEST', 'ACME'

        Returns:
            [] (List): Array of requested ssls
            [].sslId (int): SSL ID
            [].commonName (str): SSL Common Name
            [].subjectAlternativeNames (List): SSL Subject Alternative Names
            [].serialNumber (str): SSL Serial Number

        Example:
            [{"sslId":2417,"commonName":"ccmqa.com"}]
        """

        url = f"/ssl/{self.version}/"
        headers = {"login": self.username, "Content-Type": "application/json",  "customerUri": self.custom_uri,
                   "password": self.password}
        # TODO data ?
        response = self.client.get(url, headers=headers)
        return response

    def listing_ssl_types(self):
        """ List all of SSL types.

        Returns:
            [] (List): An array of available SSL types
            [].name (str): Name of SSL type
            [].id (int): ID of SSL type
            [].terms (List): An array of term(days) for SSL type

        Example:
            [{"id":17973,"name":"EV","terms":[365]}]
        """

        url = f"/ssl/{self.version}/types"
        headers = {"customerUri": self.custom_uri, "Content-Type": "application/json", "login": self.username,
                   "password": self.password}
        response = self.client.get(url, headers=headers)
        return response

    def listing_of_custom_fields_for_ssl(self):
        """ List all of custom fields defined for SSL certificates.

        Returns:
            [] (List): An array of custom fields
            [].name (str): Custom field name
            [].mandatory (bool): Is field mandatory
            [].id (int): Custom field id

        Example:
            [{"id":161,"name":"testName","mandatory":true}]
        """

        url =f"/ssl/{self.version}/customFields"
        headers = {"Accept": "application/json", "login": self.username, "customerUri": self.custom_uri,
                   "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def enroll_ssl_certificate(self, org_id: int, csr, str, subj_alt_names: str, cert_type, number_servers,
                               server_type: int, term: int, comments: str, custom_fields: list,external_requester: str):
        """ Creation and submission of a request for a new SSL certificate.

        Args:
            org_id (int): Organization ID [Must be at least 1,Must not be null]
            csr (str): Certificate signing request [Must not be empty,Size must be between 100 and 2147483647 inclusive]
            subj_alt_names (str): Subject alternative names(comma separated)
            cert_type (int): Certificate type ID
            number_servers (int): Number of Server Licenses. Required for the Wildcard products
            server_type (int): Server type ID [Must be at least 1]
            term (int): Certificate validity period in days [Must be at least 1]
            comments (str): Comments for enroll request [Size must be between 0 and 1024 inclusive]
            custom_fields[] (List): Custom fields to be applied to requested certificate. Must contain mandatory custom
                                    fields.
            custom_fields.name (str): Name of an enabled custom field.
            custom_fields.value (str): Value of the custom field.
            external_requester (str): External Requester. Acceptable format: 'email@domain.com' or 'email1@domain.com,
                                      email2@domain.com' [Size must be between 0 and 512 inclusive]

        Example:
            {"orgId":10557,"subjAltNames":"ccmqa.com","certType":17945,"numberServers":0,"serverType":-1,
            "term":365,"comments":"test","externalRequester":"","customFields":[{"name":"custom field",
            "value":"custom field value"}],"csr":"-----BEGIN CERTIFICATE REQUEST-----\n
            MIIC4jCCAc73.....LWcttIxyWnYgxvwaWX4lfx9A==\n-----END CERTIFICATE REQUEST-----"}

        Returns:
            renewID (str)
            sslId (int)

        Example:
            {"renewId":"3DE7BTmxvkiCGyNa2czs","sslId":2414}
        """

        url = f"/ssl/{self.version}/enroll"
        headers = {"login": self.username, "Content-Type": "application/json", "password": self.password,
                   "customerUri": self.custom_uri}

        data = {"orgId": org_id, "csr": csr, "subjAltNames": subj_alt_names, "certType": cert_type,
                "numberServers": number_servers, "serverType": server_type, "term": term, "comments": comments,
                "customFields": custom_fields, "externalRequester": external_requester}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def enroll_ssl_certificate_with_key_generation(self, org_id: str, common_name: str, subj_alt_names: str,
                                                   cert_type: int, number_servers: int, server_type: int,
                                                   term: int, comments: str, algorithm: str, key_size: int,
                                                   pass_phrase: str, custom_fields: list, external_requester: str):
        """ Creation and submission of a request for a new SSL certificate with generated keypair. Private key will
            be stored inside 'Private Keys Store'.

        Args:
            org_id (int): Organization ID [Must be at least 1,Must not be null]
            common_name (str): Certificate common name [Must not be null,Size must be between 1 and 64 inclusive]
            subj_alt_names (str): Subject alternative names(comma separated)
            cert_type (int): Certificate type ID
            number_servers (int): Number of Server Licenses. Required for the Wildcard products
            server_type (int): Server type ID [Must be at least 1]
            term (int): Certificate validity period in days [Must be at least 1]
            comments (str): Comments for enroll request [Size must be between 0 and 1024 inclusive]
            algorithm (str): Keypair algorithm [Possible values: RSA]
            key_size (int): Keypair key size [Applied only in case keypair algorithm is specified.
                            Possible values: [2048, 4096]]
            pass_phrase (str): Password to protect PKCS#12 certificate. [Size must be between 8 and 32 inclusive]
            custom_fields[] (List): Custom fields to be applied to requested certificate. Must contain mandatory custom
                                    fields.
            custom_fields.name (str): Name of an enabled custom field.
            custom_fields.value (str): Value of the custom field.
            external_requester (str): External Requester. Acceptable format: 'email@domain.com' or 'email1@domain.com,
                                      email2@domain.com' [Size must be between 0 and 512 inclusive]

        Example:
              {"orgId":10559,"subjAltNames":"ccmqa.com","certType":17951,"numberServers":0,"serverType":-1,"term":365,
              "comments":"test","externalRequester":"","customFields":[{"name":"custom field",
              "value":"custom field value"}],"commonName":"ccmqa.com","passPhrase":"password","keySize":2048,
              "algorithm":"RSA"}

        Returns:
            renewID (str)
            sslId (int)

        Example:
            {"renewId":"qIA9MwZk1cDjJqbHp3Oi","sslId":2415}
        """

        url = f"/ssl/{self.version}/enroll-keygen"
        headers = {"customerUri": self.custom_uri, "login": self.username, "Content-Type": "application/json",
                   "password": self.password}

        data = {"orgId": org_id, "commonName": common_name, "subjAltNames": subj_alt_names, "certType": cert_type,
                "numberServers": number_servers, "serverType": server_type, "term": term, "comments": comments,
                "algorithm": algorithm, "keySize": key_size, "passPhrase": pass_phrase, "customFields": custom_fields,
                "externalRequester": external_requester}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def link_to_download_private_key_or_whole_certificate(self, ssl_id: int, format_type: str):
        """ Generation of a link to download private key or entire certificate from Private Key Controller. You will
            need to have enabled authentication certificate to have access to the Private Key Store in order to
            download SSL certificate and the private key.

            This API method requires the User Login via Certificate authentication style.

        Args:
            ssl_id (int): SSL id for which the link will be generated. Positive integer value. Min value 1
            format_type (str): Parameter to specify download format: key only or entire certificate. Possible
            values: 'key' - for Private Key, Base64 encoded, 'p12' - for PKCS#12, Base64 encoded

        Returns:
            link (str)

        Example:
            {"link":"https:/download?token=5NOALU79DN46UBN8CB0PLJFHR1&keyformat=P12"}
        """

        url = f"/ssl/{self.version}/keystore/{ssl_id}/{format_type}"
        headers = {"customerUri": self.custom_uri, "login": self.username, "Content-Type": "application/json",
                   "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def collect_ssl_certificate(self, ssl_id: int, format_type: str):
        """ Delivering the newly issued SSL certificate from CA to the administrator for download.

        Args:
            ssl_id (int): Certificate ID. Positive integer value. Min value 1
            format_type (str): Format type for certificate. Allowed values: 'x509' - for Certificate (w/ chain), PEM
                             encoded, 'x509CO' - for Certificate only, PEM encoded, 'base64' - for PKCS#7, PEM encoded,
                             'bin' - for PKCS#7, 'x509IO' - for Root/Intermediate(s) only, PEM encoded, 'x509IOR' - for
                             Intermediate(s)/Root only, PEM encoded, 'pem' - for Certificate (w/ chain), PEM encoded,
                             'pemco' - for Certificate only, PEM encoded
        """

        url = f"/ssl/{self.version}/collect/{ssl_id}/{format_type}"
        headers = {"customerUri": self.custom_uri, "login": self.username, "password": self.password}
        response = self.client.get(url, headers=headers)
        return response

    def revoke_ssl_certificate_by_id(self, ssl_id: int, reason: str):
        """ Sending a request to CA to add the particular SSL certificate in certificate revocation list.

        Args:
            ssl_id (int): Certificate ID
            reason (str): Short message with a reason why certificate needs to be revoked [Must not be empty, Size
                          must be between 0 and 512 inclusive]
        """

        url = f"/ssl/{self.version}/revoke/{ssl_id}"
        headers = {"customerUri": self.custom_uri, "Content-Type": "application/json", "login": self.username,
                   "password": self.password}
        data = {"reason": reason}
        response = self.client.get(url, headers=headers, data=data)
        return response

    def revoke_ssl_certificate_by_serial_number(self, serial_number: int, reason: str):
        """ Sending a request to CA to add the particular SSL certificate in certificate revocation list.

        Args:
            serial_number (int): Serial Number of certificate
            reason (str): Short message with a reason why certificate needs to be revoked [Must not be empty, Size must
                          be between 0 and 512 inclusive]
        """

        url = f"/ssl/{self.version}/revoke/serial/{serial_number}"
        headers = {"login": self.username, "Content-Type": "application/json", "customerUri": self.custom_uri,
                   "password": self.password}
        data = {"reason": reason}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def renew_ssl_certificate_by_renew_id(self, renew_id: int, reason: str):
        """
        Args:
            renew_id (int): Renew ID for certificate. Max length 20 symbols
            reason (str)
        """

        url = f"/ssl/{self.version}/renew/{renew_id}"
        headers = {"login": self.username, "Content-Type": "application/json", "customerUri": self.custom_uri,
                   "password": self.password}
        data = {"reason": reason}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def renew_ssl_certificate_by_id(self, ssl_id: int, csr: str, reason: str, common_name: str,
                                    subject_alternative_names: list):
        """
        Args:
            ssl_id (int): Certificate ID. Positive integer value. Min value 1.
            csr (str): Certificate singing request [Must not be empty, Size must be between 100 and 2147483647 inclusive]
            reason (str): Short message with a reason why certificate needs to be replaced [Must not be empty]
            common_name (str): Certificate common name [Size must be between 1 and 64 inclusive]
            subject_alternative_names (List): Array of subject alternative names

        Example:
            {"csr":"-----BEGIN CERTIFICATE REQUEST-----\nMIIC4jCCAc.....X4lfx9A==\n-----END CERTIFICATE REQUEST-----",
            "reason":"test","commonName":"ccmqa.com","subjectAlternativeNames":["mafia.od.ua"]}
        """

        url = f"/ssl/{self.version}/replace/{ssl_id}"
        headers = {"login": self.username, "Content-Type": "application/json", "password": self.password,
                   "customerUri": self.custom_uri}
        data = {"csr": csr, "reason": reason, "commonName": common_name,
                "subjectAlternativeNames": subject_alternative_names}

        response = self.client.post(url, headers=headers, data=data)
        return response
