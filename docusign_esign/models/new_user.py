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


class NewUser(object):
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
        'api_password': 'str',
        'created_date_time': 'str',
        'email': 'str',
        'error_details': 'ErrorDetails',
        'membership_id': 'str',
        'permission_profile_id': 'str',
        'permission_profile_name': 'str',
        'uri': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'user_status': 'str'
    }

    attribute_map = {
        'api_password': 'apiPassword',
        'created_date_time': 'createdDateTime',
        'email': 'email',
        'error_details': 'errorDetails',
        'membership_id': 'membershipId',
        'permission_profile_id': 'permissionProfileId',
        'permission_profile_name': 'permissionProfileName',
        'uri': 'uri',
        'user_id': 'userId',
        'user_name': 'userName',
        'user_status': 'userStatus'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """NewUser - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_password = None
        self._created_date_time = None
        self._email = None
        self._error_details = None
        self._membership_id = None
        self._permission_profile_id = None
        self._permission_profile_name = None
        self._uri = None
        self._user_id = None
        self._user_name = None
        self._user_status = None
        self.discriminator = None

        setattr(self, "_{}".format('api_password'), kwargs.get('api_password', None))
        setattr(self, "_{}".format('created_date_time'), kwargs.get('created_date_time', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('membership_id'), kwargs.get('membership_id', None))
        setattr(self, "_{}".format('permission_profile_id'), kwargs.get('permission_profile_id', None))
        setattr(self, "_{}".format('permission_profile_name'), kwargs.get('permission_profile_name', None))
        setattr(self, "_{}".format('uri'), kwargs.get('uri', None))
        setattr(self, "_{}".format('user_id'), kwargs.get('user_id', None))
        setattr(self, "_{}".format('user_name'), kwargs.get('user_name', None))
        setattr(self, "_{}".format('user_status'), kwargs.get('user_status', None))

    @property
    def api_password(self):
        """Gets the api_password of this NewUser.  # noqa: E501

        Contains a token that can be used for authentication in API calls instead of using the user name and password.  # noqa: E501

        :return: The api_password of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._api_password

    @api_password.setter
    def api_password(self, api_password):
        """Sets the api_password of this NewUser.

        Contains a token that can be used for authentication in API calls instead of using the user name and password.  # noqa: E501

        :param api_password: The api_password of this NewUser.  # noqa: E501
        :type: str
        """

        self._api_password = api_password

    @property
    def created_date_time(self):
        """Gets the created_date_time of this NewUser.  # noqa: E501

        Indicates the date and time the item was created.  # noqa: E501

        :return: The created_date_time of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this NewUser.

        Indicates the date and time the item was created.  # noqa: E501

        :param created_date_time: The created_date_time of this NewUser.  # noqa: E501
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def email(self):
        """Gets the email of this NewUser.  # noqa: E501

          # noqa: E501

        :return: The email of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this NewUser.

          # noqa: E501

        :param email: The email of this NewUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def error_details(self):
        """Gets the error_details of this NewUser.  # noqa: E501


        :return: The error_details of this NewUser.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this NewUser.


        :param error_details: The error_details of this NewUser.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def membership_id(self):
        """Gets the membership_id of this NewUser.  # noqa: E501

          # noqa: E501

        :return: The membership_id of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._membership_id

    @membership_id.setter
    def membership_id(self, membership_id):
        """Sets the membership_id of this NewUser.

          # noqa: E501

        :param membership_id: The membership_id of this NewUser.  # noqa: E501
        :type: str
        """

        self._membership_id = membership_id

    @property
    def permission_profile_id(self):
        """Gets the permission_profile_id of this NewUser.  # noqa: E501

          # noqa: E501

        :return: The permission_profile_id of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._permission_profile_id

    @permission_profile_id.setter
    def permission_profile_id(self, permission_profile_id):
        """Sets the permission_profile_id of this NewUser.

          # noqa: E501

        :param permission_profile_id: The permission_profile_id of this NewUser.  # noqa: E501
        :type: str
        """

        self._permission_profile_id = permission_profile_id

    @property
    def permission_profile_name(self):
        """Gets the permission_profile_name of this NewUser.  # noqa: E501

          # noqa: E501

        :return: The permission_profile_name of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._permission_profile_name

    @permission_profile_name.setter
    def permission_profile_name(self, permission_profile_name):
        """Sets the permission_profile_name of this NewUser.

          # noqa: E501

        :param permission_profile_name: The permission_profile_name of this NewUser.  # noqa: E501
        :type: str
        """

        self._permission_profile_name = permission_profile_name

    @property
    def uri(self):
        """Gets the uri of this NewUser.  # noqa: E501

          # noqa: E501

        :return: The uri of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this NewUser.

          # noqa: E501

        :param uri: The uri of this NewUser.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def user_id(self):
        """Gets the user_id of this NewUser.  # noqa: E501

        Specifies the user ID for the new user.  # noqa: E501

        :return: The user_id of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NewUser.

        Specifies the user ID for the new user.  # noqa: E501

        :param user_id: The user_id of this NewUser.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this NewUser.  # noqa: E501

          # noqa: E501

        :return: The user_name of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this NewUser.

          # noqa: E501

        :param user_name: The user_name of this NewUser.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_status(self):
        """Gets the user_status of this NewUser.  # noqa: E501

          # noqa: E501

        :return: The user_status of this NewUser.  # noqa: E501
        :rtype: str
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """Sets the user_status of this NewUser.

          # noqa: E501

        :param user_status: The user_status of this NewUser.  # noqa: E501
        :type: str
        """

        self._user_status = user_status

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
        if issubclass(NewUser, dict):
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
        if not isinstance(other, NewUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewUser):
            return True

        return self.to_dict() != other.to_dict()
