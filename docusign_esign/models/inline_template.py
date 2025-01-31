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


class InlineTemplate(object):
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
        'custom_fields': 'CustomFields',
        'documents': 'list[Document]',
        'envelope': 'Envelope',
        'recipients': 'Recipients',
        'sequence': 'str'
    }

    attribute_map = {
        'custom_fields': 'customFields',
        'documents': 'documents',
        'envelope': 'envelope',
        'recipients': 'recipients',
        'sequence': 'sequence'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """InlineTemplate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_fields = None
        self._documents = None
        self._envelope = None
        self._recipients = None
        self._sequence = None
        self.discriminator = None

        setattr(self, "_{}".format('custom_fields'), kwargs.get('custom_fields', None))
        setattr(self, "_{}".format('documents'), kwargs.get('documents', None))
        setattr(self, "_{}".format('envelope'), kwargs.get('envelope', None))
        setattr(self, "_{}".format('recipients'), kwargs.get('recipients', None))
        setattr(self, "_{}".format('sequence'), kwargs.get('sequence', None))

    @property
    def custom_fields(self):
        """Gets the custom_fields of this InlineTemplate.  # noqa: E501

        An optional array of strings that enables the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each `customField` string can be a maximum of 100 characters.  # noqa: E501

        :return: The custom_fields of this InlineTemplate.  # noqa: E501
        :rtype: CustomFields
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this InlineTemplate.

        An optional array of strings that enables the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by DocuSign. Each `customField` string can be a maximum of 100 characters.  # noqa: E501

        :param custom_fields: The custom_fields of this InlineTemplate.  # noqa: E501
        :type: CustomFields
        """

        self._custom_fields = custom_fields

    @property
    def documents(self):
        """Gets the documents of this InlineTemplate.  # noqa: E501

        Complex element contains the details on the documents in the envelope.  # noqa: E501

        :return: The documents of this InlineTemplate.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this InlineTemplate.

        Complex element contains the details on the documents in the envelope.  # noqa: E501

        :param documents: The documents of this InlineTemplate.  # noqa: E501
        :type: list[Document]
        """

        self._documents = documents

    @property
    def envelope(self):
        """Gets the envelope of this InlineTemplate.  # noqa: E501

        A container used to send documents to recipients. The envelope carries information about the sender and timestamps to indicate the progress of the delivery procedure. It can contain collections of Documents, Tabs and Recipients.  # noqa: E501

        :return: The envelope of this InlineTemplate.  # noqa: E501
        :rtype: Envelope
        """
        return self._envelope

    @envelope.setter
    def envelope(self, envelope):
        """Sets the envelope of this InlineTemplate.

        A container used to send documents to recipients. The envelope carries information about the sender and timestamps to indicate the progress of the delivery procedure. It can contain collections of Documents, Tabs and Recipients.  # noqa: E501

        :param envelope: The envelope of this InlineTemplate.  # noqa: E501
        :type: Envelope
        """

        self._envelope = envelope

    @property
    def recipients(self):
        """Gets the recipients of this InlineTemplate.  # noqa: E501

        An array of recipient objects that provides details about the recipients of the envelope.  # noqa: E501

        :return: The recipients of this InlineTemplate.  # noqa: E501
        :rtype: Recipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this InlineTemplate.

        An array of recipient objects that provides details about the recipients of the envelope.  # noqa: E501

        :param recipients: The recipients of this InlineTemplate.  # noqa: E501
        :type: Recipients
        """

        self._recipients = recipients

    @property
    def sequence(self):
        """Gets the sequence of this InlineTemplate.  # noqa: E501

        Specifies the order in which templates are overlaid.  # noqa: E501

        :return: The sequence of this InlineTemplate.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this InlineTemplate.

        Specifies the order in which templates are overlaid.  # noqa: E501

        :param sequence: The sequence of this InlineTemplate.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

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
        if issubclass(InlineTemplate, dict):
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
        if not isinstance(other, InlineTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineTemplate):
            return True

        return self.to_dict() != other.to_dict()
