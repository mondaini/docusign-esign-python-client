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


class Workspace(object):
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
        'billable_account_id': 'str',
        'caller_information': 'WorkspaceUser',
        'created': 'str',
        'created_by_information': 'WorkspaceUser',
        'last_modified': 'str',
        'last_modified_by_information': 'WorkspaceUser',
        'settings': 'WorkspaceSettings',
        'status': 'str',
        'workspace_base_url': 'str',
        'workspace_description': 'str',
        'workspace_id': 'str',
        'workspace_name': 'str',
        'workspace_uri': 'str'
    }

    attribute_map = {
        'billable_account_id': 'billableAccountId',
        'caller_information': 'callerInformation',
        'created': 'created',
        'created_by_information': 'createdByInformation',
        'last_modified': 'lastModified',
        'last_modified_by_information': 'lastModifiedByInformation',
        'settings': 'settings',
        'status': 'status',
        'workspace_base_url': 'workspaceBaseUrl',
        'workspace_description': 'workspaceDescription',
        'workspace_id': 'workspaceId',
        'workspace_name': 'workspaceName',
        'workspace_uri': 'workspaceUri'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """Workspace - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billable_account_id = None
        self._caller_information = None
        self._created = None
        self._created_by_information = None
        self._last_modified = None
        self._last_modified_by_information = None
        self._settings = None
        self._status = None
        self._workspace_base_url = None
        self._workspace_description = None
        self._workspace_id = None
        self._workspace_name = None
        self._workspace_uri = None
        self.discriminator = None

        setattr(self, "_{}".format('billable_account_id'), kwargs.get('billable_account_id', None))
        setattr(self, "_{}".format('caller_information'), kwargs.get('caller_information', None))
        setattr(self, "_{}".format('created'), kwargs.get('created', None))
        setattr(self, "_{}".format('created_by_information'), kwargs.get('created_by_information', None))
        setattr(self, "_{}".format('last_modified'), kwargs.get('last_modified', None))
        setattr(self, "_{}".format('last_modified_by_information'), kwargs.get('last_modified_by_information', None))
        setattr(self, "_{}".format('settings'), kwargs.get('settings', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('workspace_base_url'), kwargs.get('workspace_base_url', None))
        setattr(self, "_{}".format('workspace_description'), kwargs.get('workspace_description', None))
        setattr(self, "_{}".format('workspace_id'), kwargs.get('workspace_id', None))
        setattr(self, "_{}".format('workspace_name'), kwargs.get('workspace_name', None))
        setattr(self, "_{}".format('workspace_uri'), kwargs.get('workspace_uri', None))

    @property
    def billable_account_id(self):
        """Gets the billable_account_id of this Workspace.  # noqa: E501

          # noqa: E501

        :return: The billable_account_id of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._billable_account_id

    @billable_account_id.setter
    def billable_account_id(self, billable_account_id):
        """Sets the billable_account_id of this Workspace.

          # noqa: E501

        :param billable_account_id: The billable_account_id of this Workspace.  # noqa: E501
        :type: str
        """

        self._billable_account_id = billable_account_id

    @property
    def caller_information(self):
        """Gets the caller_information of this Workspace.  # noqa: E501


        :return: The caller_information of this Workspace.  # noqa: E501
        :rtype: WorkspaceUser
        """
        return self._caller_information

    @caller_information.setter
    def caller_information(self, caller_information):
        """Sets the caller_information of this Workspace.


        :param caller_information: The caller_information of this Workspace.  # noqa: E501
        :type: WorkspaceUser
        """

        self._caller_information = caller_information

    @property
    def created(self):
        """Gets the created of this Workspace.  # noqa: E501

          # noqa: E501

        :return: The created of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Workspace.

          # noqa: E501

        :param created: The created of this Workspace.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def created_by_information(self):
        """Gets the created_by_information of this Workspace.  # noqa: E501


        :return: The created_by_information of this Workspace.  # noqa: E501
        :rtype: WorkspaceUser
        """
        return self._created_by_information

    @created_by_information.setter
    def created_by_information(self, created_by_information):
        """Sets the created_by_information of this Workspace.


        :param created_by_information: The created_by_information of this Workspace.  # noqa: E501
        :type: WorkspaceUser
        """

        self._created_by_information = created_by_information

    @property
    def last_modified(self):
        """Gets the last_modified of this Workspace.  # noqa: E501

        Utc date and time the comment was last updated (can only be done by creator.)  # noqa: E501

        :return: The last_modified of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Workspace.

        Utc date and time the comment was last updated (can only be done by creator.)  # noqa: E501

        :param last_modified: The last_modified of this Workspace.  # noqa: E501
        :type: str
        """

        self._last_modified = last_modified

    @property
    def last_modified_by_information(self):
        """Gets the last_modified_by_information of this Workspace.  # noqa: E501


        :return: The last_modified_by_information of this Workspace.  # noqa: E501
        :rtype: WorkspaceUser
        """
        return self._last_modified_by_information

    @last_modified_by_information.setter
    def last_modified_by_information(self, last_modified_by_information):
        """Sets the last_modified_by_information of this Workspace.


        :param last_modified_by_information: The last_modified_by_information of this Workspace.  # noqa: E501
        :type: WorkspaceUser
        """

        self._last_modified_by_information = last_modified_by_information

    @property
    def settings(self):
        """Gets the settings of this Workspace.  # noqa: E501


        :return: The settings of this Workspace.  # noqa: E501
        :rtype: WorkspaceSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Workspace.


        :param settings: The settings of this Workspace.  # noqa: E501
        :type: WorkspaceSettings
        """

        self._settings = settings

    @property
    def status(self):
        """Gets the status of this Workspace.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Workspace.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this Workspace.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def workspace_base_url(self):
        """Gets the workspace_base_url of this Workspace.  # noqa: E501

        The relative URL that may be used to access the workspace.  # noqa: E501

        :return: The workspace_base_url of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._workspace_base_url

    @workspace_base_url.setter
    def workspace_base_url(self, workspace_base_url):
        """Sets the workspace_base_url of this Workspace.

        The relative URL that may be used to access the workspace.  # noqa: E501

        :param workspace_base_url: The workspace_base_url of this Workspace.  # noqa: E501
        :type: str
        """

        self._workspace_base_url = workspace_base_url

    @property
    def workspace_description(self):
        """Gets the workspace_description of this Workspace.  # noqa: E501

        Text describing the purpose of the workspace.  # noqa: E501

        :return: The workspace_description of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._workspace_description

    @workspace_description.setter
    def workspace_description(self, workspace_description):
        """Sets the workspace_description of this Workspace.

        Text describing the purpose of the workspace.  # noqa: E501

        :param workspace_description: The workspace_description of this Workspace.  # noqa: E501
        :type: str
        """

        self._workspace_description = workspace_description

    @property
    def workspace_id(self):
        """Gets the workspace_id of this Workspace.  # noqa: E501

        The id of the workspace, always populated.  # noqa: E501

        :return: The workspace_id of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this Workspace.

        The id of the workspace, always populated.  # noqa: E501

        :param workspace_id: The workspace_id of this Workspace.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def workspace_name(self):
        """Gets the workspace_name of this Workspace.  # noqa: E501

        The name of the workspace.  # noqa: E501

        :return: The workspace_name of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        """Sets the workspace_name of this Workspace.

        The name of the workspace.  # noqa: E501

        :param workspace_name: The workspace_name of this Workspace.  # noqa: E501
        :type: str
        """

        self._workspace_name = workspace_name

    @property
    def workspace_uri(self):
        """Gets the workspace_uri of this Workspace.  # noqa: E501

        The relative URI that may be used to access the workspace.  # noqa: E501

        :return: The workspace_uri of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._workspace_uri

    @workspace_uri.setter
    def workspace_uri(self, workspace_uri):
        """Sets the workspace_uri of this Workspace.

        The relative URI that may be used to access the workspace.  # noqa: E501

        :param workspace_uri: The workspace_uri of this Workspace.  # noqa: E501
        :type: str
        """

        self._workspace_uri = workspace_uri

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
        if issubclass(Workspace, dict):
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
        if not isinstance(other, Workspace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Workspace):
            return True

        return self.to_dict() != other.to_dict()
