# OSRS-DISCORD-BOT
A Old School Runescape Bot for Discord

Hello! This is Jay, this bot I'm writting has 2 main purposes.
1) To learn programming and to experiment with what I can do. Bonus for having a laugh while I'm at it
2) to be a useful tool for Old School Runescape Clans.

If this is to be used, then the .env needs to be created. See https://realpython.com/how-to-make-a-discord-bot-python/ in regards to what information is needed.

Please also update the DISCORD_NAME (line 23) within OSRS1. The reason for this is that the program calls the OSRS Wiki API and if there's any issues then they will be able to assist in resolving them.

#01-06-2021####

Functions:
1 - Logs the bot into Discord

2 - Price Checks using the command !value

To Improve current functions:

1 - Split the code in classes - Makes life easier to debug

2 - Enable short-hand references to items, for example. the item Dragon Dagger (p++) is commonly referred to as DDS. Creating a list and enabling users to update this list of shorthands 

To Add functions:

1 - Command for rolling on bosses/minigames for example !Roll Vorkath 100 will roll 100 times on the Vorkath drop table + value of drops

2 - With rolling - perhaps include potiential to display the amount of EXP granted for the rolls

3 - Give a time to achieve if the user provides a average kill time
