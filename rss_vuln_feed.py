#RSS VULN FEED

# Import feedparser, time, asyncio and telegram modules
import feedparser
import time
import asyncio
import telegram

# A list of RSS feed URLs
feed_urls = ["https://sec.jetlib.com/?media=rss", "https://filestore.fortinet.com/fortiguard/rss/threatsignal.xml"]

# Telegram Bot token and chat ID
bot = telegram.Bot(token="YourToken")
chat_id = 'YourChatid'

# A set to store the titles of the entries that have been printed
printed_titles = set()


# A function to print new entries in the feeds
async def print_new_entries(feed_urls):
    # Loop through the feed URLs in the list
    for feed_url in feed_urls:
        # Parse the feed using feedparser
        feed = feedparser.parse(feed_url)

        # Loop through the entries in the feed
        for entry in feed.entries:
            # Check if the title of the entry is not in the printed_titles set
            if entry.title not in printed_titles:
                # Print the title of the entry
                print(entry.title)
                # Add the title of the entry to the printed_titles set
                printed_titles.add(entry.title)
                # Send a Telegram message with the new entry title and guid
                await send_telegram_message(entry)


# A function to send Telegram messages with the new entry title and guid
async def send_telegram_message(entry):
    # Format the message with HTML tags
    message = f"*{entry.title}*\n[Click here to read]({entry.guid})"
    # Send the message using bot.send_message() with parse_mode='HTML'
    await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')


# A while loop to run the code always
while True:
    try:
        # Call the print_new_entries function with the feed_urls list
        asyncio.run(print_new_entries(feed_urls))
    except Exception as e:
        print(f"Error: {e}")
    # Wait for 10 seconds before checking the feeds again
    time.sleep(10)
