from twilio.rest.resources.sip.credential_lists import Credentials
from twilio.rest.resources.sip.credential_lists import SipCredentialLists
from twilio.rest.resources.sip.domains import CredentialListMappings
from twilio.rest.resources.sip.domains import IpAccessControlListMappings
from twilio.rest.resources.sip.domains import Domains
from twilio.rest.resources.sip.ip_access_control_lists import IpAddresses
from twilio.rest.resources.sip.ip_access_control_lists import \
    SipIpAccessControlLists


class Sip(object):
    """Holds all the SIP resources."""
    name = "SIP"
    key = "sip"

    def __init__(self, base_uri, client):
        self.uri = "%s/SIP" % base_uri
        self.client = client
        self.domains = Domains(self.uri, client)
        self.credential_lists = SipCredentialLists(self.uri, client)
        self.ip_access_control_lists = SipIpAccessControlLists(
            self.uri,
            client,
        )

    def ip_access_control_list_mappings(self, domain_sid):
        """
        Return a :class:`IpAccessControlListMappings` instance for the
        :class:`Domain` with the given domain_sid
        """
        base_uri = "%s/Domains/%s" % (self.uri, domain_sid)
        return IpAccessControlListMappings(base_uri, self.client)

    def credential_list_mappings(self, domain_sid):
        """
        Return a :class:`CredentialListMappings` instance for the
        :class:`Domain` with the given domain_sid
        """
        base_uri = "%s/Domains/%s" % (self.uri, domain_sid)
        return CredentialListMappings(base_uri, self.client)

    def ip_addresses(self, ip_access_control_list_sid):
        """
        Return a :class:`IpAddresses` instance for the
        :class:`IpAccessControlList` with the given ip_access_control_list_sid
        """
        base_uri = "%s/IpAccessControlLists/%s" % (
            self.uri,
            ip_access_control_list_sid,
        )
        return IpAddresses(base_uri, self.client)

    def credentials(self, credential_list_sid):
        """
        Return a :class:`Credentials` instance for the
        :class:`CredentialList` with the given credential_list_sid
        """
        base_uri = "%s/CredentialLists/%s" % (
            self.uri,
            credential_list_sid,
        )
        return Credentials(base_uri, self.client)
