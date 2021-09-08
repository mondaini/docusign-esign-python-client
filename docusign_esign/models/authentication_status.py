# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class AuthenticationStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_code_result': 'EventResult',
        'age_verify_result': 'EventResult',
        'any_social_id_result': 'EventResult',
        'facebook_result': 'EventResult',
        'google_result': 'EventResult',
        'identity_verification_result': 'EventResult',
        'id_lookup_result': 'EventResult',
        'id_questions_result': 'EventResult',
        'linkedin_result': 'EventResult',
        'live_id_result': 'EventResult',
        'ofac_result': 'EventResult',
        'open_id_result': 'EventResult',
        'phone_auth_result': 'EventResult',
        'salesforce_result': 'EventResult',
        'signature_provider_result': 'EventResult',
        'sms_auth_result': 'EventResult',
        's_tan_pin_result': 'EventResult',
        'twitter_result': 'EventResult',
        'yahoo_result': 'EventResult'
    }

    attribute_map = {
        'access_code_result': 'accessCodeResult',
        'age_verify_result': 'ageVerifyResult',
        'any_social_id_result': 'anySocialIDResult',
        'facebook_result': 'facebookResult',
        'google_result': 'googleResult',
        'identity_verification_result': 'identityVerificationResult',
        'id_lookup_result': 'idLookupResult',
        'id_questions_result': 'idQuestionsResult',
        'linkedin_result': 'linkedinResult',
        'live_id_result': 'liveIDResult',
        'ofac_result': 'ofacResult',
        'open_id_result': 'openIDResult',
        'phone_auth_result': 'phoneAuthResult',
        'salesforce_result': 'salesforceResult',
        'signature_provider_result': 'signatureProviderResult',
        'sms_auth_result': 'smsAuthResult',
        's_tan_pin_result': 'sTANPinResult',
        'twitter_result': 'twitterResult',
        'yahoo_result': 'yahooResult'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AuthenticationStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_code_result = None
        self._age_verify_result = None
        self._any_social_id_result = None
        self._facebook_result = None
        self._google_result = None
        self._identity_verification_result = None
        self._id_lookup_result = None
        self._id_questions_result = None
        self._linkedin_result = None
        self._live_id_result = None
        self._ofac_result = None
        self._open_id_result = None
        self._phone_auth_result = None
        self._salesforce_result = None
        self._signature_provider_result = None
        self._sms_auth_result = None
        self._s_tan_pin_result = None
        self._twitter_result = None
        self._yahoo_result = None
        self.discriminator = None

        setattr(self, "_{}".format('access_code_result'), kwargs.get('access_code_result', None))
        setattr(self, "_{}".format('age_verify_result'), kwargs.get('age_verify_result', None))
        setattr(self, "_{}".format('any_social_id_result'), kwargs.get('any_social_id_result', None))
        setattr(self, "_{}".format('facebook_result'), kwargs.get('facebook_result', None))
        setattr(self, "_{}".format('google_result'), kwargs.get('google_result', None))
        setattr(self, "_{}".format('identity_verification_result'), kwargs.get('identity_verification_result', None))
        setattr(self, "_{}".format('id_lookup_result'), kwargs.get('id_lookup_result', None))
        setattr(self, "_{}".format('id_questions_result'), kwargs.get('id_questions_result', None))
        setattr(self, "_{}".format('linkedin_result'), kwargs.get('linkedin_result', None))
        setattr(self, "_{}".format('live_id_result'), kwargs.get('live_id_result', None))
        setattr(self, "_{}".format('ofac_result'), kwargs.get('ofac_result', None))
        setattr(self, "_{}".format('open_id_result'), kwargs.get('open_id_result', None))
        setattr(self, "_{}".format('phone_auth_result'), kwargs.get('phone_auth_result', None))
        setattr(self, "_{}".format('salesforce_result'), kwargs.get('salesforce_result', None))
        setattr(self, "_{}".format('signature_provider_result'), kwargs.get('signature_provider_result', None))
        setattr(self, "_{}".format('sms_auth_result'), kwargs.get('sms_auth_result', None))
        setattr(self, "_{}".format('s_tan_pin_result'), kwargs.get('s_tan_pin_result', None))
        setattr(self, "_{}".format('twitter_result'), kwargs.get('twitter_result', None))
        setattr(self, "_{}".format('yahoo_result'), kwargs.get('yahoo_result', None))

    @property
    def access_code_result(self):
        """Gets the access_code_result of this AuthenticationStatus.  # noqa: E501


        :return: The access_code_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._access_code_result

    @access_code_result.setter
    def access_code_result(self, access_code_result):
        """Sets the access_code_result of this AuthenticationStatus.


        :param access_code_result: The access_code_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._access_code_result = access_code_result

    @property
    def age_verify_result(self):
        """Gets the age_verify_result of this AuthenticationStatus.  # noqa: E501


        :return: The age_verify_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._age_verify_result

    @age_verify_result.setter
    def age_verify_result(self, age_verify_result):
        """Sets the age_verify_result of this AuthenticationStatus.


        :param age_verify_result: The age_verify_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._age_verify_result = age_verify_result

    @property
    def any_social_id_result(self):
        """Gets the any_social_id_result of this AuthenticationStatus.  # noqa: E501


        :return: The any_social_id_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._any_social_id_result

    @any_social_id_result.setter
    def any_social_id_result(self, any_social_id_result):
        """Sets the any_social_id_result of this AuthenticationStatus.


        :param any_social_id_result: The any_social_id_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._any_social_id_result = any_social_id_result

    @property
    def facebook_result(self):
        """Gets the facebook_result of this AuthenticationStatus.  # noqa: E501


        :return: The facebook_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._facebook_result

    @facebook_result.setter
    def facebook_result(self, facebook_result):
        """Sets the facebook_result of this AuthenticationStatus.


        :param facebook_result: The facebook_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._facebook_result = facebook_result

    @property
    def google_result(self):
        """Gets the google_result of this AuthenticationStatus.  # noqa: E501


        :return: The google_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._google_result

    @google_result.setter
    def google_result(self, google_result):
        """Sets the google_result of this AuthenticationStatus.


        :param google_result: The google_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._google_result = google_result

    @property
    def identity_verification_result(self):
        """Gets the identity_verification_result of this AuthenticationStatus.  # noqa: E501


        :return: The identity_verification_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._identity_verification_result

    @identity_verification_result.setter
    def identity_verification_result(self, identity_verification_result):
        """Sets the identity_verification_result of this AuthenticationStatus.


        :param identity_verification_result: The identity_verification_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._identity_verification_result = identity_verification_result

    @property
    def id_lookup_result(self):
        """Gets the id_lookup_result of this AuthenticationStatus.  # noqa: E501


        :return: The id_lookup_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._id_lookup_result

    @id_lookup_result.setter
    def id_lookup_result(self, id_lookup_result):
        """Sets the id_lookup_result of this AuthenticationStatus.


        :param id_lookup_result: The id_lookup_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._id_lookup_result = id_lookup_result

    @property
    def id_questions_result(self):
        """Gets the id_questions_result of this AuthenticationStatus.  # noqa: E501


        :return: The id_questions_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._id_questions_result

    @id_questions_result.setter
    def id_questions_result(self, id_questions_result):
        """Sets the id_questions_result of this AuthenticationStatus.


        :param id_questions_result: The id_questions_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._id_questions_result = id_questions_result

    @property
    def linkedin_result(self):
        """Gets the linkedin_result of this AuthenticationStatus.  # noqa: E501


        :return: The linkedin_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._linkedin_result

    @linkedin_result.setter
    def linkedin_result(self, linkedin_result):
        """Sets the linkedin_result of this AuthenticationStatus.


        :param linkedin_result: The linkedin_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._linkedin_result = linkedin_result

    @property
    def live_id_result(self):
        """Gets the live_id_result of this AuthenticationStatus.  # noqa: E501


        :return: The live_id_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._live_id_result

    @live_id_result.setter
    def live_id_result(self, live_id_result):
        """Sets the live_id_result of this AuthenticationStatus.


        :param live_id_result: The live_id_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._live_id_result = live_id_result

    @property
    def ofac_result(self):
        """Gets the ofac_result of this AuthenticationStatus.  # noqa: E501


        :return: The ofac_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._ofac_result

    @ofac_result.setter
    def ofac_result(self, ofac_result):
        """Sets the ofac_result of this AuthenticationStatus.


        :param ofac_result: The ofac_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._ofac_result = ofac_result

    @property
    def open_id_result(self):
        """Gets the open_id_result of this AuthenticationStatus.  # noqa: E501


        :return: The open_id_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._open_id_result

    @open_id_result.setter
    def open_id_result(self, open_id_result):
        """Sets the open_id_result of this AuthenticationStatus.


        :param open_id_result: The open_id_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._open_id_result = open_id_result

    @property
    def phone_auth_result(self):
        """Gets the phone_auth_result of this AuthenticationStatus.  # noqa: E501


        :return: The phone_auth_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._phone_auth_result

    @phone_auth_result.setter
    def phone_auth_result(self, phone_auth_result):
        """Sets the phone_auth_result of this AuthenticationStatus.


        :param phone_auth_result: The phone_auth_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._phone_auth_result = phone_auth_result

    @property
    def salesforce_result(self):
        """Gets the salesforce_result of this AuthenticationStatus.  # noqa: E501


        :return: The salesforce_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._salesforce_result

    @salesforce_result.setter
    def salesforce_result(self, salesforce_result):
        """Sets the salesforce_result of this AuthenticationStatus.


        :param salesforce_result: The salesforce_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._salesforce_result = salesforce_result

    @property
    def signature_provider_result(self):
        """Gets the signature_provider_result of this AuthenticationStatus.  # noqa: E501


        :return: The signature_provider_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._signature_provider_result

    @signature_provider_result.setter
    def signature_provider_result(self, signature_provider_result):
        """Sets the signature_provider_result of this AuthenticationStatus.


        :param signature_provider_result: The signature_provider_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._signature_provider_result = signature_provider_result

    @property
    def sms_auth_result(self):
        """Gets the sms_auth_result of this AuthenticationStatus.  # noqa: E501


        :return: The sms_auth_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._sms_auth_result

    @sms_auth_result.setter
    def sms_auth_result(self, sms_auth_result):
        """Sets the sms_auth_result of this AuthenticationStatus.


        :param sms_auth_result: The sms_auth_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._sms_auth_result = sms_auth_result

    @property
    def s_tan_pin_result(self):
        """Gets the s_tan_pin_result of this AuthenticationStatus.  # noqa: E501


        :return: The s_tan_pin_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._s_tan_pin_result

    @s_tan_pin_result.setter
    def s_tan_pin_result(self, s_tan_pin_result):
        """Sets the s_tan_pin_result of this AuthenticationStatus.


        :param s_tan_pin_result: The s_tan_pin_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._s_tan_pin_result = s_tan_pin_result

    @property
    def twitter_result(self):
        """Gets the twitter_result of this AuthenticationStatus.  # noqa: E501


        :return: The twitter_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._twitter_result

    @twitter_result.setter
    def twitter_result(self, twitter_result):
        """Sets the twitter_result of this AuthenticationStatus.


        :param twitter_result: The twitter_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._twitter_result = twitter_result

    @property
    def yahoo_result(self):
        """Gets the yahoo_result of this AuthenticationStatus.  # noqa: E501


        :return: The yahoo_result of this AuthenticationStatus.  # noqa: E501
        :rtype: EventResult
        """
        return self._yahoo_result

    @yahoo_result.setter
    def yahoo_result(self, yahoo_result):
        """Sets the yahoo_result of this AuthenticationStatus.


        :param yahoo_result: The yahoo_result of this AuthenticationStatus.  # noqa: E501
        :type: EventResult
        """

        self._yahoo_result = yahoo_result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AuthenticationStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuthenticationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthenticationStatus):
            return True

        return self.to_dict() != other.to_dict()
