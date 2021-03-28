# GÉANT-TCS-Client (GÉANT Trusted Certificate Service Client)

Work in progress.

# Install

    pip install geant-tcs-client

# Example

    #!/usr/bin/env python
    
    from geant_tcs_client import GEANTTCSClient
    from ssl_certificates import SSLCertificates

    def main():

        client = GEANTTCSClient.connect()
        
        config = {"username": "admin_customer14378", "password": "password123", "custom_uri": "test"}
        ssl_certs = SSLCertificates(config)
        
        print(ssl_certs.listing_ssl_types())
    
    
    if __name__ == '__main__':
        main()

