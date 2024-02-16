import os
import asyncio
from pprint import pprint
from notion_client import AsyncClient

notion = AsyncClient(auth=os.environ["NOTION_TOKEN"])


async def list_notion_users():
    list_users_response = await notion.users.list()
    pprint(list_users_response)


if __name__ == "__main__":
    asyncio.run(list_notion_users())
