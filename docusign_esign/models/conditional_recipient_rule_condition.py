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


class ConditionalRecipientRuleCondition(object):
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
        'filters': 'list[ConditionalRecipientRuleFilter]',
        'order': 'str',
        'recipient_label': 'str'
    }

    attribute_map = {
        'filters': 'filters',
        'order': 'order',
        'recipient_label': 'recipientLabel'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ConditionalRecipientRuleCondition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._filters = None
        self._order = None
        self._recipient_label = None
        self.discriminator = None

        setattr(self, "_{}".format('filters'), kwargs.get('filters', None))
        setattr(self, "_{}".format('order'), kwargs.get('order', None))
        setattr(self, "_{}".format('recipient_label'), kwargs.get('recipient_label', None))

    @property
    def filters(self):
        """Gets the filters of this ConditionalRecipientRuleCondition.  # noqa: E501

          # noqa: E501

        :return: The filters of this ConditionalRecipientRuleCondition.  # noqa: E501
        :rtype: list[ConditionalRecipientRuleFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ConditionalRecipientRuleCondition.

          # noqa: E501

        :param filters: The filters of this ConditionalRecipientRuleCondition.  # noqa: E501
        :type: list[ConditionalRecipientRuleFilter]
        """

        self._filters = filters

    @property
    def order(self):
        """Gets the order of this ConditionalRecipientRuleCondition.  # noqa: E501

          # noqa: E501

        :return: The order of this ConditionalRecipientRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ConditionalRecipientRuleCondition.

          # noqa: E501

        :param order: The order of this ConditionalRecipientRuleCondition.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def recipient_label(self):
        """Gets the recipient_label of this ConditionalRecipientRuleCondition.  # noqa: E501

          # noqa: E501

        :return: The recipient_label of this ConditionalRecipientRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._recipient_label

    @recipient_label.setter
    def recipient_label(self, recipient_label):
        """Sets the recipient_label of this ConditionalRecipientRuleCondition.

          # noqa: E501

        :param recipient_label: The recipient_label of this ConditionalRecipientRuleCondition.  # noqa: E501
        :type: str
        """

        self._recipient_label = recipient_label

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
        if issubclass(ConditionalRecipientRuleCondition, dict):
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
        if not isinstance(other, ConditionalRecipientRuleCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionalRecipientRuleCondition):
            return True

        return self.to_dict() != other.to_dict()
