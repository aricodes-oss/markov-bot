import twitch
import os
from typing import Final

from .models import Message

VALID_AUTHORS: Final = os.environ["VALID_AUTHORS"].split(",")
CHATS_TO_JOIN: Final = os.environ["CHATS"].split(",")

TWITCH_USERNAME: Final = os.environ["TWITCH_USERNAME"]
TWITCH_PASSWORD: Final = os.environ["TWITCH_PASSWORD"]


def ingest_message(message: twitch.chat.message.Message) -> None:
    if message.sender.lower() not in VALID_AUTHORS:
        return

    print(f'Saving "{message.text}" from {message.sender}')
    m = Message(sender=message.sender, contents=message.text)
    m.save()


def main() -> None:
    for username in CHATS_TO_JOIN:
        twitch.Chat(
            channel=f"#{username}", nickname=TWITCH_USERNAME, oauth=TWITCH_PASSWORD
        ).subscribe(ingest_message)


if __name__ == "__main__":
    main()
