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


class Money(object):
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
        'amount_in_base_unit': 'str',
        'currency': 'str',
        'display_amount': 'str'
    }

    attribute_map = {
        'amount_in_base_unit': 'amountInBaseUnit',
        'currency': 'currency',
        'display_amount': 'displayAmount'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """Money - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount_in_base_unit = None
        self._currency = None
        self._display_amount = None
        self.discriminator = None

        setattr(self, "_{}".format('amount_in_base_unit'), kwargs.get('amount_in_base_unit', None))
        setattr(self, "_{}".format('currency'), kwargs.get('currency', None))
        setattr(self, "_{}".format('display_amount'), kwargs.get('display_amount', None))

    @property
    def amount_in_base_unit(self):
        """Gets the amount_in_base_unit of this Money.  # noqa: E501

          # noqa: E501

        :return: The amount_in_base_unit of this Money.  # noqa: E501
        :rtype: str
        """
        return self._amount_in_base_unit

    @amount_in_base_unit.setter
    def amount_in_base_unit(self, amount_in_base_unit):
        """Sets the amount_in_base_unit of this Money.

          # noqa: E501

        :param amount_in_base_unit: The amount_in_base_unit of this Money.  # noqa: E501
        :type: str
        """

        self._amount_in_base_unit = amount_in_base_unit

    @property
    def currency(self):
        """Gets the currency of this Money.  # noqa: E501

          # noqa: E501

        :return: The currency of this Money.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Money.

          # noqa: E501

        :param currency: The currency of this Money.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def display_amount(self):
        """Gets the display_amount of this Money.  # noqa: E501

          # noqa: E501

        :return: The display_amount of this Money.  # noqa: E501
        :rtype: str
        """
        return self._display_amount

    @display_amount.setter
    def display_amount(self, display_amount):
        """Sets the display_amount of this Money.

          # noqa: E501

        :param display_amount: The display_amount of this Money.  # noqa: E501
        :type: str
        """

        self._display_amount = display_amount

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
        if issubclass(Money, dict):
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
        if not isinstance(other, Money):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Money):
            return True

        return self.to_dict() != other.to_dict()
