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


class PermissionProfile(object):
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
        'modified_by_username': 'str',
        'modified_date_time': 'str',
        'permission_profile_id': 'str',
        'permission_profile_name': 'str',
        'settings': 'AccountRoleSettings',
        'user_count': 'str',
        'users': 'list[UserInformation]'
    }

    attribute_map = {
        'modified_by_username': 'modifiedByUsername',
        'modified_date_time': 'modifiedDateTime',
        'permission_profile_id': 'permissionProfileId',
        'permission_profile_name': 'permissionProfileName',
        'settings': 'settings',
        'user_count': 'userCount',
        'users': 'users'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """PermissionProfile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._modified_by_username = None
        self._modified_date_time = None
        self._permission_profile_id = None
        self._permission_profile_name = None
        self._settings = None
        self._user_count = None
        self._users = None
        self.discriminator = None

        setattr(self, "_{}".format('modified_by_username'), kwargs.get('modified_by_username', None))
        setattr(self, "_{}".format('modified_date_time'), kwargs.get('modified_date_time', None))
        setattr(self, "_{}".format('permission_profile_id'), kwargs.get('permission_profile_id', None))
        setattr(self, "_{}".format('permission_profile_name'), kwargs.get('permission_profile_name', None))
        setattr(self, "_{}".format('settings'), kwargs.get('settings', None))
        setattr(self, "_{}".format('user_count'), kwargs.get('user_count', None))
        setattr(self, "_{}".format('users'), kwargs.get('users', None))

    @property
    def modified_by_username(self):
        """Gets the modified_by_username of this PermissionProfile.  # noqa: E501

          # noqa: E501

        :return: The modified_by_username of this PermissionProfile.  # noqa: E501
        :rtype: str
        """
        return self._modified_by_username

    @modified_by_username.setter
    def modified_by_username(self, modified_by_username):
        """Sets the modified_by_username of this PermissionProfile.

          # noqa: E501

        :param modified_by_username: The modified_by_username of this PermissionProfile.  # noqa: E501
        :type: str
        """

        self._modified_by_username = modified_by_username

    @property
    def modified_date_time(self):
        """Gets the modified_date_time of this PermissionProfile.  # noqa: E501

          # noqa: E501

        :return: The modified_date_time of this PermissionProfile.  # noqa: E501
        :rtype: str
        """
        return self._modified_date_time

    @modified_date_time.setter
    def modified_date_time(self, modified_date_time):
        """Sets the modified_date_time of this PermissionProfile.

          # noqa: E501

        :param modified_date_time: The modified_date_time of this PermissionProfile.  # noqa: E501
        :type: str
        """

        self._modified_date_time = modified_date_time

    @property
    def permission_profile_id(self):
        """Gets the permission_profile_id of this PermissionProfile.  # noqa: E501

          # noqa: E501

        :return: The permission_profile_id of this PermissionProfile.  # noqa: E501
        :rtype: str
        """
        return self._permission_profile_id

    @permission_profile_id.setter
    def permission_profile_id(self, permission_profile_id):
        """Sets the permission_profile_id of this PermissionProfile.

          # noqa: E501

        :param permission_profile_id: The permission_profile_id of this PermissionProfile.  # noqa: E501
        :type: str
        """

        self._permission_profile_id = permission_profile_id

    @property
    def permission_profile_name(self):
        """Gets the permission_profile_name of this PermissionProfile.  # noqa: E501

          # noqa: E501

        :return: The permission_profile_name of this PermissionProfile.  # noqa: E501
        :rtype: str
        """
        return self._permission_profile_name

    @permission_profile_name.setter
    def permission_profile_name(self, permission_profile_name):
        """Sets the permission_profile_name of this PermissionProfile.

          # noqa: E501

        :param permission_profile_name: The permission_profile_name of this PermissionProfile.  # noqa: E501
        :type: str
        """

        self._permission_profile_name = permission_profile_name

    @property
    def settings(self):
        """Gets the settings of this PermissionProfile.  # noqa: E501


        :return: The settings of this PermissionProfile.  # noqa: E501
        :rtype: AccountRoleSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this PermissionProfile.


        :param settings: The settings of this PermissionProfile.  # noqa: E501
        :type: AccountRoleSettings
        """

        self._settings = settings

    @property
    def user_count(self):
        """Gets the user_count of this PermissionProfile.  # noqa: E501

          # noqa: E501

        :return: The user_count of this PermissionProfile.  # noqa: E501
        :rtype: str
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this PermissionProfile.

          # noqa: E501

        :param user_count: The user_count of this PermissionProfile.  # noqa: E501
        :type: str
        """

        self._user_count = user_count

    @property
    def users(self):
        """Gets the users of this PermissionProfile.  # noqa: E501

          # noqa: E501

        :return: The users of this PermissionProfile.  # noqa: E501
        :rtype: list[UserInformation]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this PermissionProfile.

          # noqa: E501

        :param users: The users of this PermissionProfile.  # noqa: E501
        :type: list[UserInformation]
        """

        self._users = users

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
        if issubclass(PermissionProfile, dict):
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
        if not isinstance(other, PermissionProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PermissionProfile):
            return True

        return self.to_dict() != other.to_dict()
