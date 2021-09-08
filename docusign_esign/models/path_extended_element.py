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


class PathExtendedElement(object):
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
        'name': 'str',
        'type': 'str',
        'type_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'type_name': 'typeName'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """PathExtendedElement - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._type = None
        self._type_name = None
        self.discriminator = None

        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('type'), kwargs.get('type', None))
        setattr(self, "_{}".format('type_name'), kwargs.get('type_name', None))

    @property
    def name(self):
        """Gets the name of this PathExtendedElement.  # noqa: E501

          # noqa: E501

        :return: The name of this PathExtendedElement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PathExtendedElement.

          # noqa: E501

        :param name: The name of this PathExtendedElement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this PathExtendedElement.  # noqa: E501

          # noqa: E501

        :return: The type of this PathExtendedElement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PathExtendedElement.

          # noqa: E501

        :param type: The type of this PathExtendedElement.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def type_name(self):
        """Gets the type_name of this PathExtendedElement.  # noqa: E501

          # noqa: E501

        :return: The type_name of this PathExtendedElement.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this PathExtendedElement.

          # noqa: E501

        :param type_name: The type_name of this PathExtendedElement.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

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
        if issubclass(PathExtendedElement, dict):
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
        if not isinstance(other, PathExtendedElement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PathExtendedElement):
            return True

        return self.to_dict() != other.to_dict()
