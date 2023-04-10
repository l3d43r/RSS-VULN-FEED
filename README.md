#  RSS VULN FEED

Python script that parses RSS vuln feeds and sends Telegram messages with new entries.



## Installation

Provide step by step instructions on how to install the project locally.


1) install screen on ur linux distro 
----- Terminal : 
        sudo apt update 
        
        sudo apt install screen
        
        ----- python  Dependencies :

        1) pip install python-telegram-bot
        
        2) pip install feedparser

2) Telegrab bot 
* Go to this url : https://telegram.me/botfather
* Open botfather on ur telegram 
* Send /newbot to create a new Telegram bot.
* When asked, enter a name for the bot.
* Give the Telegram bot a unique username. Note that the bot name must end with the word "bot" (case-insensitive).
* Copy and save the Telegram bot's access token for later steps.

3) How to find Chatid :

* Change the token with the letter X 
---> https://api.telegram.org/botXXXXXXXX:XXXXXXXXXXXXXXXXXXX/getUpdates
* Search for Chat ID: (is numeric)

4) Replace on the code :
bot = telegram.Bot(token="YOUR TOKEN")
chat_id = 'YOUR CHAT ID '




## To Do 

: /search function 

: /set vuln cms only updater
