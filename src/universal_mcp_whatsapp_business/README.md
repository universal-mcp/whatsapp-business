# Universal Mcp Whatsapp Business MCP Server

An MCP Server for the Universal Mcp Whatsapp Business API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

## 🛠️ Setup Instructions

Follow these steps to get the development environment up and running:

### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.

### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```

### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal mcp whatsapp business/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Whatsapp Business API.


| Tool | Description |
|------|-------------|
| `get_analytics` | Get analytics. - Guide: [Analytics](https://developers.facebook.com/docs/whatsapp/business-management-api/analytics) |
| `get_credit_lines` | Get credit lines. - Endpoint reference: [Business > Extendedcredits](https://developers.facebook.com/docs/marketing-api/reference/extended-credit/) |
| `get_business_account_specific_fields` | Get business account (specific fields). Endpoint reference: [Business](https://developers.facebook.com/docs/marketing-api/reference/business/) |
| `get_commerce_settings` | Get commerce settings. - Guide: [Sell Products & Services](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/sell-products-and-services) (Cloud API) |
| `set_or_update_commerce_settings` | Set or update commerce settings. - Guide: [Sell Products & Services](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/sell-products-and-services) (Cloud API) |
| `upload_media_step1_of2_create_session` | Upload media (Step 1 of 2): Create session. - Guide: [Resumable Upload API](https://developers.facebook.com/docs/graph-api/guides/upload) |
| `upload_media_step2_of2_initiate_upload` | Upload media (Step 2 of 2): Initiate upload. - Guide: [Resumable Upload API](https://developers.facebook.com/docs/graph-api/guides/upload) |
| `get_business_phone_number` | Get business phone number. - Guide: [Retrieve Phone Numbers](https://developers.facebook.com/docs/whatsapp/business-management-api/manage-phone-numbers) |
| `get_all_business_phone_numbers` | Get all business phone numbers. - Guide: [Phone Numbers](https://developers.facebook.com/docs/whatsapp/phone-numbers) |
| `get_qr_code` | Get QR code. - Guide: [QR Codes](https://developers.facebook.com/docs/whatsapp/business-management-api/qr-codes) |
| `delete_qr_code` | Delete QR code. - Guide: [QR Codes](https://developers.facebook.com/docs/whatsapp/business-management-api/qr-codes) |
| `get_all_qr_codes_default_fields` | Get all QR codes (default fields). - Guide: [QR Codes](https://developers.facebook.com/docs/whatsapp/business-management-api/qr-codes) |
| `create_qr_code` | Create QR code. - Guide: [QR Codes](https://developers.facebook.com/docs/whatsapp/business-management-api/qr-codes) |
| `get_template_by_id_default_fields` | Get template by ID (default fields). - Guide: [Message Templates](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates) |
| `edit_template` | Edit template. - Guide: [Message Templates](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates) |
| `get_template_by_name_default_fields` | Get template by name (default fields). - Guide: [Message Templates](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates) |
| `create_authentication_template_wotp_copy_code_button` | Create authentication template w/ OTP copy code button. - Guide: [Authentication Templates with OTP Buttons](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates) |
| `delete_template_by_name` | Delete template by name. - Guide: [Message Templates](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates) |
| `get_all_apps_subscribed_to_waba_swebhooks` | Get all apps subscribed to WABA's webhooks. - Guide: [Webhooks](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/set-up-webhooks) |
| `subscribe_app_to_waba_swebhooks` | Subscribe app to WABA's webhooks. - Guide: [Webhooks](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/set-up-webhooks) |
| `unsubscribe_app_from_waba_swebhooks` | Unsubscribe app from WABA's webhooks. - Guide: [Webhooks](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/set-up-webhooks) |
| `get_all_shared_wabas` | Get all shared WABAs. Endpoint reference: [Business > Extended Credits](https://developers.facebook.com/docs/marketing-api/reference/business/extendedcredits/) |
| `get_all_owned_wabas` | Get all owned WABAs. Endpoint reference: [Business > Extended Credits](https://developers.facebook.com/docs/marketing-api/reference/business/extendedcredits/) |


## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal mcp whatsapp business/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the Universal Mcp Whatsapp Business app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server 