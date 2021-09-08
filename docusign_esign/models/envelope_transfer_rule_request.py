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


class EnvelopeTransferRuleRequest(object):
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
        'carbon_copy_original_owner': 'str',
        'enabled': 'str',
        'envelope_transfer_rule_id': 'str',
        'event_type': 'str',
        'from_groups': 'list[Group]',
        'from_users': 'list[UserInformation]',
        'modified_date': 'str',
        'modified_user': 'UserInformation',
        'to_folder': 'Folder',
        'to_user': 'UserInformation'
    }

    attribute_map = {
        'carbon_copy_original_owner': 'carbonCopyOriginalOwner',
        'enabled': 'enabled',
        'envelope_transfer_rule_id': 'envelopeTransferRuleId',
        'event_type': 'eventType',
        'from_groups': 'fromGroups',
        'from_users': 'fromUsers',
        'modified_date': 'modifiedDate',
        'modified_user': 'modifiedUser',
        'to_folder': 'toFolder',
        'to_user': 'toUser'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """EnvelopeTransferRuleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._carbon_copy_original_owner = None
        self._enabled = None
        self._envelope_transfer_rule_id = None
        self._event_type = None
        self._from_groups = None
        self._from_users = None
        self._modified_date = None
        self._modified_user = None
        self._to_folder = None
        self._to_user = None
        self.discriminator = None

        setattr(self, "_{}".format('carbon_copy_original_owner'), kwargs.get('carbon_copy_original_owner', None))
        setattr(self, "_{}".format('enabled'), kwargs.get('enabled', None))
        setattr(self, "_{}".format('envelope_transfer_rule_id'), kwargs.get('envelope_transfer_rule_id', None))
        setattr(self, "_{}".format('event_type'), kwargs.get('event_type', None))
        setattr(self, "_{}".format('from_groups'), kwargs.get('from_groups', None))
        setattr(self, "_{}".format('from_users'), kwargs.get('from_users', None))
        setattr(self, "_{}".format('modified_date'), kwargs.get('modified_date', None))
        setattr(self, "_{}".format('modified_user'), kwargs.get('modified_user', None))
        setattr(self, "_{}".format('to_folder'), kwargs.get('to_folder', None))
        setattr(self, "_{}".format('to_user'), kwargs.get('to_user', None))

    @property
    def carbon_copy_original_owner(self):
        """Gets the carbon_copy_original_owner of this EnvelopeTransferRuleRequest.  # noqa: E501

          # noqa: E501

        :return: The carbon_copy_original_owner of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._carbon_copy_original_owner

    @carbon_copy_original_owner.setter
    def carbon_copy_original_owner(self, carbon_copy_original_owner):
        """Sets the carbon_copy_original_owner of this EnvelopeTransferRuleRequest.

          # noqa: E501

        :param carbon_copy_original_owner: The carbon_copy_original_owner of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: str
        """

        self._carbon_copy_original_owner = carbon_copy_original_owner

    @property
    def enabled(self):
        """Gets the enabled of this EnvelopeTransferRuleRequest.  # noqa: E501

          # noqa: E501

        :return: The enabled of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this EnvelopeTransferRuleRequest.

          # noqa: E501

        :param enabled: The enabled of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def envelope_transfer_rule_id(self):
        """Gets the envelope_transfer_rule_id of this EnvelopeTransferRuleRequest.  # noqa: E501

          # noqa: E501

        :return: The envelope_transfer_rule_id of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._envelope_transfer_rule_id

    @envelope_transfer_rule_id.setter
    def envelope_transfer_rule_id(self, envelope_transfer_rule_id):
        """Sets the envelope_transfer_rule_id of this EnvelopeTransferRuleRequest.

          # noqa: E501

        :param envelope_transfer_rule_id: The envelope_transfer_rule_id of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: str
        """

        self._envelope_transfer_rule_id = envelope_transfer_rule_id

    @property
    def event_type(self):
        """Gets the event_type of this EnvelopeTransferRuleRequest.  # noqa: E501

          # noqa: E501

        :return: The event_type of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EnvelopeTransferRuleRequest.

          # noqa: E501

        :param event_type: The event_type of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def from_groups(self):
        """Gets the from_groups of this EnvelopeTransferRuleRequest.  # noqa: E501

          # noqa: E501

        :return: The from_groups of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: list[Group]
        """
        return self._from_groups

    @from_groups.setter
    def from_groups(self, from_groups):
        """Sets the from_groups of this EnvelopeTransferRuleRequest.

          # noqa: E501

        :param from_groups: The from_groups of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: list[Group]
        """

        self._from_groups = from_groups

    @property
    def from_users(self):
        """Gets the from_users of this EnvelopeTransferRuleRequest.  # noqa: E501

          # noqa: E501

        :return: The from_users of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: list[UserInformation]
        """
        return self._from_users

    @from_users.setter
    def from_users(self, from_users):
        """Sets the from_users of this EnvelopeTransferRuleRequest.

          # noqa: E501

        :param from_users: The from_users of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: list[UserInformation]
        """

        self._from_users = from_users

    @property
    def modified_date(self):
        """Gets the modified_date of this EnvelopeTransferRuleRequest.  # noqa: E501

          # noqa: E501

        :return: The modified_date of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this EnvelopeTransferRuleRequest.

          # noqa: E501

        :param modified_date: The modified_date of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: str
        """

        self._modified_date = modified_date

    @property
    def modified_user(self):
        """Gets the modified_user of this EnvelopeTransferRuleRequest.  # noqa: E501


        :return: The modified_user of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: UserInformation
        """
        return self._modified_user

    @modified_user.setter
    def modified_user(self, modified_user):
        """Sets the modified_user of this EnvelopeTransferRuleRequest.


        :param modified_user: The modified_user of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: UserInformation
        """

        self._modified_user = modified_user

    @property
    def to_folder(self):
        """Gets the to_folder of this EnvelopeTransferRuleRequest.  # noqa: E501


        :return: The to_folder of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: Folder
        """
        return self._to_folder

    @to_folder.setter
    def to_folder(self, to_folder):
        """Sets the to_folder of this EnvelopeTransferRuleRequest.


        :param to_folder: The to_folder of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: Folder
        """

        self._to_folder = to_folder

    @property
    def to_user(self):
        """Gets the to_user of this EnvelopeTransferRuleRequest.  # noqa: E501


        :return: The to_user of this EnvelopeTransferRuleRequest.  # noqa: E501
        :rtype: UserInformation
        """
        return self._to_user

    @to_user.setter
    def to_user(self, to_user):
        """Sets the to_user of this EnvelopeTransferRuleRequest.


        :param to_user: The to_user of this EnvelopeTransferRuleRequest.  # noqa: E501
        :type: UserInformation
        """

        self._to_user = to_user

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
        if issubclass(EnvelopeTransferRuleRequest, dict):
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
        if not isinstance(other, EnvelopeTransferRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvelopeTransferRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
