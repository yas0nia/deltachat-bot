#!/usr/bin/env python3
"""
Example echo bot without using hooks
"""
import asyncio
import logging
import sys

from deltachat_rpc_client import DeltaChat, EventType, Rpc, SpecialContactId
from llm_handler import fetch_llm_reply


async def main():
    async with Rpc() as rpc:
        deltachat = DeltaChat(rpc)
        system_info = await deltachat.get_system_info()
        logging.info("Running deltachat core %s", system_info["deltachat_core_version"])

        accounts = await deltachat.get_all_accounts()
        account = accounts[0] if accounts else await deltachat.add_account()

        await account.set_config("bot", "1")
        if not await account.is_configured():
            logging.info("Account is not configured, configuring")
            await account.set_config("addr", sys.argv[1])
            await account.set_config("mail_pw", sys.argv[2])
            await account.configure()
            logging.info("Configured")
        else:
            logging.info("Account is already configured")
            await deltachat.start_io()

        async def process_messages():
            for message in await account.get_next_messages():
                snapshot = await message.get_snapshot()
                await snapshot.message.mark_seen()
                if (
                    snapshot.from_id != SpecialContactId.SELF
                    and not snapshot.is_bot
                    and not snapshot.is_info
                ):
                    print("incomming msg", snapshot.text)
                    reply = await fetch_llm_reply(snapshot.text)

                    await snapshot.chat.send_text(reply)

        # Process old messages.
        await process_messages()

        while True:
            event = await account.wait_for_event()
            if event["type"] == EventType.INFO:
                logging.info("%s", event["msg"])
            elif event["type"] == EventType.WARNING:
                logging.warning("%s", event["msg"])
            elif event["type"] == EventType.ERROR:
                logging.error("%s", event["msg"])
            elif event["type"] == EventType.INCOMING_MSG:
                logging.info("Got an incoming message")
                await process_messages()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
