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


class MergeField(object):
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
        'allow_sender_to_edit': 'str',
        'allow_sender_to_edit_metadata': 'PropertyMetadata',
        'configuration_type': 'str',
        'configuration_type_metadata': 'PropertyMetadata',
        'path': 'str',
        'path_extended': 'list[PathExtendedElement]',
        'path_extended_metadata': 'PropertyMetadata',
        'path_metadata': 'PropertyMetadata',
        'row': 'str',
        'row_metadata': 'PropertyMetadata',
        'write_back': 'str',
        'write_back_metadata': 'PropertyMetadata'
    }

    attribute_map = {
        'allow_sender_to_edit': 'allowSenderToEdit',
        'allow_sender_to_edit_metadata': 'allowSenderToEditMetadata',
        'configuration_type': 'configurationType',
        'configuration_type_metadata': 'configurationTypeMetadata',
        'path': 'path',
        'path_extended': 'pathExtended',
        'path_extended_metadata': 'pathExtendedMetadata',
        'path_metadata': 'pathMetadata',
        'row': 'row',
        'row_metadata': 'rowMetadata',
        'write_back': 'writeBack',
        'write_back_metadata': 'writeBackMetadata'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """MergeField - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_sender_to_edit = None
        self._allow_sender_to_edit_metadata = None
        self._configuration_type = None
        self._configuration_type_metadata = None
        self._path = None
        self._path_extended = None
        self._path_extended_metadata = None
        self._path_metadata = None
        self._row = None
        self._row_metadata = None
        self._write_back = None
        self._write_back_metadata = None
        self.discriminator = None

        setattr(self, "_{}".format('allow_sender_to_edit'), kwargs.get('allow_sender_to_edit', None))
        setattr(self, "_{}".format('allow_sender_to_edit_metadata'), kwargs.get('allow_sender_to_edit_metadata', None))
        setattr(self, "_{}".format('configuration_type'), kwargs.get('configuration_type', None))
        setattr(self, "_{}".format('configuration_type_metadata'), kwargs.get('configuration_type_metadata', None))
        setattr(self, "_{}".format('path'), kwargs.get('path', None))
        setattr(self, "_{}".format('path_extended'), kwargs.get('path_extended', None))
        setattr(self, "_{}".format('path_extended_metadata'), kwargs.get('path_extended_metadata', None))
        setattr(self, "_{}".format('path_metadata'), kwargs.get('path_metadata', None))
        setattr(self, "_{}".format('row'), kwargs.get('row', None))
        setattr(self, "_{}".format('row_metadata'), kwargs.get('row_metadata', None))
        setattr(self, "_{}".format('write_back'), kwargs.get('write_back', None))
        setattr(self, "_{}".format('write_back_metadata'), kwargs.get('write_back_metadata', None))

    @property
    def allow_sender_to_edit(self):
        """Gets the allow_sender_to_edit of this MergeField.  # noqa: E501

        When set to **true**, the sender can modify the value of the custom tab during the sending process.  # noqa: E501

        :return: The allow_sender_to_edit of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._allow_sender_to_edit

    @allow_sender_to_edit.setter
    def allow_sender_to_edit(self, allow_sender_to_edit):
        """Sets the allow_sender_to_edit of this MergeField.

        When set to **true**, the sender can modify the value of the custom tab during the sending process.  # noqa: E501

        :param allow_sender_to_edit: The allow_sender_to_edit of this MergeField.  # noqa: E501
        :type: str
        """

        self._allow_sender_to_edit = allow_sender_to_edit

    @property
    def allow_sender_to_edit_metadata(self):
        """Gets the allow_sender_to_edit_metadata of this MergeField.  # noqa: E501


        :return: The allow_sender_to_edit_metadata of this MergeField.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._allow_sender_to_edit_metadata

    @allow_sender_to_edit_metadata.setter
    def allow_sender_to_edit_metadata(self, allow_sender_to_edit_metadata):
        """Sets the allow_sender_to_edit_metadata of this MergeField.


        :param allow_sender_to_edit_metadata: The allow_sender_to_edit_metadata of this MergeField.  # noqa: E501
        :type: PropertyMetadata
        """

        self._allow_sender_to_edit_metadata = allow_sender_to_edit_metadata

    @property
    def configuration_type(self):
        """Gets the configuration_type of this MergeField.  # noqa: E501

        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.  # noqa: E501

        :return: The configuration_type of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """Sets the configuration_type of this MergeField.

        If merge field's are being used, specifies the type of the merge field. The only  supported value is **salesforce**.  # noqa: E501

        :param configuration_type: The configuration_type of this MergeField.  # noqa: E501
        :type: str
        """

        self._configuration_type = configuration_type

    @property
    def configuration_type_metadata(self):
        """Gets the configuration_type_metadata of this MergeField.  # noqa: E501


        :return: The configuration_type_metadata of this MergeField.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._configuration_type_metadata

    @configuration_type_metadata.setter
    def configuration_type_metadata(self, configuration_type_metadata):
        """Sets the configuration_type_metadata of this MergeField.


        :param configuration_type_metadata: The configuration_type_metadata of this MergeField.  # noqa: E501
        :type: PropertyMetadata
        """

        self._configuration_type_metadata = configuration_type_metadata

    @property
    def path(self):
        """Gets the path of this MergeField.  # noqa: E501

        Sets the object associated with the custom tab. Currently this is the Salesforce Object.  # noqa: E501

        :return: The path of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MergeField.

        Sets the object associated with the custom tab. Currently this is the Salesforce Object.  # noqa: E501

        :param path: The path of this MergeField.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def path_extended(self):
        """Gets the path_extended of this MergeField.  # noqa: E501

          # noqa: E501

        :return: The path_extended of this MergeField.  # noqa: E501
        :rtype: list[PathExtendedElement]
        """
        return self._path_extended

    @path_extended.setter
    def path_extended(self, path_extended):
        """Sets the path_extended of this MergeField.

          # noqa: E501

        :param path_extended: The path_extended of this MergeField.  # noqa: E501
        :type: list[PathExtendedElement]
        """

        self._path_extended = path_extended

    @property
    def path_extended_metadata(self):
        """Gets the path_extended_metadata of this MergeField.  # noqa: E501


        :return: The path_extended_metadata of this MergeField.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._path_extended_metadata

    @path_extended_metadata.setter
    def path_extended_metadata(self, path_extended_metadata):
        """Sets the path_extended_metadata of this MergeField.


        :param path_extended_metadata: The path_extended_metadata of this MergeField.  # noqa: E501
        :type: PropertyMetadata
        """

        self._path_extended_metadata = path_extended_metadata

    @property
    def path_metadata(self):
        """Gets the path_metadata of this MergeField.  # noqa: E501


        :return: The path_metadata of this MergeField.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._path_metadata

    @path_metadata.setter
    def path_metadata(self, path_metadata):
        """Sets the path_metadata of this MergeField.


        :param path_metadata: The path_metadata of this MergeField.  # noqa: E501
        :type: PropertyMetadata
        """

        self._path_metadata = path_metadata

    @property
    def row(self):
        """Gets the row of this MergeField.  # noqa: E501

        Specifies the row number in a Salesforce table that the merge field value corresponds to.  # noqa: E501

        :return: The row of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._row

    @row.setter
    def row(self, row):
        """Sets the row of this MergeField.

        Specifies the row number in a Salesforce table that the merge field value corresponds to.  # noqa: E501

        :param row: The row of this MergeField.  # noqa: E501
        :type: str
        """

        self._row = row

    @property
    def row_metadata(self):
        """Gets the row_metadata of this MergeField.  # noqa: E501


        :return: The row_metadata of this MergeField.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._row_metadata

    @row_metadata.setter
    def row_metadata(self, row_metadata):
        """Sets the row_metadata of this MergeField.


        :param row_metadata: The row_metadata of this MergeField.  # noqa: E501
        :type: PropertyMetadata
        """

        self._row_metadata = row_metadata

    @property
    def write_back(self):
        """Gets the write_back of this MergeField.  # noqa: E501

        When wet to true, the information entered in the tab automatically updates the related Salesforce data when an envelope is completed.  # noqa: E501

        :return: The write_back of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._write_back

    @write_back.setter
    def write_back(self, write_back):
        """Sets the write_back of this MergeField.

        When wet to true, the information entered in the tab automatically updates the related Salesforce data when an envelope is completed.  # noqa: E501

        :param write_back: The write_back of this MergeField.  # noqa: E501
        :type: str
        """

        self._write_back = write_back

    @property
    def write_back_metadata(self):
        """Gets the write_back_metadata of this MergeField.  # noqa: E501


        :return: The write_back_metadata of this MergeField.  # noqa: E501
        :rtype: PropertyMetadata
        """
        return self._write_back_metadata

    @write_back_metadata.setter
    def write_back_metadata(self, write_back_metadata):
        """Sets the write_back_metadata of this MergeField.


        :param write_back_metadata: The write_back_metadata of this MergeField.  # noqa: E501
        :type: PropertyMetadata
        """

        self._write_back_metadata = write_back_metadata

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
        if issubclass(MergeField, dict):
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
        if not isinstance(other, MergeField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MergeField):
            return True

        return self.to_dict() != other.to_dict()
