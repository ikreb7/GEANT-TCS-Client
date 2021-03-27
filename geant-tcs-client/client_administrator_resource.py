

class ClientAdministratorResource:

    def __init__(self, client, config: dict, version: str = "v1"):
        self.client = client
        self.version = version
        self.login = config.get("username")
        self.password = config.get("password")
        self.custom_uri = config.get("custom_uri")

    def create_client_admin(self, email: str):
        """ Create client admin’s account.

        Args:
            login (str): Login [Must be null or not blank, Must match the regular expression: ^([a-zA-Z0-9@_\.\-\+\'])*, Must not be blank, Size must be between 0 and 128 inclusive]
            email (str): E-Mail [Must be a well-formed email address, Must be null or not blank, Must not be blank]
            forename (str): Forename [Must be null or not blank, Must match the regular expression: ^((?!.*[>|<|!|@|#|\$|\%|\^|\*|\(|\)|~|\?|/|\|\&|\_|\+|=|\"|:|;|,|\{|\}|\[|\]|||`].*).)*$, Must not be blank, Size must be between 0 and 64 inclusive]
            surname (str): [Must be null or not blank, Must match the regular expression: ^((?!.*[>|<|!|@|#|\$|\%|\^|\*|\(|\)|~|\?|/|\|\&|\_|\+|=|\"|:|;|,|\{|\}|\[|\]|||`].*).)*$, Must not be blank, Size must be between 0 and 64 inclusive]
            title (str): Title or Position
            telephone (str): Telephone Number [Must match the regular expression: [#|0-9|\(|\)|\-|\+| x]*]
            street (str): Street Address
            locality (str): Locality
            state (str): State
            post_code (str): Postal Code [Must match the regular expression: ^[a-zA-Z0-9\s-]{0,10}$]
            country (str): Country
            relationship (str): Relationship [Size must be between 0 and 256 inclusive]
            certificateSerialNumber (str): Authentication Certificate Serial Number
            password (str): Password [Must be null or not blank, Must not be blank]
            privileges (List): Privileges
            credentials.[] (List): Credentials [Must not be empty]
            credentials.[].role (str): Role
            credentials.[].orgId (int): Organization Identifier

        Example:
            {"login":"admin","email":"a@a.com","forename":"Admin","surname":"Adminovich","telephone":"+3804821111111",
            "password":"1234","credentials":[{"role":"RAO_SSL","orgId":12299}]}

        Todo:
            * regex input data
        """

        url = f"/person/{self.version}/id/byEmail/{email}"
        headers = {"Accept": "application/json", "customerUri": self.custom_uri,
                   "login": self.username, "Content-Type": "application/json;charset=utf-8", "password": self.password}
        response = self.client.post(url, headers=headers)
        return response

    def update_client_admin(self, id, login: str, email: str, forename: str, surname: str, title: str, telephone: str,
                            street: str, locality: str, state: str, post_code: str, country: str, relationship: str,
                            certificate_serial_number: str, password: str, privileges: str, credentials: list,
                            credentials_role: str, credentials_org_id: int):
        """ Update client admin’s account.

        Args:
            id (int): ID of client admin being updated
            login (str): Login [Must be null or not blank, Must match the regular expression: ^([a-zA-Z0-9@_\.\-\+\'])*, Must not be blank, Size must be between 0 and 128 inclusive]
            email (str): E-Mail [Must be a well-formed email address, Must be null or not blank, Must not be blank]
            forename (str): Forename [Must be null or not blank, Must match the regular expression: ^((?!.*[>|<|!|@|#|\$|\%|\^|\*|\(|\)|~|\?|/|\|\&|\_|\+|=|\"|:|;|,|\{|\}|\[|\]|||`].*).)*$, Must not be blank, Size must be between 0 and 64 inclusive]
            surname (str): [Must be null or not blank, Must match the regular expression: ^((?!.*[>|<|!|@|#|\$|\%|\^|\*|\(|\)|~|\?|/|\|\&|\_|\+|=|\"|:|;|,|\{|\}|\[|\]|||`].*).)*$, Must not be blank, Size must be between 0 and 64 inclusive]
            title (str): Title or Position
            telephone (str): Telephone Number [Must match the regular expression: [#|0-9|\(|\)|\-|\+| x]*]
            street (str): Street Address
            locality (str): Locality
            state (str): State
            post_code (str): Postal Code [Must match the regular expression: ^[a-zA-Z0-9\s-]{0,10}$]
            country (str): Country
            relationship (str): Relationship [Size must be between 0 and 256 inclusive]
            certificate_serial_number (str): Authentication Certificate Serial Number
            password (str): Password [Must be null or not blank, Must not be blank]
            privileges (List): Privileges
            credentials (List): Credentials [Must not be empty]
            credentials_role (str): Role
            credentials_org_id (int): Organization Identifier

        Example:
           {"login":"admin","email":"a@a.com","forename":"Admin","surname":"Adminovich","telephone":"+3804871111111",
           "password":"1234","privileges":["allowCreate","allowDelete","allowEdit"],
           "credentials":[{"role":"RAO_SSL","orgId":12279}]}

        """

        url = f"/admin/{self.version}/{id}"
        headers = {"customerUri": self.custom_uri, "Accept": "application/json", "login": self.username,
                   "Content-Type": "application/json;charset=utf-8", "password": self.password}

        credentials = [{"role": credentials_role, "orgId": credentials_org_id}]
        data = {"login": login, "email": email, "forename": forename, "surname": surname, "telephone": telephone,
                "password": password, "privileges": privileges, "credentials": credentials}

        response = self.client.put(url, headers=headers, data=data)
        return response

    def delete_client_admin(self, id: int):
        """ Delete client admin’s account.

        Args:
            id (int): ID of client admin being deleted
        """

        url = f"/admin/{self.version}/{id}"
        headers = {"login": self.username, "Content-Type": "application/json;charset=utf-8",
                   "customerUri": self.custom_uri, "password": self.password, "Accept": "application/json"}

        response = self.client.delete(url, headers=headers)
        return response

    def get_client_admins_list(self, size: int, **parameter):
        """ Get list of Client Administrators.

        Args:
            size (int): Count of returned entries
            position (int): Position shift
            login (str): Login filter
            email (str): E-mail filter
            status (str): Status filter
            org_id (str): Organization ID filter

        Returns:
            [] (List): Array of requested client admins
            [].id (int): Client admin ID
            [].login (str): Client admin login
            [].email (str): Client admin E-mail
            [].forename (str): Client admin forename
            [].surname (str): Client admin surname

        Example:
            [{"id":12703,"login":"testadmin_customer18160","forename":"client-admin-18166",
            "surname":"client-admin-18166","email":"TestAdmin_Customer18160@aa.com"},
            {"id":12702,"login":"admindrao_customer18160","forename":"client-admin-18164",
            "surname":"client-admin-18164","email":"AdminDrao_Customer18160@aa.com"},
            {"id":12701,"login":"admin_customer18160","forename":"client-admin-18161",
            "surname":"client-admin-18161","email":"Admin_Customer18160@aa.com"}]
        """

        url = f"/admin/{self.version}/"
        if parameter:
            key, value = parameter.popitem()
            url = f"{url}?{key}={value}"
            for para in parameter:
                url = f"{url}&{para}={parameter[para]}"

        headers = {"login": self.username, "customerUri": self.custom_uri, "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def get_client_admin_details(self, id: int):
        """ Get client admin’s details

        Args:
            id (int): ID of client admin whose details are being requested

        Returns:
            id (int): ID
            status (str): Client admin status. Possible values: 'REQUESTED', 'ACTIVE' and 'AWAITING_ME'
            forename (str): Forename
            surename (str): Surname
            login (str): Login
            email (str): Email
            created (str): Client admin creation date
            modified (str): Client admin last modification date
            lastPasswordChange (str): Last password change date
            credentials[] (List): Array of client admin’s roles
            credentials[].role (str): Client admin’s role
            credentials[].orgId (int): Organization ID
            passwordState (str): Client admin’s password state. Possible values: 'ALIVE', 'EXPIRED' and 'NEVER_EXPIRE'
            passwordExpiryDate (str): Expiration date of Client Admin’s password
            activeState (str): Client admin’s active state. Possible values: 'ACTIVE' and 'SUSPENDED'
            failedAttempts (int): Number of failed attempts
            type (str): Client admin account type. Possible values: 'STANDARD', 'IDP_USER' and 'IDP_TEMPLATE'
            privileges (List): Array of client admin’s privileges

        Example:
            {"id":12763,"status":"Active","forename":"client-admin-18284","surname":"client-admin-18284",
            "login":"admindrao_customer18280","email":"AdminDrao_Customer18280@aa.com","created":"2020-01-15",
            "modified":"2020-01-15","lastPasswordChange":"2020-01-15","credentials":[{"role":"DRAO_SSL","orgId":12303}],
            "passwordState":"ALIVE","passwordExpiryDate":"2020-04-14","activeState":"Active",
            "privileges":["allowEdit","allowCreate"],"failedAttempts":0,"type":"Standard"}
        """

        url = f"/admin/{self.version}/{id}/"
        headers = {"Accept": "application/json", "login": self.username, "password": self.password,
                   "customerUri": self.custom_uri}

        response = self.client.get(url, headers=headers)
        return response

    def get_client_admin_roles(self):
        """ Get roles available for client admin

        Returns:
            [] (List): Roles of Client Admin. Possible values: 'MRAO', 'RAO_SSL', 'RAO_SMIME', 'RAO_DEVICE', 'RAO_CS',
                       'DRAO_SSL', 'DRAO_SMIME', 'DRAO_DEVICE', and 'DRAO_CS'

        Example:
            ["MRAO","RAO_SSL","RAO_SMIME","RAO_CS","RAO_DEVICE","DRAO_SSL","DRAO_SMIME","DRAO_CS","DRAO_DEVICE"]
        """

        url = f"/admin/{self.version}/roles"
        headers = {"customerUri": self.custom_uri, "Accept": "application/json", "login": self.username,
                   "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def get_client_admin_privileges(self, **role):
        """ Get privileges available for client admin

        Args:
            role (dict): Client admin’s role. Multiple roles can be provided.

        Returns:
            [].name (str): Privileges for Client Admin. Possible names: 'allowCreate' - Allow creation of peer admin
                           users, 'allowEdit' - Allow editing of peer admin users, 'allowDelete' - Allow deleting of
                           peer admin users, 'allowDCV' - Allow DCV, 'allowSslChanging' - Allow SSL details changing,
                           'allowSslAutoApprove' - Allow SSL auto approve, 'wsApiUseOnly' - WS API use only,
                           'allowMsAdDiscovery' - MS AD Discovery, 'allowKeyVault' - Allow download keys from Key Vault
            [].description (str): Description for privilege.

        Example:
            [{"name":"allowCreate","description":"Allow creation of peer admin users"},{"name":"allowDelete",
            "description":"Allow deleting of peer admin users"},{"name":"allowEdit",
            "description":"Allow editing of peer admin users"},{"name":"allowSslAutoApprove",
            "description":"Allow SSL auto approve"},{"name":"allowSslChanging",
            "description":"Allow SSL details changing"},{"name":"wsApiUseOnly","description":"WS API use only"}]
        """

        url = f"/admin/{self.version}/privileges"
        if role:
            key, value = role.popitem()
            url = f"{url}?{key}={value}"
            for para in role:
                url = f"{url}&{para}={role[para]}"

    def get_password_state(self, state: str, expiration_date: str):
        """ State of Client Admin’s password

        Returns:
            state (str): State of Client Admin. Possible values: 'ALIVE', 'EXPIRED' and 'NEVER_EXPIRE'
            expiration_date (str): Expiration date of Client Admin’s password

        Example:
            {"expirationDate":"2020-04-14","state":"ALIVE"}
        """

        url = f"/admin/{self.version}/password"
        headers = {"Accept": "application/json", "login": self.username, "customerUri": self.custom_uri,
                   "password": self.password}

        response = self.client.get(url, headers=headers)
        return response

    def change_password(self, password: str):
        """ Change of Client Admin’s password. Possible only within a month from expiration.

        Args:
            password (str): Password of Client Admin

        Returns (Failed case):
            code (int): Code of error if error has occurred
            description (str): Error message

        Example:
            {"code":-976,"description":"New password must be between 8 and 32 characters."}
        """

        url = f"/admin/{self.version}/changepassword"
        headers = {"Accept": "application/json", "customerUri": self.custom_uri,
                   "Content-Type": "application/json;charset=UTF-8", "login": self.username,
                   "password": self.password}
        data = {"newPassword": password}

        response = self.client.post(url, headers=headers, data=data)
        return response
