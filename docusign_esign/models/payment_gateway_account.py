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


class PaymentGatewayAccount(object):
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
        'display_name': 'str',
        'payment_gateway': 'str',
        'payment_gateway_account_id': 'str',
        'payment_gateway_display_name': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'payment_gateway': 'paymentGateway',
        'payment_gateway_account_id': 'paymentGatewayAccountId',
        'payment_gateway_display_name': 'paymentGatewayDisplayName'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """PaymentGatewayAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_name = None
        self._payment_gateway = None
        self._payment_gateway_account_id = None
        self._payment_gateway_display_name = None
        self.discriminator = None

        setattr(self, "_{}".format('display_name'), kwargs.get('display_name', None))
        setattr(self, "_{}".format('payment_gateway'), kwargs.get('payment_gateway', None))
        setattr(self, "_{}".format('payment_gateway_account_id'), kwargs.get('payment_gateway_account_id', None))
        setattr(self, "_{}".format('payment_gateway_display_name'), kwargs.get('payment_gateway_display_name', None))

    @property
    def display_name(self):
        """Gets the display_name of this PaymentGatewayAccount.  # noqa: E501

          # noqa: E501

        :return: The display_name of this PaymentGatewayAccount.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PaymentGatewayAccount.

          # noqa: E501

        :param display_name: The display_name of this PaymentGatewayAccount.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def payment_gateway(self):
        """Gets the payment_gateway of this PaymentGatewayAccount.  # noqa: E501

          # noqa: E501

        :return: The payment_gateway of this PaymentGatewayAccount.  # noqa: E501
        :rtype: str
        """
        return self._payment_gateway

    @payment_gateway.setter
    def payment_gateway(self, payment_gateway):
        """Sets the payment_gateway of this PaymentGatewayAccount.

          # noqa: E501

        :param payment_gateway: The payment_gateway of this PaymentGatewayAccount.  # noqa: E501
        :type: str
        """

        self._payment_gateway = payment_gateway

    @property
    def payment_gateway_account_id(self):
        """Gets the payment_gateway_account_id of this PaymentGatewayAccount.  # noqa: E501

          # noqa: E501

        :return: The payment_gateway_account_id of this PaymentGatewayAccount.  # noqa: E501
        :rtype: str
        """
        return self._payment_gateway_account_id

    @payment_gateway_account_id.setter
    def payment_gateway_account_id(self, payment_gateway_account_id):
        """Sets the payment_gateway_account_id of this PaymentGatewayAccount.

          # noqa: E501

        :param payment_gateway_account_id: The payment_gateway_account_id of this PaymentGatewayAccount.  # noqa: E501
        :type: str
        """

        self._payment_gateway_account_id = payment_gateway_account_id

    @property
    def payment_gateway_display_name(self):
        """Gets the payment_gateway_display_name of this PaymentGatewayAccount.  # noqa: E501

          # noqa: E501

        :return: The payment_gateway_display_name of this PaymentGatewayAccount.  # noqa: E501
        :rtype: str
        """
        return self._payment_gateway_display_name

    @payment_gateway_display_name.setter
    def payment_gateway_display_name(self, payment_gateway_display_name):
        """Sets the payment_gateway_display_name of this PaymentGatewayAccount.

          # noqa: E501

        :param payment_gateway_display_name: The payment_gateway_display_name of this PaymentGatewayAccount.  # noqa: E501
        :type: str
        """

        self._payment_gateway_display_name = payment_gateway_display_name

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
        if issubclass(PaymentGatewayAccount, dict):
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
        if not isinstance(other, PaymentGatewayAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentGatewayAccount):
            return True

        return self.to_dict() != other.to_dict()
