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

def gmail_create_draft(text, userEmail):
  """Create and insert a draft email.
   Print the returned draft's message and id.
   Returns: Draft object, including draft id and message meta data.

  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """

  creds, _ = ""

  if os.path.exists("credentials.json"):
    with open("credentials.json" , "r") as r:
      creds, _ = r


  try:
    # create gmail api client
    service = build("gmail", "v1", credentials=creds)

    message = EmailMessage()

    # message.set_content("This is automated draft mail")
    message.set_content(f"THIS TOKEN EXPIRED IN 5 MINUTES: {text}\nDON'T SHARE THIS TOKEN WITH ANYONE")

    message["To"] = userEmail
    message["From"] = "banquito947@gmail.com"
    message["Subject"] = "TOKEN REGISTER"

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"message": {"raw": encoded_message}}
    # pylint: disable=E1101
    draft = (
        service.users()
        # .drafts()
        .messages
        # .create(userId="me", body=create_message)
        .semd(userId="me", body=create_message)
        .execute()
    )

    print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

  except HttpError as error:
    print(f"An error occurred: {error}")
    draft = None

  return draft


if __name__ == "__main__":
  gmail_create_draft()