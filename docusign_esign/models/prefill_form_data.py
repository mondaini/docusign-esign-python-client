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


class PrefillFormData(object):
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
        'form_data': 'list[FormDataItem]',
        'sender_email': 'str',
        'sender_name': 'str',
        'sender_user_id': 'str'
    }

    attribute_map = {
        'form_data': 'formData',
        'sender_email': 'senderEmail',
        'sender_name': 'senderName',
        'sender_user_id': 'senderUserId'
    }

    def __init__(self, form_data=None, sender_email=None, sender_name=None, sender_user_id=None):  # noqa: E501
        """PrefillFormData - a model defined in Swagger"""  # noqa: E501

        self._form_data = None
        self._sender_email = None
        self._sender_name = None
        self._sender_user_id = None
        self.discriminator = None

        if form_data is not None:
            self.form_data = form_data
        if sender_email is not None:
            self.sender_email = sender_email
        if sender_name is not None:
            self.sender_name = sender_name
        if sender_user_id is not None:
            self.sender_user_id = sender_user_id

    @property
    def form_data(self):
        """Gets the form_data of this PrefillFormData.  # noqa: E501

          # noqa: E501

        :return: The form_data of this PrefillFormData.  # noqa: E501
        :rtype: list[FormDataItem]
        """
        return self._form_data

    @form_data.setter
    def form_data(self, form_data):
        """Sets the form_data of this PrefillFormData.

          # noqa: E501

        :param form_data: The form_data of this PrefillFormData.  # noqa: E501
        :type: list[FormDataItem]
        """

        self._form_data = form_data

    @property
    def sender_email(self):
        """Gets the sender_email of this PrefillFormData.  # noqa: E501

          # noqa: E501

        :return: The sender_email of this PrefillFormData.  # noqa: E501
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this PrefillFormData.

          # noqa: E501

        :param sender_email: The sender_email of this PrefillFormData.  # noqa: E501
        :type: str
        """

        self._sender_email = sender_email

    @property
    def sender_name(self):
        """Gets the sender_name of this PrefillFormData.  # noqa: E501

          # noqa: E501

        :return: The sender_name of this PrefillFormData.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this PrefillFormData.

          # noqa: E501

        :param sender_name: The sender_name of this PrefillFormData.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

    @property
    def sender_user_id(self):
        """Gets the sender_user_id of this PrefillFormData.  # noqa: E501

          # noqa: E501

        :return: The sender_user_id of this PrefillFormData.  # noqa: E501
        :rtype: str
        """
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, sender_user_id):
        """Sets the sender_user_id of this PrefillFormData.

          # noqa: E501

        :param sender_user_id: The sender_user_id of this PrefillFormData.  # noqa: E501
        :type: str
        """

        self._sender_user_id = sender_user_id

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
        if issubclass(PrefillFormData, dict):
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
        if not isinstance(other, PrefillFormData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
