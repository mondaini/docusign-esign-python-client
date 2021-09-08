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


class ProvisioningInformation(object):
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
        'default_connection_id': 'str',
        'default_plan_id': 'str',
        'distributor_code': 'str',
        'distributor_password': 'str',
        'password_rule_text': 'str',
        'plan_promotion_text': 'str',
        'purchase_order_or_prom_allowed': 'str'
    }

    attribute_map = {
        'default_connection_id': 'defaultConnectionId',
        'default_plan_id': 'defaultPlanId',
        'distributor_code': 'distributorCode',
        'distributor_password': 'distributorPassword',
        'password_rule_text': 'passwordRuleText',
        'plan_promotion_text': 'planPromotionText',
        'purchase_order_or_prom_allowed': 'purchaseOrderOrPromAllowed'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ProvisioningInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._default_connection_id = None
        self._default_plan_id = None
        self._distributor_code = None
        self._distributor_password = None
        self._password_rule_text = None
        self._plan_promotion_text = None
        self._purchase_order_or_prom_allowed = None
        self.discriminator = None

        setattr(self, "_{}".format('default_connection_id'), kwargs.get('default_connection_id', None))
        setattr(self, "_{}".format('default_plan_id'), kwargs.get('default_plan_id', None))
        setattr(self, "_{}".format('distributor_code'), kwargs.get('distributor_code', None))
        setattr(self, "_{}".format('distributor_password'), kwargs.get('distributor_password', None))
        setattr(self, "_{}".format('password_rule_text'), kwargs.get('password_rule_text', None))
        setattr(self, "_{}".format('plan_promotion_text'), kwargs.get('plan_promotion_text', None))
        setattr(self, "_{}".format('purchase_order_or_prom_allowed'), kwargs.get('purchase_order_or_prom_allowed', None))

    @property
    def default_connection_id(self):
        """Gets the default_connection_id of this ProvisioningInformation.  # noqa: E501

          # noqa: E501

        :return: The default_connection_id of this ProvisioningInformation.  # noqa: E501
        :rtype: str
        """
        return self._default_connection_id

    @default_connection_id.setter
    def default_connection_id(self, default_connection_id):
        """Sets the default_connection_id of this ProvisioningInformation.

          # noqa: E501

        :param default_connection_id: The default_connection_id of this ProvisioningInformation.  # noqa: E501
        :type: str
        """

        self._default_connection_id = default_connection_id

    @property
    def default_plan_id(self):
        """Gets the default_plan_id of this ProvisioningInformation.  # noqa: E501

          # noqa: E501

        :return: The default_plan_id of this ProvisioningInformation.  # noqa: E501
        :rtype: str
        """
        return self._default_plan_id

    @default_plan_id.setter
    def default_plan_id(self, default_plan_id):
        """Sets the default_plan_id of this ProvisioningInformation.

          # noqa: E501

        :param default_plan_id: The default_plan_id of this ProvisioningInformation.  # noqa: E501
        :type: str
        """

        self._default_plan_id = default_plan_id

    @property
    def distributor_code(self):
        """Gets the distributor_code of this ProvisioningInformation.  # noqa: E501

        The code that identifies the billing plan groups and plans for the new account.  # noqa: E501

        :return: The distributor_code of this ProvisioningInformation.  # noqa: E501
        :rtype: str
        """
        return self._distributor_code

    @distributor_code.setter
    def distributor_code(self, distributor_code):
        """Sets the distributor_code of this ProvisioningInformation.

        The code that identifies the billing plan groups and plans for the new account.  # noqa: E501

        :param distributor_code: The distributor_code of this ProvisioningInformation.  # noqa: E501
        :type: str
        """

        self._distributor_code = distributor_code

    @property
    def distributor_password(self):
        """Gets the distributor_password of this ProvisioningInformation.  # noqa: E501

        The password for the distributorCode.  # noqa: E501

        :return: The distributor_password of this ProvisioningInformation.  # noqa: E501
        :rtype: str
        """
        return self._distributor_password

    @distributor_password.setter
    def distributor_password(self, distributor_password):
        """Sets the distributor_password of this ProvisioningInformation.

        The password for the distributorCode.  # noqa: E501

        :param distributor_password: The distributor_password of this ProvisioningInformation.  # noqa: E501
        :type: str
        """

        self._distributor_password = distributor_password

    @property
    def password_rule_text(self):
        """Gets the password_rule_text of this ProvisioningInformation.  # noqa: E501

          # noqa: E501

        :return: The password_rule_text of this ProvisioningInformation.  # noqa: E501
        :rtype: str
        """
        return self._password_rule_text

    @password_rule_text.setter
    def password_rule_text(self, password_rule_text):
        """Sets the password_rule_text of this ProvisioningInformation.

          # noqa: E501

        :param password_rule_text: The password_rule_text of this ProvisioningInformation.  # noqa: E501
        :type: str
        """

        self._password_rule_text = password_rule_text

    @property
    def plan_promotion_text(self):
        """Gets the plan_promotion_text of this ProvisioningInformation.  # noqa: E501

          # noqa: E501

        :return: The plan_promotion_text of this ProvisioningInformation.  # noqa: E501
        :rtype: str
        """
        return self._plan_promotion_text

    @plan_promotion_text.setter
    def plan_promotion_text(self, plan_promotion_text):
        """Sets the plan_promotion_text of this ProvisioningInformation.

          # noqa: E501

        :param plan_promotion_text: The plan_promotion_text of this ProvisioningInformation.  # noqa: E501
        :type: str
        """

        self._plan_promotion_text = plan_promotion_text

    @property
    def purchase_order_or_prom_allowed(self):
        """Gets the purchase_order_or_prom_allowed of this ProvisioningInformation.  # noqa: E501

          # noqa: E501

        :return: The purchase_order_or_prom_allowed of this ProvisioningInformation.  # noqa: E501
        :rtype: str
        """
        return self._purchase_order_or_prom_allowed

    @purchase_order_or_prom_allowed.setter
    def purchase_order_or_prom_allowed(self, purchase_order_or_prom_allowed):
        """Sets the purchase_order_or_prom_allowed of this ProvisioningInformation.

          # noqa: E501

        :param purchase_order_or_prom_allowed: The purchase_order_or_prom_allowed of this ProvisioningInformation.  # noqa: E501
        :type: str
        """

        self._purchase_order_or_prom_allowed = purchase_order_or_prom_allowed

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
        if issubclass(ProvisioningInformation, dict):
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
        if not isinstance(other, ProvisioningInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProvisioningInformation):
            return True

        return self.to_dict() != other.to_dict()
