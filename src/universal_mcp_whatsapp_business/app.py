from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class WhatsappBusinessApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='whatsapp-business', integration=integration, **kwargs)
        self.base_url = "https://graph.facebook.com"

    def get_analytics(self, api_version, waba_id, fields=None) -> dict[str, Any]:
        """
        Retrieves details of a specified WhatsApp Business Account (WABA) with customizable fields using the GET method.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            fields (string): Specifies which fields to include/exclude in the response for the WhatsApp Business Account resource. Example: 'analytics.start(1680503760).end(1680564980).granularity(DAY).phone_numbers([]).country_codes(["US", "BR"])'.

        Returns:
            dict[str, Any]: Example reponse / Example response / Example response / Example response

        Tags:
            WhatsApp Business Accounts (WABA)
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'")
        url = f"{self.base_url}/{api_version}/{waba_id}"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_credit_lines(self, api_version, business_account_id) -> dict[str, Any]:
        """
        Retrieves the extended credit lines available for a specified business account using its ID.

        Args:
            api_version (string): api-version
            business_account_id (string): business-account-id

        Returns:
            dict[str, Any]: Example response

        Tags:
            Billing
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_account_id is None:
            raise ValueError("Missing required parameter 'business-account-id'")
        url = f"{self.base_url}/{api_version}/{business_account_id}/extendedcredits"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_business_account_specific_fields(self, api_version, business_account_id, fields=None) -> dict[str, Any]:
        """
        Retrieves information about a business account using the specified API version and business account ID, optionally filtering the response fields via a query parameter.

        Args:
            api_version (string): api-version
            business_account_id (string): business-account-id
            fields (string): Specifies the fields to include in the response, reducing payload size by returning only the requested data. Example: 'id,name,timezone_id'.

        Returns:
            dict[str, Any]: Example response

        Tags:
            Business accounts, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_account_id is None:
            raise ValueError("Missing required parameter 'business-account-id'")
        url = f"{self.base_url}/{api_version}/{business_account_id}"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_commerce_settings(self, api_version, business_phone_number_id) -> dict[str, Any]:
        """
        Retrieves the commerce settings configured for a specific WhatsApp Business phone number.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id

        Returns:
            dict[str, Any]: Example response

        Tags:
            Commerce
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/whatsapp_commerce_settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def set_or_update_commerce_settings(self, api_version, business_phone_number_id, is_cart_enabled=None, is_catalog_visible=None) -> dict[str, Any]:
        """
        Updates WhatsApp Business commerce settings (cart availability and catalog visibility) for a specific business phone number.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id
            is_cart_enabled (string): Indicates whether the shopping cart is enabled or disabled for the specified WhatsApp commerce settings. Example: 'true'.
            is_catalog_visible (string): Determines whether the business's product catalog is visible to customers in WhatsApp conversations. Example: 'true'.

        Returns:
            dict[str, Any]: Example response

        Tags:
            Commerce
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/whatsapp_commerce_settings"
        query_params = {k: v for k, v in [('is_cart_enabled', is_cart_enabled), ('is_catalog_visible', is_catalog_visible)] if v is not None}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def upload_media_step1_of2_create_session(self, api_version, app_id, file_length=None, file_type=None) -> dict[str, Any]:
        """
        Uploads a file using the specified API version and application ID, with optional query parameters for file length and type, and returns a successful status message upon completion.

        Args:
            api_version (string): api-version
            app_id (string): app-id
            file_length (string): File size, in bytes Example: '<FILE_SIZE>'.
            file_type (string): File MIME type (e.g. image/jpg) Example: '<MIME_TYPE>'.

        Returns:
            dict[str, Any]: Step 1 example response

        Tags:
            Media
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if app_id is None:
            raise ValueError("Missing required parameter 'app-id'")
        url = f"{self.base_url}/{api_version}/{app_id}/uploads"
        query_params = {k: v for k, v in [('file_length', file_length), ('file_type', file_type)] if v is not None}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def upload_media_step2_of2_initiate_upload(self, api_version, request_body=None) -> dict[str, Any]:
        """
        Initiates a session using the provided SESSION_ID and file offset specified in the header, supporting further session-related operations via the POST method at the "/{api-version}/<SESSION_ID>" endpoint.

        Args:
            api_version (string): api-version
            request_body (dict | None): Optional dictionary for arbitrary request body data.

        Returns:
            dict[str, Any]: Step 2 example response

        Tags:
            Media, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        url = f"{self.base_url}/{api_version}/<SESSION_ID>"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_business_phone_number(self, api_version, business_phone_number_id, fields=None) -> dict[str, Any]:
        """
        Retrieves details for a specific business phone number ID using query parameters to specify returned fields.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id
            fields (string): Specifies which fields to include in the response for the business phone number. Example: 'id,display_phone_number,name_status'.

        Returns:
            dict[str, Any]: Example response / Example response

        Tags:
            Phone numbers
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}"
        query_params = {k: v for k, v in [('fields', fields)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_business_phone_numbers(self, api_version, waba_id, fields=None, filtering=None) -> list[Any]:
        """
        Retrieves a list of phone numbers associated with a specific WhatsApp Business Account (WABA), allowing for filtering and customization of the response fields.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            fields (string): Optional parameter to specify which fields should be included in the response for phone numbers associated with a WABA, allowing customization of the returned data. Example: 'id,is_official_business_account,display_phone_number,verified_name'.
            filtering (string): Specifies query parameters to filter phone numbers based on specific criteria for the GET operation. Example: "[{'field':'account_mode','operator':'EQUAL','value':'SANDBOX'}]".

        Returns:
            list[Any]: Example response

        Tags:
            Phone numbers
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'")
        url = f"{self.base_url}/{api_version}/{waba_id}/phone_numbers"
        query_params = {k: v for k, v in [('fields', fields), ('filtering', filtering)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_qr_code(self, api_version, business_phone_number_id) -> dict[str, Any]:
        """
        Retrieves a message linked to a specific QR code for a business phone number using the GET method via the API.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id

        Returns:
            dict[str, Any]: Example Response

        Tags:
            QR codes
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/message_qrdls/<QR_CODE_ID>"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_qr_code(self, api_version, business_phone_number_id) -> dict[str, Any]:
        """
        Deletes a specific WhatsApp Business QR code using the provided QR code ID and returns a success message if the operation is completed successfully.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id

        Returns:
            dict[str, Any]: Example Response

        Tags:
            QR codes
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/message_qrdls/<QR_CODE_ID>"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_qr_codes_default_fields(self, api_version, business_phone_number_id, fields=None, code=None) -> dict[str, Any]:
        """
        Retrieves a list of message QR code deep links associated with a business phone number, filtered by specified fields and QR code identifiers.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id
            fields (string): .format can be SVG or PNG Example: 'code,prefilled_message,qr_image_url.format(SVG)'.
            code (string): The unique identifier code used to filter messages associated with the specified business phone number. Example: '<QR_CODE_ID>'.

        Returns:
            dict[str, Any]: Example Response / Example Response / Example Response / Example Response

        Tags:
            QR codes
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'")
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/message_qrdls"
        query_params = {k: v for k, v in [('fields', fields), ('code', code)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_qr_code(self, api_version, business_phone_number_id, code=None, prefilled_message=None) -> dict[str, Any]:
        """
        Creates a WhatsApp Business QR code with a predefined message and returns the generated code details.

        Args:
            api_version (string): api-version
            business_phone_number_id (string): business-phone-number-id
            code (string): code Example: 'WOMVT6TJ2BP7A1'.
            prefilled_message (string): prefilled_message
                Example:
                ```json
                {
                  "generate_qr_image": "SVG",
                  "prefilled_message": "Show me Cyber Monday deals!"
                }
                ```

        Returns:
            dict[str, Any]: Example Response / Example Response

        Tags:
            QR codes
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_phone_number_id is None:
            raise ValueError("Missing required parameter 'business-phone-number-id'")
        request_body = {
            'code': code,
            'prefilled_message': prefilled_message,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/{api_version}/{business_phone_number_id}/message_qrdls"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_by_id_default_fields(self, api_version) -> dict[str, Any]:
        """
        Retrieves a template using the specified template ID from the API version path.

        Args:
            api_version (string): api-version

        Returns:
            dict[str, Any]: Example response

        Tags:
            Templates
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        url = f"{self.base_url}/{api_version}/<TEMPLATE_ID>"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def edit_template(self, api_version, category=None, components=None, language=None, name=None) -> dict[str, Any]:
        """
        Creates or processes a resource using the specified template ID based on the API version and returns a successful status upon completion.

        Args:
            api_version (string): api-version
            category (string): category Example: 'MARKETING'.
            components (array): components Example: "[{'format': 'TEXT', 'text': 'Fall Sale', 'type': 'HEADER'}, {'example': {'body_text': [['Mark', 'FALL25']]}, 'text': 'Hi {{1}}, our Fall Sale is on! Use promo code {{2}} Get an extra 25% off every order above $350!', 'type': 'BODY'}, {'text': 'Not interested in any of our sales? Tap Stop Promotions', 'type': 'FOOTER'}, {'buttons': [{'text': 'Stop promotions', 'type': 'QUICK_REPLY'}], 'type': 'BUTTONS'}]".
            language (string): language Example: 'en_US'.
            name (string): name
                Example:
                ```json
                {
                  "category": "MARKETING",
                  "components": [
                    {
                      "format": "TEXT",
                      "text": "Fall Sale",
                      "type": "HEADER"
                    },
                    {
                      "example": {
                        "body_text": [
                          [
                            "Mark",
                            "FALL25"
                          ]
                        ]
                      },
                      "text": "Hi {{1}}, our Fall Sale is on! Use promo code {{2}} Get an extra 25% off every order above $350!",
                      "type": "BODY"
                    },
                    {
                      "text": "Not interested in any of our sales? Tap Stop Promotions",
                      "type": "FOOTER"
                    },
                    {
                      "buttons": [
                        {
                          "text": "Stop promotions",
                          "type": "QUICK_REPLY"
                        }
                      ],
                      "type": "BUTTONS"
                    }
                  ],
                  "language": "en_US",
                  "name": "2023_april_promo"
                }
                ```

        Returns:
            dict[str, Any]: Example response

        Tags:
            Templates
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        request_body = {
            'category': category,
            'components': components,
            'language': language,
            'name': name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/{api_version}/<TEMPLATE_ID>"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_template_by_name_default_fields(self, api_version, waba_id, name=None) -> dict[str, Any]:
        """
        Retrieves a list of WhatsApp message templates associated with a specific WhatsApp Business Account using the "GET" method, allowing filtering by template name.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            name (string): Filters message templates by exact name match. Example: '<TEMPLATE_NAME>'.

        Returns:
            dict[str, Any]: Example response / Example response

        Tags:
            Templates, important
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'")
        url = f"{self.base_url}/{api_version}/{waba_id}/message_templates"
        query_params = {k: v for k, v in [('name', name)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_authentication_template_wotp_copy_code_button(self, api_version, waba_id, category=None, components=None, language=None, name=None) -> dict[str, Any]:
        """
        Creates a new WhatsApp message template for a business account, allowing businesses to send standardized messages to customers.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            category (string): category Example: 'UTILITY'.
            components (array): components Example: "[{'example': {'header_handle': ['4::YXBwbGljYXRpb24vcGRm:ARZVv4zuogJMxmAdS3_6T4o_K4ll2806avA7rWpikisTzYPsXXUeKk0REjS-hIM1rYrizHD7rQXj951TKgUFblgd_BDWVROCwRkg9Vhjj-cHNQ:e:1681237341:634974688087057:100089620928913:ARa1ZDhwbLZM3EENeeg']}, 'format': 'DOCUMENT', 'type': 'HEADER'}, {'example': {'body_text': [['Mark', '860198-230332']]}, 'text': 'Thank you for your order, {{1}}! Your order number is {{2}}. Tap the PDF linked above to view your receipt. If you have any questions, please use the buttons below to contact support. Thanks again!', 'type': 'BODY'}, {'buttons': [{'phone_number': '16467043595', 'text': 'Call', 'type': 'PHONE_NUMBER'}, {'text': 'Contact Support', 'type': 'URL', 'url': 'https://www.examplesite.com/support'}], 'type': 'BUTTONS'}]".
            language (string): language Example: 'en_US'.
            name (string): name
                Example:
                ```json
                {
                  "category": "AUTHENTICATION",
                  "components": [
                    {
                      "add_security_recommendation": true,
                      "type": "BODY"
                    },
                    {
                      "code_expiration_minutes": 10,
                      "type": "FOOTER"
                    },
                    {
                      "buttons": [
                        {
                          "otp_type": "COPY_CODE",
                          "text": "Copy Code",
                          "type": "OTP"
                        }
                      ],
                      "type": "BUTTONS"
                    }
                  ],
                  "language": "en_US",
                  "name": "authentication_code_copy_code_button"
                }
                ```

        Returns:
            dict[str, Any]: Example response / Example response / Example response / Example response / Example response / Example response / Example response / Example response

        Tags:
            Templates
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'")
        request_body = {
            'category': category,
            'components': components,
            'language': language,
            'name': name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/{api_version}/{waba_id}/message_templates"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_template_by_name(self, api_version, waba_id, name=None, hsm_id=None) -> dict[str, Any]:
        """
        Deletes WhatsApp message templates by name (all languages) or specific ID using query parameters and returns a success status.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id
            name (string): The name of the message template to delete. Example: '<TEMPLATE_NAME>'.
            hsm_id (string): Template ID Example: '<HSM_ID>'.

        Returns:
            dict[str, Any]: Example response / Example response

        Tags:
            Templates
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'")
        url = f"{self.base_url}/{api_version}/{waba_id}/message_templates"
        query_params = {k: v for k, v in [('name', name), ('hsm_id', hsm_id)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_apps_subscribed_to_waba_swebhooks(self, api_version, waba_id) -> dict[str, Any]:
        """
        Retrieves a list of apps subscribed to webhooks for a WhatsApp Business Account using the GET method.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id

        Returns:
            dict[str, Any]: Example response

        Tags:
            Webhooks
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'")
        url = f"{self.base_url}/{api_version}/{waba_id}/subscribed_apps"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def subscribe_app_to_waba_swebhooks(self, api_version, waba_id) -> dict[str, Any]:
        """
        Subscribes an app to webhooks for a WhatsApp Business Account (WABA) using the POST method at the `/subscribed_apps` endpoint, allowing the app to receive updates and notifications from the WABA.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id

        Returns:
            dict[str, Any]: Example response

        Tags:
            Webhooks
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'")
        url = f"{self.base_url}/{api_version}/{waba_id}/subscribed_apps"
        query_params = {}
        response = self._post(url, data={}, params=query_params)
        response.raise_for_status()
        return response.json()

    def unsubscribe_app_from_waba_swebhooks(self, api_version, waba_id) -> dict[str, Any]:
        """
        Unsubscribes an app from webhook notifications for a WhatsApp Business Account.

        Args:
            api_version (string): api-version
            waba_id (string): waba-id

        Returns:
            dict[str, Any]: Example response

        Tags:
            Webhooks
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if waba_id is None:
            raise ValueError("Missing required parameter 'waba-id'")
        url = f"{self.base_url}/{api_version}/{waba_id}/subscribed_apps"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_shared_wabas(self, api_version, business_account_id) -> Any:
        """
        Retrieves information about WhatsApp Business accounts associated with a business client, using the specified business account ID and API version.

        Args:
            api_version (string): api-version
            business_account_id (string): business-account-id

        Returns:
            Any: API response data.

        Tags:
            WhatsApp Business Accounts (WABA)
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_account_id is None:
            raise ValueError("Missing required parameter 'business-account-id'")
        url = f"{self.base_url}/{api_version}/{business_account_id}/client_whatsapp_business_accounts"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_owned_wabas(self, api_version, business_account_id) -> dict[str, Any]:
        """
        Retrieves a list of WhatsApp Business Accounts owned by or shared with the specified business account using a GET request to the given endpoint.

        Args:
            api_version (string): api-version
            business_account_id (string): business-account-id

        Returns:
            dict[str, Any]: Example response

        Tags:
            WhatsApp Business Accounts (WABA)
        """
        if api_version is None:
            raise ValueError("Missing required parameter 'api-version'")
        if business_account_id is None:
            raise ValueError("Missing required parameter 'business-account-id'")
        url = f"{self.base_url}/{api_version}/{business_account_id}/owned_whatsapp_business_accounts"
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
