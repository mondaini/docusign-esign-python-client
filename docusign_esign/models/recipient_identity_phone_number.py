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


class RecipientIdentityPhoneNumber(object):
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
        'country_code': 'str',
        'extension': 'str',
        'number': 'str'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'extension': 'extension',
        'number': 'number'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """RecipientIdentityPhoneNumber - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._country_code = None
        self._extension = None
        self._number = None
        self.discriminator = None

        setattr(self, "_{}".format('country_code'), kwargs.get('country_code', None))
        setattr(self, "_{}".format('extension'), kwargs.get('extension', None))
        setattr(self, "_{}".format('number'), kwargs.get('number', None))

    @property
    def country_code(self):
        """Gets the country_code of this RecipientIdentityPhoneNumber.  # noqa: E501

          # noqa: E501

        :return: The country_code of this RecipientIdentityPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this RecipientIdentityPhoneNumber.

          # noqa: E501

        :param country_code: The country_code of this RecipientIdentityPhoneNumber.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def extension(self):
        """Gets the extension of this RecipientIdentityPhoneNumber.  # noqa: E501

          # noqa: E501

        :return: The extension of this RecipientIdentityPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this RecipientIdentityPhoneNumber.

          # noqa: E501

        :param extension: The extension of this RecipientIdentityPhoneNumber.  # noqa: E501
        :type: str
        """

        self._extension = extension

    @property
    def number(self):
        """Gets the number of this RecipientIdentityPhoneNumber.  # noqa: E501

          # noqa: E501

        :return: The number of this RecipientIdentityPhoneNumber.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this RecipientIdentityPhoneNumber.

          # noqa: E501

        :param number: The number of this RecipientIdentityPhoneNumber.  # noqa: E501
        :type: str
        """

        self._number = number

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
        if issubclass(RecipientIdentityPhoneNumber, dict):
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
        if not isinstance(other, RecipientIdentityPhoneNumber):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecipientIdentityPhoneNumber):
            return True

        return self.to_dict() != other.to_dict()
