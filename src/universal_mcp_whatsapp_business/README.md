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


## Tool List

| Tool | Description |
|------|-------------|
| get_analytics | Retrieve WhatsApp Business Account analytics data via the WABA Analytics API endpoints. |
| get_credit_lines | Retrieve credit line information from the Facebook Marketing API Business > Extendedcredits endpoint. |
| get_business_account_specific_fields | Retrieve business account data with specified fields from the Facebook Marketing API. |
| get_commerce_settings | Retrieve the commerce settings configured for the WhatsApp Business account. |
| set_or_update_commerce_settings | Set or update WhatsApp commerce settings. |
| upload_media_step1_of2_create_session | Initiates a resumable media upload session by creating an upload session ID and preparing the endpoint. |
| upload_media_step2_of2_initiate_upload | Initiates a media upload to a server using a resumable upload API. |
| get_business_phone_number | Retrieves the business phone number for the associated WhatsApp Business Account. |
| get_all_business_phone_numbers | Retrieves all business phone numbers, optionally filtering by specified fields or criteria. |
| get_qr_code | Retrieves QR code information from the WhatsApp Business API for the associated business account. |
| delete_qr_code | Deletes a QR code from the WhatsApp Business API. |
| get_all_qr_codes_default_fields | Retrieves QR codes with default fields from the WhatsApp Business API. |
| create_qr_code | Creates a QR code based on the provided code and prefilled message. |
| get_template_by_id_default_fields | Retrieves a WhatsApp message template by ID, including default fields. |
| edit_template | Edits a template by sending a POST request with the specified parameters. |
| get_template_by_name_default_fields | Retrieves a WhatsApp message template by name using default fields from the WhatsApp Business Account API. |
| create_authentication_template_wotp_copy_code_button | Creates an authentication message template with an OTP copy code button for WhatsApp Business API. |
| delete_template_by_name | Deletes a message template by name from a WhatsApp Business API account. |
| get_all_apps_subscribed_to_waba_swebhooks | Retrieve all apps subscribed to WABA's webhooks. |
| subscribe_app_to_waba_swebhooks | Subscribe an application to WhatsApp Business Account (WABA) webhooks. |
| unsubscribe_app_from_waba_swebhooks | Unsubscribes the app from WhatsApp Business Account (WABA) webhooks, removing all existing subscriptions. |
| get_all_shared_wabas | Retrieve all shared WhatsApp Business Accounts (WABAs) associated with the authenticated business. |
| get_all_owned_wabas | Retrieves all owned WhatsApp Business Accounts (WABAs) through an API request. |

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