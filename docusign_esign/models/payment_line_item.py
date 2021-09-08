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


class PaymentLineItem(object):
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
        'amount_reference': 'str',
        'description': 'str',
        'item_code': 'str',
        'name': 'str'
    }

    attribute_map = {
        'amount_reference': 'amountReference',
        'description': 'description',
        'item_code': 'itemCode',
        'name': 'name'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """PaymentLineItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount_reference = None
        self._description = None
        self._item_code = None
        self._name = None
        self.discriminator = None

        setattr(self, "_{}".format('amount_reference'), kwargs.get('amount_reference', None))
        setattr(self, "_{}".format('description'), kwargs.get('description', None))
        setattr(self, "_{}".format('item_code'), kwargs.get('item_code', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))

    @property
    def amount_reference(self):
        """Gets the amount_reference of this PaymentLineItem.  # noqa: E501

          # noqa: E501

        :return: The amount_reference of this PaymentLineItem.  # noqa: E501
        :rtype: str
        """
        return self._amount_reference

    @amount_reference.setter
    def amount_reference(self, amount_reference):
        """Sets the amount_reference of this PaymentLineItem.

          # noqa: E501

        :param amount_reference: The amount_reference of this PaymentLineItem.  # noqa: E501
        :type: str
        """

        self._amount_reference = amount_reference

    @property
    def description(self):
        """Gets the description of this PaymentLineItem.  # noqa: E501

          # noqa: E501

        :return: The description of this PaymentLineItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentLineItem.

          # noqa: E501

        :param description: The description of this PaymentLineItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def item_code(self):
        """Gets the item_code of this PaymentLineItem.  # noqa: E501

          # noqa: E501

        :return: The item_code of this PaymentLineItem.  # noqa: E501
        :rtype: str
        """
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        """Sets the item_code of this PaymentLineItem.

          # noqa: E501

        :param item_code: The item_code of this PaymentLineItem.  # noqa: E501
        :type: str
        """

        self._item_code = item_code

    @property
    def name(self):
        """Gets the name of this PaymentLineItem.  # noqa: E501

          # noqa: E501

        :return: The name of this PaymentLineItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentLineItem.

          # noqa: E501

        :param name: The name of this PaymentLineItem.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(PaymentLineItem, dict):
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
        if not isinstance(other, PaymentLineItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentLineItem):
            return True

        return self.to_dict() != other.to_dict()
