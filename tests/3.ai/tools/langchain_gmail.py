


from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch
from langchain_community.tools.gmail.utils import (
    build_resource_service,
    get_gmail_credentials,
)

credentials = get_gmail_credentials(
    token_file="token.json", 
    scopes=["https://mail.google.com/"], 
    client_secrets_file="credentials.json"
)

api_resource = build_resource_service(credentials=credentials)

def fetch_mails():
  search = GmailSearch(api_resource=api_resource)
  # deprecated
  # emails = search("in:inbox")
  emails = search.invoke("in:inbox")

  mails = []

  for email in emails: 
      mails.append(
          {
              "subject": email["subject"],
              "snippet": email["snippet"],
          }
      )

  return mails

if __name__ == "__main__":
  print(fetch_mails())