
class DomainControlValidationResource:
    """ Any domain added to SCM must pass Domain Control Validation (DCV) before Sectigo can issue certificates to it.
        DCV is a procedure of validation of the Applicant’s control of the domain which needs to appear in the subject
        of the certificate. This resource is used to perform DCV.
    """

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.login = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def start_validation_http(self, domains: str):
        """ Start Domain Control Validation using HTTP method.

        Returns:
            url (str): URL
            first_line (str): First line
            second_line (str): Second line

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 196

            {"url":"http://ccmqa.com/.well-known/pki-validation/EBB6EDA1A4B685CED6E0CBF28AD336DC.txt",
            "firstLine":"d889535bd9fd75a0cd261c48d2ba45636faa8fe57846be24e055e1c0094a9acb","secondLine":"sectigo.com"}
         """
        data = {"domain": domains}

        url = f"/dcv/{self.version}/validation/start/domain/http"
        headers = {"Content-Type": "application/json;charset=utf-8", "login": self.username,
                   "customerUri": self.custom_uri, "password": self.password}

        response = self.client.post(url, headers=headers)
        return response

    def start_validation_https(self, domains: str):
        """ Start Domain Control Validation using HTTPS method.

        Returns:
            url (str): URL
            first_line (str): First line
            second_line (str): Second line

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 197

            {"url":"http://ccmqa.com/.well-known/pki-validation/EBB6EDA1A4B685CED6E0CBF28AD336DC.txt",
            "firstLine":"d889535bd9fd75a0cd261c48d2ba45636faa8fe57846be24e055e1c0094a9acb","secondLine":"sectigo.com"}
         """
        data = {"domain": domains}

        url = f"/dcv/{self.version}/validation/start/domain/https"
        headers = {"Content-Type": "application/json;charset=utf-8", "login": self.username,
                   "customerUri": self.custom_uri, "password": self.password}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def start_validation_cname(self, domains: str):
        """ Start DomStart Domain Control Validation using CName method.

        Returns:
            host (str): Host
            point (str): Point

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 144

            {"host":"_ebb6eda1a4b685ced6e0cbf28ad336dc.ccmqa.com.",
            "point":"d889535bd9fd75a0cd261c48d2ba4563.6faa8fe57846be24e055e1c0094a9acb.sectigo.com."}
         """
        data = {"domain": domains}

        url = f"/dcv/{self.version}/validation/start/domain/https"
        headers = {"Content-Type": "application/json;charset=utf-8", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def submit_validation_http(self, domain: str):
        """ Submit a request for Domain Control Validation using HTTP method.

        Args:
            domain (str): Domain to validate [Must not be empty, Size must be between 0 and 255 inclusive]

        Returns:
            orderStatus (str): Order status
            message (str): Message
            status (str): Status

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 119

            {"status":"NOT_VALIDATED","orderStatus":"SUBMITTED","message":"DCV status: Not Validated;
            DCV order status: Submitted"}
         """
        data = {"domain": domain}

        url = f"/dcv/{self.version}/validation/submit/domain/https"
        headers = {"Content-Type": "application/json;charset=utf-8", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def submit_validation_https(self, domain: str):
        """ Submit a request for Domain Control Validation using HTTPS method.

        Args:
            domain (str): Domain to validate [Must not be empty, Size must be between 0 and 255 inclusive]

        Returns:
            orderStatus (str): Order status
            message (str): Message
            status (str): Status

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 119

            {"status":"NOT_VALIDATED","orderStatus":"SUBMITTED","message":"DCV status: Not Validated;
            DCV order status: Submitted"}
         """
        data = {"domain": domain}

        url = f"/dcv/{self.version}/validation/submit/domain/https"
        headers = {"Content-Type": "application/json;charset=utf-8", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def submit_validation_cname(self, domain: str):
        """ Submit a request for Domain Control Validation using CName method.

        Args:
            domain (str): Domain to validate [Must not be empty, Size must be between 0 and 255 inclusive]

        Returns:
            orderStatus (str): Order status
            message (str): Message
            status (str): Status

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 119

            {"status":"NOT_VALIDATED","orderStatus":"SUBMITTED","message":"DCV status: Not Validated;
            DCV order status: Submitted"}
         """
        data = {"domain": domain}

        url = f"/dcv/{self.version}/validation/submit/domain/cname"
        headers = {"Content-Type": "application/json;charset=utf-8", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def submit_validation_email(self, domain: str):
        """ Submit a request for Domain Control Validation using Email method.

        Args:
            domain (str): Domain to validate [Must not be empty, Size must be between 0 and 255 inclusive]

        Returns:
            orderStatus (str): Order status
            message (str): Message
            status (str): Status

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 119

            {"status":"NOT_VALIDATED","orderStatus":"SUBMITTED","message":"DCV status: Not Validated;
            DCV order status: Submitted"}
         """
        data = {"domain": domain}

        url = f"/dcv/{self.version}/validation/submit/domain/email"
        headers = {"Content-Type": "application/json;charset=utf-8", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def get_validation_status(self, domain: str):
        """ Obtain the result of Domain Control Validation procedure as a validation status of the subject domain.

        # TODO V1 and V2 switch

        Args:
            domain (str): Domain which status is requested [Must not be empty, Size must be between 0 and 255 inclusive]

        Returns:
            status (str): Validation status
            orderStatus (str): Validation order status
            expiration_date (str): Validation expiration date


        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 119

            {"status":"NOT_VALIDATED","orderStatus":"SUBMITTED","message":"DCV status: Not Validated;
            DCV order status: Submitted"}
         """
        data = {"domain": domain}

        url = f"/dcv/{self.version}/validation/status"
        headers = {"Content-Type": "application/json;charset=utf-8", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.post(url, headers=headers, data=data)
        return response

    def search_domains(self, position: int, size: int, domain: str, org: int, department: int, dcv_status: str,
                       order_status: str, expires_in: int):
        """ Obtain the result of Domain Control Validation procedure as a validation statuses.

        Args:
            position (int): Position shift
            size (int): Count of entries
            domain (str): Count of entries
            org (int): Organization ID # TODO could be empty? See org=&
            department (int): Department ID
            dcv_status (str): DCV Status
            order_status (str): DCV Order status
            expires_in (int): Expires in (days)

        Returns:
            [] (list): Array of DCV domains
            [].domain (str): Domain
            [].dcvStatus (str): DCV Status
            [].dcvOrderStatus (str): DCV Order status
            [].dcvMethod (str): DCV Method

        Example:
            HTTP/1.1 200 OK
            Content-Type: application/json
            Content-Length: 102

            [{"domain":"ccmqa.com","dcvStatus":"NOT_VALIDATED","dcvOrderStatus":"NOT_INITIATED","dcvMethod":null}]
         """

        url = f"/dcv/{self.version}/validation?size={size}&position={position}&domain={domain}&org={org}&" \
              f"department={department}&dcvStatus={dcv_status}&orderStatus={order_status}&expiresIn={expires_in}"
        headers = {"login": self.username, "password": self.password,
                   "customerUri": self.custom_uri, "Accept": "application/json"}

        response = self.client.get(url, headers=headers)
        return response