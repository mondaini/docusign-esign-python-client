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


class OauthAccess(object):
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
        'access_token': 'str',
        'data': 'list[NameValue]',
        'expires_in': 'str',
        'refresh_token': 'str',
        'scope': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'data': 'data',
        'expires_in': 'expires_in',
        'refresh_token': 'refresh_token',
        'scope': 'scope',
        'token_type': 'token_type'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """OauthAccess - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_token = None
        self._data = None
        self._expires_in = None
        self._refresh_token = None
        self._scope = None
        self._token_type = None
        self.discriminator = None

        setattr(self, "_{}".format('access_token'), kwargs.get('access_token', None))
        setattr(self, "_{}".format('data'), kwargs.get('data', None))
        setattr(self, "_{}".format('expires_in'), kwargs.get('expires_in', None))
        setattr(self, "_{}".format('refresh_token'), kwargs.get('refresh_token', None))
        setattr(self, "_{}".format('scope'), kwargs.get('scope', None))
        setattr(self, "_{}".format('token_type'), kwargs.get('token_type', None))

    @property
    def access_token(self):
        """Gets the access_token of this OauthAccess.  # noqa: E501

        Access token information.  # noqa: E501

        :return: The access_token of this OauthAccess.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OauthAccess.

        Access token information.  # noqa: E501

        :param access_token: The access_token of this OauthAccess.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def data(self):
        """Gets the data of this OauthAccess.  # noqa: E501

          # noqa: E501

        :return: The data of this OauthAccess.  # noqa: E501
        :rtype: list[NameValue]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this OauthAccess.

          # noqa: E501

        :param data: The data of this OauthAccess.  # noqa: E501
        :type: list[NameValue]
        """

        self._data = data

    @property
    def expires_in(self):
        """Gets the expires_in of this OauthAccess.  # noqa: E501

          # noqa: E501

        :return: The expires_in of this OauthAccess.  # noqa: E501
        :rtype: str
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this OauthAccess.

          # noqa: E501

        :param expires_in: The expires_in of this OauthAccess.  # noqa: E501
        :type: str
        """

        self._expires_in = expires_in

    @property
    def refresh_token(self):
        """Gets the refresh_token of this OauthAccess.  # noqa: E501

          # noqa: E501

        :return: The refresh_token of this OauthAccess.  # noqa: E501
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """Sets the refresh_token of this OauthAccess.

          # noqa: E501

        :param refresh_token: The refresh_token of this OauthAccess.  # noqa: E501
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def scope(self):
        """Gets the scope of this OauthAccess.  # noqa: E501

        Must be set to \"api\".  # noqa: E501

        :return: The scope of this OauthAccess.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OauthAccess.

        Must be set to \"api\".  # noqa: E501

        :param scope: The scope of this OauthAccess.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def token_type(self):
        """Gets the token_type of this OauthAccess.  # noqa: E501

          # noqa: E501

        :return: The token_type of this OauthAccess.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this OauthAccess.

          # noqa: E501

        :param token_type: The token_type of this OauthAccess.  # noqa: E501
        :type: str
        """

        self._token_type = token_type

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
        if issubclass(OauthAccess, dict):
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
        if not isinstance(other, OauthAccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OauthAccess):
            return True

        return self.to_dict() != other.to_dict()
