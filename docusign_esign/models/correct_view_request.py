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


class CorrectViewRequest(object):
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
        'return_url': 'str',
        'suppress_navigation': 'str',
        'view_url': 'str'
    }

    attribute_map = {
        'return_url': 'returnUrl',
        'suppress_navigation': 'suppressNavigation',
        'view_url': 'viewUrl'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """CorrectViewRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._return_url = None
        self._suppress_navigation = None
        self._view_url = None
        self.discriminator = None

        setattr(self, "_{}".format('return_url'), kwargs.get('return_url', None))
        setattr(self, "_{}".format('suppress_navigation'), kwargs.get('suppress_navigation', None))
        setattr(self, "_{}".format('view_url'), kwargs.get('view_url', None))

    @property
    def return_url(self):
        """Gets the return_url of this CorrectViewRequest.  # noqa: E501

        The url used after correct/send view session has ended. DocuSign redirects to the url and includes an event parameter that can be used by your app. The event parameters returned are:   * send (user corrected and sent the envelope) * save (user saved the envelope) * cancel (user canceled the transaction.) * error (there was an error when performing the correct or send) * sessionEnd (the session ended before the user completed a different action)  ###### Note: Include https:// in the URL or the redirect might not succeed on some browsers.   # noqa: E501

        :return: The return_url of this CorrectViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this CorrectViewRequest.

        The url used after correct/send view session has ended. DocuSign redirects to the url and includes an event parameter that can be used by your app. The event parameters returned are:   * send (user corrected and sent the envelope) * save (user saved the envelope) * cancel (user canceled the transaction.) * error (there was an error when performing the correct or send) * sessionEnd (the session ended before the user completed a different action)  ###### Note: Include https:// in the URL or the redirect might not succeed on some browsers.   # noqa: E501

        :param return_url: The return_url of this CorrectViewRequest.  # noqa: E501
        :type: str
        """

        self._return_url = return_url

    @property
    def suppress_navigation(self):
        """Gets the suppress_navigation of this CorrectViewRequest.  # noqa: E501

        Specifies whether the window is displayed with or without dressing.  # noqa: E501

        :return: The suppress_navigation of this CorrectViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._suppress_navigation

    @suppress_navigation.setter
    def suppress_navigation(self, suppress_navigation):
        """Sets the suppress_navigation of this CorrectViewRequest.

        Specifies whether the window is displayed with or without dressing.  # noqa: E501

        :param suppress_navigation: The suppress_navigation of this CorrectViewRequest.  # noqa: E501
        :type: str
        """

        self._suppress_navigation = suppress_navigation

    @property
    def view_url(self):
        """Gets the view_url of this CorrectViewRequest.  # noqa: E501

          # noqa: E501

        :return: The view_url of this CorrectViewRequest.  # noqa: E501
        :rtype: str
        """
        return self._view_url

    @view_url.setter
    def view_url(self, view_url):
        """Sets the view_url of this CorrectViewRequest.

          # noqa: E501

        :param view_url: The view_url of this CorrectViewRequest.  # noqa: E501
        :type: str
        """

        self._view_url = view_url

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
        if issubclass(CorrectViewRequest, dict):
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
        if not isinstance(other, CorrectViewRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CorrectViewRequest):
            return True

        return self.to_dict() != other.to_dict()
