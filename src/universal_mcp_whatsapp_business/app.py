from typing import Annotated, Any

from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration


class WhatsappBusinessApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='whatsappbusinessapp', integration=integration, **kwargs)
        self.base_url = "https://graph.facebook.com"

    def get_analytics(self, api_version: str, waba_id: str, fields: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Retrieve WhatsApp Business Account analytics data via the WABA Analytics API endpoints.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            waba_id: The WhatsApp Business Account ID.
            fields: Optional fields filter (Annotated[Any, '']) specifying which analytics metrics to return. Defaults to None, which typically returns all available fields through API defaults.

        Returns:
            Dictionary containing the requested analytics data, structured according to the API response format with string keys and dynamic values.

        Raises:
            HTTPError: If the API request fails due to network issues, invalid parameters, or authentication failures.

        Tags:
            analytics, waba, api-client, get, business-management, important
        """
        # Path: /{api-version}/{waba-id} (GET)
        path = f"/{api_version}/{waba_id}"
        url = f"{self.base_url}{path}"
        query_params = {
                "fields": fields,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_credit_lines(self, api_version: str, business_account_id: str) -> dict[str, Any]:
        """
        Retrieve credit line information from the Facebook Marketing API Business > Extendedcredits endpoint.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_account_id: The Business Account ID.

        Returns:
            A dictionary containing credit line details as returned by the API.

        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails with a 4XX/5XX status code.

        Tags:
            billing, api-client, facebook, marketing, important
        """
        # Path: /{api-version}/{business-account-id}/extendedcredits (GET)
        path = f"/{api_version}/{business_account_id}/extendedcredits"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_business_account_specific_fields(self, api_version: str, business_account_id: str, fields: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Retrieve business account data with specified fields from the Facebook Marketing API.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_account_id: The Business Account ID.
            fields: Comma-separated field names to include in the response (see API reference for available fields). If None, all available fields are returned by default.

        Returns:
            Dictionary containing the requested business account data from the API response.

        Raises:
            HTTPError: If the API request fails due to invalid parameters, authentication issues, or server errors.

        Tags:
            business, api, retrieve, fields, important
        """
        # Path: /{api-version}/{business-account-id} (GET)
        path = f"/{api_version}/{business_account_id}"
        url = f"{self.base_url}{path}"
        query_params = {
                "fields": fields,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_commerce_settings(self, api_version: str, business_phone_number_id: str) -> dict[str, Any]:
        """
        Retrieve the commerce settings configured for the WhatsApp Business account.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_phone_number_id: The WhatsApp Business Phone Number ID.

        Returns:
            A dictionary containing the commerce settings data, typically including payment configurations and product/service permissions.

        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails, such as due to network issues, invalid authentication, or server errors.

        Tags:
            commerce, retrieve, settings, important
        """
        # Path: /{api-version}/{business-phone-number-id}/whatsapp_commerce_settings (GET)
        path = f"/{api_version}/{business_phone_number_id}/whatsapp_commerce_settings"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_or_update_commerce_settings(self, api_version: str, business_phone_number_id: str, is_cart_enabled: Annotated[Any | None, ''] = None, is_catalog_visible: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Set or update WhatsApp commerce settings.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_phone_number_id: The WhatsApp Business Phone Number ID.
            is_cart_enabled: Optional boolean indicating whether the cart is enabled.
            is_catalog_visible: Optional boolean indicating whether the catalog is visible.

        Returns:
            A dictionary containing the updated commerce settings.

        Raises:
            HTTPError: Raised if the HTTP request fails, typically due to network errors or invalid responses.

        Tags:
            commerce, management, update, important
        """
        # Path: /{api-version}/{business-phone-number-id}/whatsapp_commerce_settings (POST)
        path = f"/{api_version}/{business_phone_number_id}/whatsapp_commerce_settings"
        url = f"{self.base_url}{path}"
        query_params = {
                "is_cart_enabled": is_cart_enabled,
                "is_catalog_visible": is_catalog_visible,
            }
        # Note: Schema defines these as query parameters for POST, which is followed here.
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, params=query_params) # Using params for query parameters
        response.raise_for_status()
        return response.json()

    def upload_media_step1_of2_create_session(self, api_version: str, app_id: str, file_length: Annotated[Any | None, 'File size, in bytes'] = None, file_type: Annotated[Any | None, 'File MIME type (e.g. image/jpg)'] = None) -> dict[str, Any]:
        """
        Initiates a resumable media upload session by creating an upload session ID and preparing the endpoint.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            app_id: The Application ID.
            file_length: File size in bytes (required for resumable upload API)
            file_type: File MIME type (e.g. 'image/jpg', required for content validation)

        Returns:
            dict[str, Any]: Upload session metadata including upload URL and session ID

        Raises:
            requests.HTTPError: Raised for 4XX/5XX status codes during API communication

        Tags:
            media, upload, async-job, api, management, important
        """
        # Path: /{api-version}/{app-id}/uploads (POST)
        path = f"/{api_version}/{app_id}/uploads"
        url = f"{self.base_url}{path}"
        query_params = {
                "file_length": file_length,
                "file_type": file_type,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def upload_media_step2_of2_initiate_upload(self, api_version: str, session_id: str, file_offset: Annotated[Any, 'Offset in bytes for resumable upload'] = 0, request_body: Annotated[Any, 'Raw file content bytes'] = None) -> dict[str, Any]:
        """
        Initiates a media upload to a server using a resumable upload API.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            session_id: The upload session ID obtained from step 1.
            file_offset: Offset in bytes for the resumable upload (usually 0 for the first chunk).
            request_body: An optional annotated dictionary with the upload payload (default is None), ideally raw bytes for file content.

        Returns:
            A dictionary containing the server's response.

        Raises:
            requests.HTTPError: Raised if the server responds with an unsuccessful status code.

        Tags:
            upload, media, important
        """
        # Path: /{api-version}/<SESSION_ID> (POST)
        path = f"/{api_version}/{session_id}"
        url = f"{self.base_url}{path}"
        query_params = {} # Schema defines no query params for POST
        headers = {"file_offset": str(file_offset)} # Schema defines file_offset as a header

        # request_body should likely be raw file content bytes
        response = self._post(url, data=request_body, params=query_params, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_business_phone_number(self, api_version: str, business_phone_number_id: str, fields: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Retrieves the business phone number for the associated WhatsApp Business Account.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_phone_number_id: The WhatsApp Business Phone Number ID.
            fields: Optional field specifying which fields to include in the response. Defaults to None.

        Returns:
            A dictionary containing the phone number details.

        Raises:
            HTTPError: If the HTTP request returns an unsuccessful status code.

        Tags:
            phone-numbers, whatsapp-business, management-api, important
        """
        # Path: /{api-version}/{business-phone-number-id} (GET)
        path = f"/{api_version}/{business_phone_number_id}"
        url = f"{self.base_url}{path}"
        query_params = {
                "fields": fields,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_business_phone_numbers(self, api_version: str, waba_id: str, fields: Annotated[Any | None, ''] = None, filtering: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Retrieves all business phone numbers, optionally filtering by specified fields or criteria.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            waba_id: The WhatsApp Business Account ID.
            fields: Optional fields to include in the response.
            filtering: Optional filtering criteria for the phone numbers.

        Returns:
            A dictionary containing the API response with a 'data' key containing a list of all business phone numbers.

        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.

        Tags:
            phone-numbers, management, important, api-request
        """
        # Path: /{api-version}/{waba-id}/phone_numbers (GET)
        path = f"/{api_version}/{waba_id}/phone_numbers"
        url = f"{self.base_url}{path}"
        query_params = {
                "fields": fields,
                "filtering": filtering,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_qr_code(self, api_version: str, business_phone_number_id: str, qr_code_id: str) -> dict[str, Any]:
        """
        Retrieves QR code information from the WhatsApp Business API for the associated business account.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_phone_number_id: The WhatsApp Business Phone Number ID.
            qr_code_id: The ID of the specific QR code to retrieve.

        Returns:
            A dictionary containing QR code details from the API response, including configuration data and expiry information

        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails, typically due to invalid credentials, network issues, or server errors

        Tags:
            qr-code, api, whatsapp, business, retrieve, important
        """
        # Path: /{api-version}/{business-phone-number-id}/message_qrdls/<QR_CODE_ID> (GET)
        path = f"/{api_version}/{business_phone_number_id}/message_qrdls/{qr_code_id}"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_qr_code(self, api_version: str, business_phone_number_id: str, qr_code_id: str) -> dict[str, Any]:
        """
        Deletes a QR code from the WhatsApp Business API.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_phone_number_id: The WhatsApp Business Phone Number ID.
            qr_code_id: The ID of the specific QR code to delete.

        Returns:
            A dictionary containing the result of the QR code deletion.

        Raises:
            requests.exceptions.HTTPError: Raised if an HTTP error occurs during the request.

        Tags:
            delete, qr-code, whatsapp, important
        """
        # Path: /{api-version}/{business-phone-number-id}/message_qrdls/<QR_CODE_ID> (DELETE)
        path = f"/{api_version}/{business_phone_number_id}/message_qrdls/{qr_code_id}"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_qr_codes_default_fields(self, api_version: str, business_phone_number_id: str, code: Annotated[Any | None, ''] = None, fields: Annotated[Any | None, '.format can be SVG or PNG'] = None) -> dict[str, Any]:
        """
        Retrieves QR codes with default fields from the WhatsApp Business API.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_phone_number_id: The WhatsApp Business Phone Number ID.
            code: Optional filter parameter to specify QR codes by code identifier
            fields: Optional format specification for QR code output (e.g., SVG or PNG)

        Returns:
            Dictionary containing the API response data with QR code information

        Raises:
            requests.HTTPError: Raised when the API request fails due to HTTP errors (4XX/5XX status codes)

        Tags:
            qr-codes, retrieve, management, api, important
        """
        # Path: /{api-version}/{business-phone-number-id}/message_qrdls (GET)
        path = f"/{api_version}/{business_phone_number_id}/message_qrdls"
        url = f"{self.base_url}{path}"
        query_params = {
                "fields": fields,
                "code": code,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        # Schema has requestBody defined for GET, but it's empty and unusual for GET. Removed request_body from call.
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_qr_code(self, api_version: str, business_phone_number_id: str, code: Annotated[Any | None, ''] = None, prefilled_message: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Creates a QR code based on the provided code and prefilled message.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_phone_number_id: The WhatsApp Business Phone Number ID.
            code: Optional code to include in the QR code. Defaults to None.
            prefilled_message: Optional prefilled message to include in the QR code. Defaults to None.

        Returns:
            A dictionary containing the response after creating the QR code.

        Raises:
            requests.HTTPError: Raised if there is an issue with the HTTP request, such as an invalid response status.

        Tags:
            qr-code, whatsapp, important
        """
        # Path: /{api-version}/{business-phone-number-id}/message_qrdls (POST)
        path = f"/{api_version}/{business_phone_number_id}/message_qrdls"
        url = f"{self.base_url}{path}"
        query_params = {} # Schema defines no query params for POST
        request_body = {
            "code": code,
            "prefilled_message": prefilled_message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        response = self._post(url, json=request_body, params=query_params) # Using json for request body
        response.raise_for_status()
        return response.json()

    def get_template_by_id_default_fields(self, api_version: str, template_id: str) -> dict[str, Any]:
        """
        Retrieves a WhatsApp message template by ID, including default fields.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            template_id: The ID of the specific message template to retrieve.

        Returns:
            A dictionary with template data.

        Raises:
            requests.HTTPError: Raised when there's an issue with the HTTP request status, such as a non-successful status code.

        Tags:
            templates, whatsapp, message-templates, important
        """
        # Path: /{api-version}/<TEMPLATE_ID> (GET)
        path = f"/{api_version}/{template_id}"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def edit_template(self, api_version: str, template_id: str, category: Annotated[Any | None, ''] = None, components: Annotated[list[Any] | None, ''] = None, language: Annotated[Any | None, ''] = None, name: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Edits a template by sending a POST request with the specified parameters.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            template_id: The ID of the specific message template to edit.
            category: Optional category for the template.
            components: Optional components for the template.
            language: Optional language for the template.
            name: Optional name for the template.

        Returns:
            A dictionary containing the response data from the POST request.

        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.

        Tags:
            edit, template, management, important
        """
        # Path: /{api-version}/<TEMPLATE_ID> (POST)
        path = f"/{api_version}/{template_id}"
        url = f"{self.base_url}{path}"
        query_params = {} # Schema defines no query params for POST
        request_body = {
            "category": category,
            "components": components,
            "language": language,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        response = self._post(url, json=request_body, params=query_params) # Using json for request body
        response.raise_for_status()
        return response.json()

    def get_template_by_name_default_fields(self, api_version: str, waba_id: str, name: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Retrieves a WhatsApp message template by name using default fields from the WhatsApp Business Account API.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            waba_id: The WhatsApp Business Account ID.
            name: Name of the template to retrieve. If None, returns templates without name filtering.

        Returns:
            Dictionary containing template data as returned by the WhatsApp Business Account API.

        Raises:
            HTTPError: If the API request fails (e.g., invalid credentials, template not found).

        Tags:
            templates, whatsapp, api, management, important
        """
        # Path: /{api-version}/{waba-id}/message_templates (GET)
        path = f"/{api_version}/{waba_id}/message_templates"
        url = f"{self.base_url}{path}"
        query_params = {
                "name": name,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_authentication_template_wotp_copy_code_button(self, api_version: str, waba_id: str, category: Annotated[Any | None, ''] = None, components: Annotated[list[Any] | None, ''] = None, language: Annotated[Any | None, ''] = None, name: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Creates an authentication message template with an OTP copy code button for WhatsApp Business API.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            waba_id: The WhatsApp Business Account ID.
            category: Template category (e.g., authentication, marketing). Required by WhatsApp's template guidelines.
            components: List containing structured components for the template, including the OTP button configuration.
            language: Language code for the template (e.g., 'en_US' for English-US).
            name: Unique identifier name for the template.

        Returns:
            Dictionary containing the API response data, typically including template approval status and template ID.

        Raises:
            HTTPError: Raised if the API request fails (e.g., invalid parameters, authentication issues, or server errors).

        Tags:
            authentication, templates, whatsapp-api, async-job, important
        """
        # Path: /{api-version}/{waba-id}/message_templates (POST)
        path = f"/{api_version}/{waba_id}/message_templates"
        url = f"{self.base_url}{path}"
        query_params = {} # Schema defines no query params for POST
        request_body = {
            "category": category,
            "components": components,
            "language": language,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        response = self._post(url, json=request_body, params=query_params) # Using json for request body
        response.raise_for_status()
        return response.json()

    def delete_template_by_name(self, api_version: str, waba_id: str, hsm_id: Annotated[Any | None, 'Template ID'] = None, name: Annotated[Any | None, ''] = None) -> dict[str, Any]:
        """
        Deletes a message template by name from a WhatsApp Business API account.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            waba_id: The WhatsApp Business Account ID.
            hsm_id: Optional template ID for filtering (or deletion target if name is not used).
            name: Optional template name used for deletion (or filtering if hsm_id is not used).

        Returns:
            A dictionary containing the response from the deletion request.

        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as network errors or invalid server responses.

        Tags:
            delete, templates, whatsapp-api, management, important
        """
        # Path: /{api-version}/{waba-id}/message_templates (DELETE)
        path = f"/{api_version}/{waba_id}/message_templates"
        url = f"{self.base_url}{path}"
        query_params = {
                "name": name,
                "hsm_id": hsm_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_apps_subscribed_to_waba_swebhooks(self, api_version: str, waba_id: str) -> dict[str, Any]:
        """
        Retrieve all apps subscribed to WABA's webhooks.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            waba_id: The WhatsApp Business Account ID.

        Returns:
            A dictionary mapping app identities to their details, represented as Any.

        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as network errors or invalid responses.

        Tags:
            list, management, webhooks, waba, important
        """
        # Path: /{api-version}/{waba-id}/subscribed_apps (GET)
        path = f"/{api_version}/{waba_id}/subscribed_apps"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscribe_app_to_waba_swebhooks(self, api_version: str, waba_id: str) -> dict[str, Any]:
        """
        Subscribe an application to WhatsApp Business Account (WABA) webhooks.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            waba_id: The WhatsApp Business Account ID.

        Returns:
            A dictionary containing the subscription response from the WABA API.

        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request to subscribe the app fails.

        Tags:
            subscribe, webhooks, waba, important
        """
        # Path: /{api-version}/{waba-id}/subscribed_apps (POST)
        path = f"/{api_version}/{waba_id}/subscribed_apps"
        url = f"{self.base_url}{path}"
        query_params = {} # Schema defines no query params for POST
        response = self._post(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def unsubscribe_app_from_waba_swebhooks(self, api_version: str, waba_id: str) -> dict[str, Any]:
        """
        Unsubscribes the app from WhatsApp Business Account (WABA) webhooks, removing all existing subscriptions.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            waba_id: The WhatsApp Business Account ID.

        Returns:
            dict[str, Any]: Response data from the API containing operation results or confirmation details

        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails (e.g., network issues, invalid credentials, or resource not found)

        Tags:
            webhooks, unsubscribe, whatsapp, api, management, important
        """
        # Path: /{api-version}/{waba-id}/subscribed_apps (DELETE)
        path = f"/{api_version}/{waba_id}/subscribed_apps"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_shared_wabas(self, api_version: str, business_account_id: str) -> dict[str, Any]:
        """
        Retrieve all shared WhatsApp Business Accounts (WABAs) associated with the authenticated business.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_account_id: The Business Account ID.

        Returns:
            Dict[str, Any]: A dictionary containing the API response data, typically including WABA details and associated metadata.

        Raises:
            HTTPError: Raised if the API request fails due to network issues, authorization errors, or invalid endpoint parameters.

        Tags:
            whatsapp, waba, list, retrieve, business, api, important
        """
        # Path: /{api-version}/{business-account-id}/client_whatsapp_business_accounts (GET)
        path = f"/{api_version}/{business_account_id}/client_whatsapp_business_accounts"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_owned_wabas(self, api_version: str, business_account_id: str) -> dict[str, Any]:
        """
        Retrieves all owned WhatsApp Business Accounts (WABAs) through an API request.

        Args:
            api_version: The API version to use (e.g., 'v16.0').
            business_account_id: The Business Account ID.

        Returns:
            A dictionary containing the API response data with WABA details, typically including account IDs, statuses, and ownership metadata.

        Raises:
            HTTPError: Raised when the API request fails, including scenarios like invalid authentication, network issues, or server errors (handled by response.raise_for_status()).

        Tags:
            waba, management, api-request, important
        """
        # Path: /{api-version}/{business-account-id}/owned_whatsapp_business_accounts (GET)
        path = f"/{api_version}/{business_account_id}/owned_whatsapp_business_accounts"
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()


    def list_tools(self):
        return [
            self.get_analytics,
            self.get_credit_lines,
            self.get_business_account_specific_fields,
            self.get_commerce_settings,
            self.set_or_update_commerce_settings,
            self.upload_media_step1_of2_create_session,
            self.upload_media_step2_of2_initiate_upload,
            self.get_business_phone_number,
            self.get_all_business_phone_numbers,
            self.get_qr_code,
            self.delete_qr_code,
            self.get_all_qr_codes_default_fields,
            self.create_qr_code,
            self.get_template_by_id_default_fields,
            self.edit_template,
            self.get_template_by_name_default_fields,
            self.create_authentication_template_wotp_copy_code_button,
            self.delete_template_by_name,
            self.get_all_apps_subscribed_to_waba_swebhooks,
            self.subscribe_app_to_waba_swebhooks,
            self.unsubscribe_app_from_waba_swebhooks,
            self.get_all_shared_wabas,
            self.get_all_owned_wabas
        ]
