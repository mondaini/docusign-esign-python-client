# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import, print_function

import base64
import subprocess
from pprint import pprint
import unittest
import webbrowser

import docusign_esign as docusign
from docusign_esign import AuthenticationApi, EnvelopesApi, TemplatesApi, DiagnosticsApi
from docusign_esign.rest import ApiException

username = "node_sdk@mailinator.com"
password = "{PASSWORD}"
integrator_key = "ae30ea4e-xxxx-xxxx-xxxx-fcb57d2dc4df"
BASE_URL = "https://demo.docusign.net/restapi"

sign_test1_file = "test/docs/SignTest1.pdf"
template_id = "cf2a46c2-xxxx-xxxx-xxxx-752547b1a419"
envelope_id = "343cb64c-a7ca-416f-a412-2092e703bfd8"
user_id = "fcc5726c-xxxx-xxxx-xxxx-40bbbe6ca126"
oauth_base_url = "account-d.docusign.com" # use account.docusign.com for Live/Production
redirect_uri = "https://www.docusign.com/api"
private_key_filename = "test/keys/docusign_private_key.txt"

client_secret = "b4dccdbe-xxxx-xxxx-xxxx-b2f0f7448f8f"


class SdkUnitTests(unittest.TestCase):
    def setUp(self):
        self.api_client = docusign.ApiClient(BASE_URL)

        # IMPORTANT NOTE:
        # the first time you ask for a JWT access token, you should grant access by making the following call
        # get DocuSign OAuth authorization url:
        oauth_login_url = self.api_client.get_jwt_uri(integrator_key, redirect_uri, oauth_base_url)
        # open DocuSign OAuth authorization url in the browser, login and grant access
        # webbrowser.open_new_tab(oauth_login_url)
        print(oauth_login_url)
        # END OF NOTE

        # configure the ApiClient to asynchronously get an access to token and store it
        self.api_client.configure_jwt_authorization_flow(private_key_filename, oauth_base_url, integrator_key, user_id, 3600)

        docusign.configuration.api_client = self.api_client

    def tearDown(self):
        pass

    def testLogin(self):
        auth_api = AuthenticationApi()

        try:
            login_info = auth_api.login(api_password='true', include_account_id_guid='true')
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            print("LoginInformation: ", end="")
            pprint(login_info)

            # parse first account's baseUrl
            base_url, _ = login_accounts[0].base_url.split('/v2')

            # below code required for production, no effect in demo (same domain)
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception

    def testOAuthLogin(self):
        # create a separate api client for this test case
        api_client = docusign.ApiClient(BASE_URL)
        # make sure to pass the redirect uri
        api_client.configure_authorization_flow(integrator_key, client_secret, redirect_uri)

        # get DocuSign OAuth authorization url
        oauth_login_url = api_client.get_authorization_uri()
        # open DocuSign OAuth login in the browser
        print(oauth_login_url)
        # webbrowser.open_new_tab(oauth_login_url)

        # IMPORTANT NOTE: after the login, DocuSign will send back a fresh authorization code as a query param of the redirect URI.
        # You should set up a route that handles the redirect call to get that code and pass it to token endpoint as shown in the next lines:

        '''
        code = raw_input("Enter the authorization code here:")
        api_client.authenticate_with_code(code)

        auth_api = AuthenticationApi(api_client)

        try:
            login_info = auth_api.login(api_password='true', include_account_id_guid='true')
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            print("LoginInformation: ", end="")
            pprint(login_info)

            # parse first account's baseUrl
            base_url, _ = login_accounts[0].base_url.split('/v2')

            # below code required for production, no effect in demo (same domain)
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception
        '''

    def testRequestASignature(self):
        file_contents = open(sign_test1_file, 'rb').read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position =  '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        envelope_definition.status = 'sent'

        auth_api = AuthenticationApi()
        envelopes_api = EnvelopesApi()

        try:
            login_info = auth_api.login(api_password='true', include_account_id_guid='true')
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            envelope_summary = envelopes_api.create_envelope(login_accounts[0].account_id, envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None
            assert envelope_summary.status == 'sent'

            print("EnvelopeSummary: ", end="")
            pprint(envelope_summary)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception

    def testRequestSignatureFromTemplate(self):
        template_role_name = 'Needs to sign'

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # assign template information including ID and role(s)
        envelope_definition.template_id = template_id

        # create a template role with a valid templateId and roleName and assign signer info
        t_role = docusign.TemplateRole()
        t_role.role_name = template_role_name
        t_role.name ='Pat Developer'
        t_role.email = username

        # create a list of template roles and add our newly created role
        # assign template role(s) to the envelope
        envelope_definition.template_roles = [t_role]

        # send the envelope by setting |status| to "sent". To save as a draft set to "created"
        envelope_definition.status = 'sent'

        auth_api = AuthenticationApi()
        envelopes_api = EnvelopesApi()

        try:
            login_info = auth_api.login(api_password='true', include_account_id_guid='true')
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            envelope_summary = envelopes_api.create_envelope(login_accounts[0].account_id, envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None
            assert envelope_summary.status == 'sent'

            print("EnvelopeSummary: ", end="")
            pprint(envelope_summary)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception

    def testEmbeddedSigning(self):
        file_contents = open(sign_test1_file, 'rb').read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'
        signer.client_user_id = client_user_id

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position =  '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        envelope_definition.status = 'sent'

        auth_api = AuthenticationApi()
        envelopes_api = EnvelopesApi()

        try:
            login_info = auth_api.login()
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            envelope_summary = envelopes_api.create_envelope(login_accounts[0].account_id,
                                                             envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None
            assert envelope_summary.status == 'sent'

            print("EnvelopeSummary: ", end="")
            pprint(envelope_summary)

            return_url = 'http://www.docusign.com/developer-center'
            recipient_view_request = docusign.RecipientViewRequest()
            recipient_view_request.return_url = return_url
            recipient_view_request.client_user_id = client_user_id
            recipient_view_request.authentication_method = 'email'
            recipient_view_request.user_name = 'Pat Developer'
            recipient_view_request.email = username

            view_url = envelopes_api.create_recipient_view(login_accounts[0].account_id, envelope_summary.envelope_id, recipient_view_request=recipient_view_request)

            assert view_url is not None
            assert view_url.url is not None

            # This Url should work in an Iframe or browser to allow signing
            print("ViewUrl is ", end="")
            pprint(view_url)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception


    def testCreateTemplate(self):
        file_contents = open(sign_test1_file, 'rb').read()

        # create an envelope to be signed

        envelope_template = docusign.EnvelopeTemplate()
        envelope_template.email_subject = 'Please Sign my Python SDK Envelope (Embedded Signer)'
        envelope_template.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the template
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_template.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position =  '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_template.recipients = recipients

        env_template_definition = docusign.EnvelopeTemplateDefinition()
        env_template_definition.name = 'myTemplate'
        envelope_template.envelope_template_definition = env_template_definition

        auth_api = AuthenticationApi()
        templates_api = TemplatesApi()

        try:
            login_info = auth_api.login()
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            template_summary = templates_api.create_template(login_accounts[0].account_id, envelope_template=envelope_template)
            assert template_summary is not None
            assert template_summary.template_id is not None

            print("TemplateSummary: ", end="")
            pprint(template_summary)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception

    def testDownLoadEnvelopeDocuments(self):
        file_contents = open(sign_test1_file, 'rb').read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'
        signer.client_user_id = client_user_id

        # Create a Text tab somewhere on the document for the signer to sign
        text = docusign.Text()
        text.document_id = '1'
        text.page_number = '1'
        text.recipient_id = '1'
        text.x_position = '100'
        text.y_position =  '100'
        text.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.text_tabs = [text]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        # send the envelope (otherwise it will be "created" in the Draft folder)
        envelope_definition.status = 'sent'

        auth_api = AuthenticationApi()
        envelopes_api = EnvelopesApi()

        try:
            login_info = auth_api.login()
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            envelope_summary = envelopes_api.create_envelope(login_accounts[0].account_id, envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None

            print("EnvelopeSummary: ", end="")
            pprint(envelope_summary)

            file = envelopes_api.get_document(login_accounts[0].account_id, 'combined', envelope_summary.envelope_id)
            assert len(file) > 0
            subprocess.call('open ' + file, shell=True)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception

    def testListDocuments(self):
        auth_api = AuthenticationApi()
        envelopes_api = EnvelopesApi()

        try:
            login_info = auth_api.login()
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            docs_list = envelopes_api.list_documents(login_accounts[0].account_id, envelope_id)
            assert docs_list is not None
            assert (docs_list.envelope_id == envelope_id)

            print("EnvelopeDocumentsResult: ", end="")
            pprint(docs_list)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None  # make the test case fail in case of an API exception

    def testResendEnvelope(self):
        file_contents = open(sign_test1_file, 'rb').read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'
        signer.client_user_id = client_user_id

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position =  '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        # send the envelope (otherwise it will be "created" in the Draft folder)
        envelope_definition.status = 'sent'

        auth_api = AuthenticationApi()
        envelopes_api = EnvelopesApi()

        try:
            login_info = auth_api.login()
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            envelope_summary = envelopes_api.create_envelope(login_accounts[0].account_id, envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None

            print("EnvelopeSummary: ", end="")
            pprint(envelope_summary)

            recipients_update_summary = envelopes_api.update_recipients(login_accounts[0].account_id, envelope_summary.envelope_id, recipients=recipients, resend_envelope='true')
            assert recipients_update_summary is not None
            assert len(recipients_update_summary.recipient_update_results) > 0
            assert ("SUCCESS" == recipients_update_summary.recipient_update_results[0].error_details.error_code);
            print("RecipientsUpdateSummary: ", end="")
            pprint(recipients_update_summary)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception

    def testGetDiagnosticLogs(self):
        file_contents = open(sign_test1_file, 'rb').read()

        # create an envelope to be signed
        envelope_definition = docusign.EnvelopeDefinition()
        envelope_definition.email_subject = 'Please Sign my Python SDK Envelope'
        envelope_definition.email_blurb = 'Hello, Please sign my Python SDK Envelope.'

        # add a document to the envelope
        doc = docusign.Document()
        base64_doc = base64.b64encode(file_contents).decode("utf-8")
        doc.document_base64 = base64_doc
        doc.name = 'TestFile.pdf'
        doc.document_id = '1'
        envelope_definition.documents = [doc]

        # Add a recipient to sign the document
        signer = docusign.Signer()
        signer.email = username
        signer.name = 'Pat Developer'
        signer.recipient_id = '1'

        # this value represents the client's unique identifier for the signer
        client_user_id = '2939'
        signer.client_user_id = client_user_id

        # Create a SignHere tab somewhere on the document for the signer to sign
        sign_here = docusign.SignHere()
        sign_here.document_id = '1'
        sign_here.page_number = '1'
        sign_here.recipient_id = '1'
        sign_here.x_position = '100'
        sign_here.y_position =  '100'
        sign_here.scale_value = '0.5'

        tabs = docusign.Tabs()
        tabs.sign_here_tabs = [sign_here]
        signer.tabs = tabs

        recipients = docusign.Recipients()
        recipients.signers = [signer]
        envelope_definition.recipients = recipients

        # send the envelope (otherwise it will be "created" in the Draft folder)
        envelope_definition.status = 'sent'

        auth_api = AuthenticationApi()
        envelopes_api = EnvelopesApi()
        diag_api = DiagnosticsApi()

        try:
            login_info = auth_api.login()
            assert login_info is not None
            assert len(login_info.login_accounts) > 0
            login_accounts = login_info.login_accounts
            assert login_accounts[0].account_id is not None

            base_url, _ = login_accounts[0].base_url.split('/v2')
            self.api_client.host = base_url
            docusign.configuration.api_client = self.api_client

            diagnostics_settings_information = docusign.DiagnosticsSettingsInformation()
            diagnostics_settings_information.api_request_logging = 'true'
            diag_api.update_request_log_settings(diagnostics_settings_information=diagnostics_settings_information)

            envelope_summary = envelopes_api.create_envelope(login_accounts[0].account_id, envelope_definition=envelope_definition)
            assert envelope_summary is not None
            assert envelope_summary.envelope_id is not None

            print("EnvelopeSummary: ", end="")
            pprint(envelope_summary)

            file1 = envelopes_api.get_document(login_accounts[0].account_id, 'combined', envelope_summary.envelope_id)
            assert len(file1) > 0
            subprocess.call('open ' + file1, shell=True)

            logsList = diag_api.list_request_logs()
            request_log_id = logsList.api_request_logs[0].request_log_id
            file2 = diag_api.get_request_log(request_log_id)
            assert len(file2) > 0
            subprocess.call('open ' + file2, shell=True)

        except ApiException as e:
            print("\nException when calling DocuSign API: %s" % e)
            assert e is None # make the test case fail in case of an API exception

if __name__ == '__main__':
    unittest.main()
