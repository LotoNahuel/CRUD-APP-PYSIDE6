import os.path
import base64
from email.message import EmailMessage

# import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def get_gmail_service():

  creds = None

  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file( "token.json", SCOPES )

  if not creds or not creds.valid:

    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file( "api/credentials.json", SCOPES )

      creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
      token.write(creds.to_json())

  return build( "gmail", "v1", credentials=creds )

def gmail_create_draft(text, userEmail):

  try:
    # create gmail api client
    # service = build("gmail", "v1", credentials=creds)
    service = get_gmail_service()

    message = EmailMessage()

    message.set_content(f"THIS TOKEN EXPIRED IN 5 MINUTES: {text}\nDON'T SHARE THIS TOKEN WITH ANYONE")

    message["To"] = userEmail
    message["From"] = "banquito947@gmail.com"
    message["Subject"] = "TOKEN REGISTER"

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )

    print(f'Message: {send_message["id"]}')

    return True, send_message

  except HttpError as error:
    print(f"An error occurred: {error}")
  return False, None


if __name__ == "__main__":
  get_gmail_service()
  gmail_create_draft()