import os
from pprint import pprint
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

list_users_response = notion.users.list()
pprint(list_users_response)
