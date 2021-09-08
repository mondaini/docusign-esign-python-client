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


class Note(object):
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
        'anchor_case_sensitive': 'str',
        'anchor_horizontal_alignment': 'str',
        'anchor_ignore_if_not_present': 'str',
        'anchor_match_whole_word': 'str',
        'anchor_string': 'str',
        'anchor_units': 'str',
        'anchor_x_offset': 'str',
        'anchor_y_offset': 'str',
        'bold': 'str',
        'conditional_parent_label': 'str',
        'conditional_parent_value': 'str',
        'custom_tab_id': 'str',
        'document_id': 'str',
        'error_details': 'ErrorDetails',
        'font': 'str',
        'font_color': 'str',
        'font_size': 'str',
        'height': 'int',
        'italic': 'str',
        'merge_field': 'MergeField',
        'name': 'str',
        'page_number': 'str',
        'recipient_id': 'str',
        'shared': 'str',
        'status': 'str',
        'tab_group_labels': 'list[str]',
        'tab_id': 'str',
        'tab_label': 'str',
        'tab_order': 'str',
        'template_locked': 'str',
        'template_required': 'str',
        'tooltip': 'str',
        'underline': 'str',
        'value': 'str',
        'width': 'int',
        'x_position': 'str',
        'y_position': 'str'
    }

    attribute_map = {
        'anchor_case_sensitive': 'anchorCaseSensitive',
        'anchor_horizontal_alignment': 'anchorHorizontalAlignment',
        'anchor_ignore_if_not_present': 'anchorIgnoreIfNotPresent',
        'anchor_match_whole_word': 'anchorMatchWholeWord',
        'anchor_string': 'anchorString',
        'anchor_units': 'anchorUnits',
        'anchor_x_offset': 'anchorXOffset',
        'anchor_y_offset': 'anchorYOffset',
        'bold': 'bold',
        'conditional_parent_label': 'conditionalParentLabel',
        'conditional_parent_value': 'conditionalParentValue',
        'custom_tab_id': 'customTabId',
        'document_id': 'documentId',
        'error_details': 'errorDetails',
        'font': 'font',
        'font_color': 'fontColor',
        'font_size': 'fontSize',
        'height': 'height',
        'italic': 'italic',
        'merge_field': 'mergeField',
        'name': 'name',
        'page_number': 'pageNumber',
        'recipient_id': 'recipientId',
        'shared': 'shared',
        'status': 'status',
        'tab_group_labels': 'tabGroupLabels',
        'tab_id': 'tabId',
        'tab_label': 'tabLabel',
        'tab_order': 'tabOrder',
        'template_locked': 'templateLocked',
        'template_required': 'templateRequired',
        'tooltip': 'tooltip',
        'underline': 'underline',
        'value': 'value',
        'width': 'width',
        'x_position': 'xPosition',
        'y_position': 'yPosition'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """Note - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._anchor_case_sensitive = None
        self._anchor_horizontal_alignment = None
        self._anchor_ignore_if_not_present = None
        self._anchor_match_whole_word = None
        self._anchor_string = None
        self._anchor_units = None
        self._anchor_x_offset = None
        self._anchor_y_offset = None
        self._bold = None
        self._conditional_parent_label = None
        self._conditional_parent_value = None
        self._custom_tab_id = None
        self._document_id = None
        self._error_details = None
        self._font = None
        self._font_color = None
        self._font_size = None
        self._height = None
        self._italic = None
        self._merge_field = None
        self._name = None
        self._page_number = None
        self._recipient_id = None
        self._shared = None
        self._status = None
        self._tab_group_labels = None
        self._tab_id = None
        self._tab_label = None
        self._tab_order = None
        self._template_locked = None
        self._template_required = None
        self._tooltip = None
        self._underline = None
        self._value = None
        self._width = None
        self._x_position = None
        self._y_position = None
        self.discriminator = None

        setattr(self, "_{}".format('anchor_case_sensitive'), kwargs.get('anchor_case_sensitive', None))
        setattr(self, "_{}".format('anchor_horizontal_alignment'), kwargs.get('anchor_horizontal_alignment', None))
        setattr(self, "_{}".format('anchor_ignore_if_not_present'), kwargs.get('anchor_ignore_if_not_present', None))
        setattr(self, "_{}".format('anchor_match_whole_word'), kwargs.get('anchor_match_whole_word', None))
        setattr(self, "_{}".format('anchor_string'), kwargs.get('anchor_string', None))
        setattr(self, "_{}".format('anchor_units'), kwargs.get('anchor_units', None))
        setattr(self, "_{}".format('anchor_x_offset'), kwargs.get('anchor_x_offset', None))
        setattr(self, "_{}".format('anchor_y_offset'), kwargs.get('anchor_y_offset', None))
        setattr(self, "_{}".format('bold'), kwargs.get('bold', None))
        setattr(self, "_{}".format('conditional_parent_label'), kwargs.get('conditional_parent_label', None))
        setattr(self, "_{}".format('conditional_parent_value'), kwargs.get('conditional_parent_value', None))
        setattr(self, "_{}".format('custom_tab_id'), kwargs.get('custom_tab_id', None))
        setattr(self, "_{}".format('document_id'), kwargs.get('document_id', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('font'), kwargs.get('font', None))
        setattr(self, "_{}".format('font_color'), kwargs.get('font_color', None))
        setattr(self, "_{}".format('font_size'), kwargs.get('font_size', None))
        setattr(self, "_{}".format('height'), kwargs.get('height', None))
        setattr(self, "_{}".format('italic'), kwargs.get('italic', None))
        setattr(self, "_{}".format('merge_field'), kwargs.get('merge_field', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('page_number'), kwargs.get('page_number', None))
        setattr(self, "_{}".format('recipient_id'), kwargs.get('recipient_id', None))
        setattr(self, "_{}".format('shared'), kwargs.get('shared', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('tab_group_labels'), kwargs.get('tab_group_labels', None))
        setattr(self, "_{}".format('tab_id'), kwargs.get('tab_id', None))
        setattr(self, "_{}".format('tab_label'), kwargs.get('tab_label', None))
        setattr(self, "_{}".format('tab_order'), kwargs.get('tab_order', None))
        setattr(self, "_{}".format('template_locked'), kwargs.get('template_locked', None))
        setattr(self, "_{}".format('template_required'), kwargs.get('template_required', None))
        setattr(self, "_{}".format('tooltip'), kwargs.get('tooltip', None))
        setattr(self, "_{}".format('underline'), kwargs.get('underline', None))
        setattr(self, "_{}".format('value'), kwargs.get('value', None))
        setattr(self, "_{}".format('width'), kwargs.get('width', None))
        setattr(self, "_{}".format('x_position'), kwargs.get('x_position', None))
        setattr(self, "_{}".format('y_position'), kwargs.get('y_position', None))

    @property
    def anchor_case_sensitive(self):
        """Gets the anchor_case_sensitive of this Note.  # noqa: E501

        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.  # noqa: E501

        :return: The anchor_case_sensitive of this Note.  # noqa: E501
        :rtype: str
        """
        return self._anchor_case_sensitive

    @anchor_case_sensitive.setter
    def anchor_case_sensitive(self, anchor_case_sensitive):
        """Sets the anchor_case_sensitive of this Note.

        When set to **true**, the anchor string does not consider case when matching strings in the document. The default value is **true**.  # noqa: E501

        :param anchor_case_sensitive: The anchor_case_sensitive of this Note.  # noqa: E501
        :type: str
        """

        self._anchor_case_sensitive = anchor_case_sensitive

    @property
    def anchor_horizontal_alignment(self):
        """Gets the anchor_horizontal_alignment of this Note.  # noqa: E501

        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.  # noqa: E501

        :return: The anchor_horizontal_alignment of this Note.  # noqa: E501
        :rtype: str
        """
        return self._anchor_horizontal_alignment

    @anchor_horizontal_alignment.setter
    def anchor_horizontal_alignment(self, anchor_horizontal_alignment):
        """Sets the anchor_horizontal_alignment of this Note.

        Specifies the alignment of anchor tabs with anchor strings. Possible values are **left** or **right**. The default value is **left**.  # noqa: E501

        :param anchor_horizontal_alignment: The anchor_horizontal_alignment of this Note.  # noqa: E501
        :type: str
        """

        self._anchor_horizontal_alignment = anchor_horizontal_alignment

    @property
    def anchor_ignore_if_not_present(self):
        """Gets the anchor_ignore_if_not_present of this Note.  # noqa: E501

        When set to **true**, this tab is ignored if anchorString is not found in the document.  # noqa: E501

        :return: The anchor_ignore_if_not_present of this Note.  # noqa: E501
        :rtype: str
        """
        return self._anchor_ignore_if_not_present

    @anchor_ignore_if_not_present.setter
    def anchor_ignore_if_not_present(self, anchor_ignore_if_not_present):
        """Sets the anchor_ignore_if_not_present of this Note.

        When set to **true**, this tab is ignored if anchorString is not found in the document.  # noqa: E501

        :param anchor_ignore_if_not_present: The anchor_ignore_if_not_present of this Note.  # noqa: E501
        :type: str
        """

        self._anchor_ignore_if_not_present = anchor_ignore_if_not_present

    @property
    def anchor_match_whole_word(self):
        """Gets the anchor_match_whole_word of this Note.  # noqa: E501

        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.  # noqa: E501

        :return: The anchor_match_whole_word of this Note.  # noqa: E501
        :rtype: str
        """
        return self._anchor_match_whole_word

    @anchor_match_whole_word.setter
    def anchor_match_whole_word(self, anchor_match_whole_word):
        """Sets the anchor_match_whole_word of this Note.

        When set to **true**, the anchor string in this tab matches whole words only (strings embedded in other strings are ignored.) The default value is **true**.  # noqa: E501

        :param anchor_match_whole_word: The anchor_match_whole_word of this Note.  # noqa: E501
        :type: str
        """

        self._anchor_match_whole_word = anchor_match_whole_word

    @property
    def anchor_string(self):
        """Gets the anchor_string of this Note.  # noqa: E501

        Anchor text information for a radio button.  # noqa: E501

        :return: The anchor_string of this Note.  # noqa: E501
        :rtype: str
        """
        return self._anchor_string

    @anchor_string.setter
    def anchor_string(self, anchor_string):
        """Sets the anchor_string of this Note.

        Anchor text information for a radio button.  # noqa: E501

        :param anchor_string: The anchor_string of this Note.  # noqa: E501
        :type: str
        """

        self._anchor_string = anchor_string

    @property
    def anchor_units(self):
        """Gets the anchor_units of this Note.  # noqa: E501

        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.  # noqa: E501

        :return: The anchor_units of this Note.  # noqa: E501
        :rtype: str
        """
        return self._anchor_units

    @anchor_units.setter
    def anchor_units(self, anchor_units):
        """Sets the anchor_units of this Note.

        Specifies units of the X and Y offset. Units could be pixels, millimeters, centimeters, or inches.  # noqa: E501

        :param anchor_units: The anchor_units of this Note.  # noqa: E501
        :type: str
        """

        self._anchor_units = anchor_units

    @property
    def anchor_x_offset(self):
        """Gets the anchor_x_offset of this Note.  # noqa: E501

        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :return: The anchor_x_offset of this Note.  # noqa: E501
        :rtype: str
        """
        return self._anchor_x_offset

    @anchor_x_offset.setter
    def anchor_x_offset(self, anchor_x_offset):
        """Sets the anchor_x_offset of this Note.

        Specifies the X axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :param anchor_x_offset: The anchor_x_offset of this Note.  # noqa: E501
        :type: str
        """

        self._anchor_x_offset = anchor_x_offset

    @property
    def anchor_y_offset(self):
        """Gets the anchor_y_offset of this Note.  # noqa: E501

        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :return: The anchor_y_offset of this Note.  # noqa: E501
        :rtype: str
        """
        return self._anchor_y_offset

    @anchor_y_offset.setter
    def anchor_y_offset(self, anchor_y_offset):
        """Sets the anchor_y_offset of this Note.

        Specifies the Y axis location of the tab, in anchorUnits, relative to the anchorString.  # noqa: E501

        :param anchor_y_offset: The anchor_y_offset of this Note.  # noqa: E501
        :type: str
        """

        self._anchor_y_offset = anchor_y_offset

    @property
    def bold(self):
        """Gets the bold of this Note.  # noqa: E501

        When set to **true**, the information in the tab is bold.  # noqa: E501

        :return: The bold of this Note.  # noqa: E501
        :rtype: str
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """Sets the bold of this Note.

        When set to **true**, the information in the tab is bold.  # noqa: E501

        :param bold: The bold of this Note.  # noqa: E501
        :type: str
        """

        self._bold = bold

    @property
    def conditional_parent_label(self):
        """Gets the conditional_parent_label of this Note.  # noqa: E501

        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.  # noqa: E501

        :return: The conditional_parent_label of this Note.  # noqa: E501
        :rtype: str
        """
        return self._conditional_parent_label

    @conditional_parent_label.setter
    def conditional_parent_label(self, conditional_parent_label):
        """Sets the conditional_parent_label of this Note.

        For conditional fields this is the TabLabel of the parent tab that controls this tab's visibility.  # noqa: E501

        :param conditional_parent_label: The conditional_parent_label of this Note.  # noqa: E501
        :type: str
        """

        self._conditional_parent_label = conditional_parent_label

    @property
    def conditional_parent_value(self):
        """Gets the conditional_parent_value of this Note.  # noqa: E501

        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active.   # noqa: E501

        :return: The conditional_parent_value of this Note.  # noqa: E501
        :rtype: str
        """
        return self._conditional_parent_value

    @conditional_parent_value.setter
    def conditional_parent_value(self, conditional_parent_value):
        """Sets the conditional_parent_value of this Note.

        For conditional fields, this is the value of the parent tab that controls the tab's visibility.  If the parent tab is a Checkbox, Radio button, Optional Signature, or Optional Initial use \"on\" as the value to show that the parent tab is active.   # noqa: E501

        :param conditional_parent_value: The conditional_parent_value of this Note.  # noqa: E501
        :type: str
        """

        self._conditional_parent_value = conditional_parent_value

    @property
    def custom_tab_id(self):
        """Gets the custom_tab_id of this Note.  # noqa: E501

        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.  # noqa: E501

        :return: The custom_tab_id of this Note.  # noqa: E501
        :rtype: str
        """
        return self._custom_tab_id

    @custom_tab_id.setter
    def custom_tab_id(self, custom_tab_id):
        """Sets the custom_tab_id of this Note.

        The DocuSign generated custom tab ID for the custom tab to be applied. This can only be used when adding new tabs for a recipient. When used, the new tab inherits all the custom tab properties.  # noqa: E501

        :param custom_tab_id: The custom_tab_id of this Note.  # noqa: E501
        :type: str
        """

        self._custom_tab_id = custom_tab_id

    @property
    def document_id(self):
        """Gets the document_id of this Note.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this Note.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Note.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this Note.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def error_details(self):
        """Gets the error_details of this Note.  # noqa: E501


        :return: The error_details of this Note.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this Note.


        :param error_details: The error_details of this Note.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def font(self):
        """Gets the font of this Note.  # noqa: E501

        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.  # noqa: E501

        :return: The font of this Note.  # noqa: E501
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """Sets the font of this Note.

        The font to be used for the tab value. Supported Fonts: Arial, Arial, ArialNarrow, Calibri, CourierNew, Garamond, Georgia, Helvetica,   LucidaConsole, Tahoma, TimesNewRoman, Trebuchet, Verdana, MSGothic, MSMincho, Default.  # noqa: E501

        :param font: The font of this Note.  # noqa: E501
        :type: str
        """

        self._font = font

    @property
    def font_color(self):
        """Gets the font_color of this Note.  # noqa: E501

        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.  # noqa: E501

        :return: The font_color of this Note.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this Note.

        The font color used for the information in the tab.  Possible values are: Black, BrightBlue, BrightRed, DarkGreen, DarkRed, Gold, Green, NavyBlue, Purple, or White.  # noqa: E501

        :param font_color: The font_color of this Note.  # noqa: E501
        :type: str
        """

        self._font_color = font_color

    @property
    def font_size(self):
        """Gets the font_size of this Note.  # noqa: E501

        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.  # noqa: E501

        :return: The font_size of this Note.  # noqa: E501
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this Note.

        The font size used for the information in the tab.  Possible values are: Size7, Size8, Size9, Size10, Size11, Size12, Size14, Size16, Size18, Size20, Size22, Size24, Size26, Size28, Size36, Size48, or Size72.  # noqa: E501

        :param font_size: The font_size of this Note.  # noqa: E501
        :type: str
        """

        self._font_size = font_size

    @property
    def height(self):
        """Gets the height of this Note.  # noqa: E501

        Height of the tab in pixels.  # noqa: E501

        :return: The height of this Note.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Note.

        Height of the tab in pixels.  # noqa: E501

        :param height: The height of this Note.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def italic(self):
        """Gets the italic of this Note.  # noqa: E501

        When set to **true**, the information in the tab is italic.  # noqa: E501

        :return: The italic of this Note.  # noqa: E501
        :rtype: str
        """
        return self._italic

    @italic.setter
    def italic(self, italic):
        """Sets the italic of this Note.

        When set to **true**, the information in the tab is italic.  # noqa: E501

        :param italic: The italic of this Note.  # noqa: E501
        :type: str
        """

        self._italic = italic

    @property
    def merge_field(self):
        """Gets the merge_field of this Note.  # noqa: E501


        :return: The merge_field of this Note.  # noqa: E501
        :rtype: MergeField
        """
        return self._merge_field

    @merge_field.setter
    def merge_field(self, merge_field):
        """Sets the merge_field of this Note.


        :param merge_field: The merge_field of this Note.  # noqa: E501
        :type: MergeField
        """

        self._merge_field = merge_field

    @property
    def name(self):
        """Gets the name of this Note.  # noqa: E501

        Specifies the tool tip text for the tab.  # noqa: E501

        :return: The name of this Note.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Note.

        Specifies the tool tip text for the tab.  # noqa: E501

        :param name: The name of this Note.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def page_number(self):
        """Gets the page_number of this Note.  # noqa: E501

        Specifies the page number on which the tab is located.  # noqa: E501

        :return: The page_number of this Note.  # noqa: E501
        :rtype: str
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this Note.

        Specifies the page number on which the tab is located.  # noqa: E501

        :param page_number: The page_number of this Note.  # noqa: E501
        :type: str
        """

        self._page_number = page_number

    @property
    def recipient_id(self):
        """Gets the recipient_id of this Note.  # noqa: E501

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :return: The recipient_id of this Note.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this Note.

        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.  # noqa: E501

        :param recipient_id: The recipient_id of this Note.  # noqa: E501
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def shared(self):
        """Gets the shared of this Note.  # noqa: E501

        When set to **true**, this custom tab is shared.  # noqa: E501

        :return: The shared of this Note.  # noqa: E501
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Note.

        When set to **true**, this custom tab is shared.  # noqa: E501

        :param shared: The shared of this Note.  # noqa: E501
        :type: str
        """

        self._shared = shared

    @property
    def status(self):
        """Gets the status of this Note.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this Note.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Note.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this Note.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tab_group_labels(self):
        """Gets the tab_group_labels of this Note.  # noqa: E501

          # noqa: E501

        :return: The tab_group_labels of this Note.  # noqa: E501
        :rtype: list[str]
        """
        return self._tab_group_labels

    @tab_group_labels.setter
    def tab_group_labels(self, tab_group_labels):
        """Sets the tab_group_labels of this Note.

          # noqa: E501

        :param tab_group_labels: The tab_group_labels of this Note.  # noqa: E501
        :type: list[str]
        """

        self._tab_group_labels = tab_group_labels

    @property
    def tab_id(self):
        """Gets the tab_id of this Note.  # noqa: E501

        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].       # noqa: E501

        :return: The tab_id of this Note.  # noqa: E501
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        """Sets the tab_id of this Note.

        The unique identifier for the tab. The tabid can be retrieved with the [ML:GET call].       # noqa: E501

        :param tab_id: The tab_id of this Note.  # noqa: E501
        :type: str
        """

        self._tab_id = tab_id

    @property
    def tab_label(self):
        """Gets the tab_label of this Note.  # noqa: E501

        The label string associated with the tab.  # noqa: E501

        :return: The tab_label of this Note.  # noqa: E501
        :rtype: str
        """
        return self._tab_label

    @tab_label.setter
    def tab_label(self, tab_label):
        """Sets the tab_label of this Note.

        The label string associated with the tab.  # noqa: E501

        :param tab_label: The tab_label of this Note.  # noqa: E501
        :type: str
        """

        self._tab_label = tab_label

    @property
    def tab_order(self):
        """Gets the tab_order of this Note.  # noqa: E501

          # noqa: E501

        :return: The tab_order of this Note.  # noqa: E501
        :rtype: str
        """
        return self._tab_order

    @tab_order.setter
    def tab_order(self, tab_order):
        """Sets the tab_order of this Note.

          # noqa: E501

        :param tab_order: The tab_order of this Note.  # noqa: E501
        :type: str
        """

        self._tab_order = tab_order

    @property
    def template_locked(self):
        """Gets the template_locked of this Note.  # noqa: E501

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :return: The template_locked of this Note.  # noqa: E501
        :rtype: str
        """
        return self._template_locked

    @template_locked.setter
    def template_locked(self, template_locked):
        """Sets the template_locked of this Note.

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :param template_locked: The template_locked of this Note.  # noqa: E501
        :type: str
        """

        self._template_locked = template_locked

    @property
    def template_required(self):
        """Gets the template_required of this Note.  # noqa: E501

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :return: The template_required of this Note.  # noqa: E501
        :rtype: str
        """
        return self._template_required

    @template_required.setter
    def template_required(self, template_required):
        """Sets the template_required of this Note.

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :param template_required: The template_required of this Note.  # noqa: E501
        :type: str
        """

        self._template_required = template_required

    @property
    def tooltip(self):
        """Gets the tooltip of this Note.  # noqa: E501

          # noqa: E501

        :return: The tooltip of this Note.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this Note.

          # noqa: E501

        :param tooltip: The tooltip of this Note.  # noqa: E501
        :type: str
        """

        self._tooltip = tooltip

    @property
    def underline(self):
        """Gets the underline of this Note.  # noqa: E501

        When set to **true**, the information in the tab is underlined.  # noqa: E501

        :return: The underline of this Note.  # noqa: E501
        :rtype: str
        """
        return self._underline

    @underline.setter
    def underline(self, underline):
        """Sets the underline of this Note.

        When set to **true**, the information in the tab is underlined.  # noqa: E501

        :param underline: The underline of this Note.  # noqa: E501
        :type: str
        """

        self._underline = underline

    @property
    def value(self):
        """Gets the value of this Note.  # noqa: E501

        Specifies the value of the tab.   # noqa: E501

        :return: The value of this Note.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Note.

        Specifies the value of the tab.   # noqa: E501

        :param value: The value of this Note.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def width(self):
        """Gets the width of this Note.  # noqa: E501

        Width of the tab in pixels.  # noqa: E501

        :return: The width of this Note.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Note.

        Width of the tab in pixels.  # noqa: E501

        :param width: The width of this Note.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def x_position(self):
        """Gets the x_position of this Note.  # noqa: E501

        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :return: The x_position of this Note.  # noqa: E501
        :rtype: str
        """
        return self._x_position

    @x_position.setter
    def x_position(self, x_position):
        """Sets the x_position of this Note.

        This indicates the horizontal offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :param x_position: The x_position of this Note.  # noqa: E501
        :type: str
        """

        self._x_position = x_position

    @property
    def y_position(self):
        """Gets the y_position of this Note.  # noqa: E501

        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :return: The y_position of this Note.  # noqa: E501
        :rtype: str
        """
        return self._y_position

    @y_position.setter
    def y_position(self, y_position):
        """Sets the y_position of this Note.

        This indicates the vertical offset of the object on the page. DocuSign uses 72 DPI when determining position.  # noqa: E501

        :param y_position: The y_position of this Note.  # noqa: E501
        :type: str
        """

        self._y_position = y_position

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
        if issubclass(Note, dict):
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
        if not isinstance(other, Note):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Note):
            return True

        return self.to_dict() != other.to_dict()
