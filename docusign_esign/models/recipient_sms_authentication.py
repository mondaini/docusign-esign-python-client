# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class RecipientSMSAuthentication(object):
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
        'sender_provided_numbers': 'list[str]',
        'sender_provided_numbers_metadata': 'PropertyMetadata'
    }

    attribute_map = {
        'sender_provided_numbers': 'senderProvidedNumbers',
        'sender_provided_numbers_metadata': 'senderProvidedNumbersMetadata'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientSMSAuthentication - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._sender_provided_numbers = None
        self._sender_provided_numbers_metadata = None
        self.discriminator = None

        setattr(self, "_{}".format('sender_provided_numbers'), kwargs.get('sender_provided_numbers', None))
        setattr(self, "_{}".format('sender_provided_numbers_metadata'), kwargs.get('sender_provided_numbers_metadata', None))

    @property
    def sender_provided_numbers(self):
        """Gets the sender_provided_numbers of this RecipientSMSAuthentication.  # noqa: E501

        An Array containing a list of phone numbers the recipient may use for SMS text authentication.   # noqa: E501

        :return: The sender_provided_numbers of this RecipientSMSAuthentication.  # noqa: E501
        :rtype: list[str]
        """
        return self._sender_provided_numbers

    @sender_provided_numbers.setter
    def sender_provided_numbers(self, sender_provided_numbers):
        """Sets the sender_provided_numbers of this RecipientSMSAuthentication.

        An Array containing a list of phone numbers the recipient may use for SMS text authentication.   # noqa: E501

        :param sender_provided_numbers: The sender_provided_numbers of this RecipientSMSAuthentication.  # noqa: E501
        :type: list[str]
        """

        self._sender_provided_numbers = sender_provided_numbers

    @property
    def sender_provided_numbers_metadata(self):
        """Gets the sender_provided_numbers_metadata of this RecipientSMSAuthentication.  # noqa: E501


        :return: The sender_provided_numbers_metadata of this RecipientSMSAuthentication.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._sender_provided_numbers_metadata

    @sender_provided_numbers_metadata.setter
    def sender_provided_numbers_metadata(self, sender_provided_numbers_metadata):
        """Sets the sender_provided_numbers_metadata of this RecipientSMSAuthentication.


        :param sender_provided_numbers_metadata: The sender_provided_numbers_metadata of this RecipientSMSAuthentication.  # noqa: E501
        :type: PropertyMetadata
        """

        self._sender_provided_numbers_metadata = sender_provided_numbers_metadata

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
        if issubclass(RecipientSMSAuthentication, dict):
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
        if not isinstance(other, RecipientSMSAuthentication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientSMSAuthentication):
            return True

        return self.to_dict() != other.to_dict()
