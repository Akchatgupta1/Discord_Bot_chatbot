# Imports
import discord
from discord import app_commands
from discord.ext import commands
import google.generativeai as genai

# Configuration
discord_api_key="your discord api key"
gemini_api_key = "your api key"

genai. configure(api_key=gemini_api_key)
model = genai. GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])

intents = discord. Intents.default( )
intents. messages = True
intents.message_content = True

bot = commands. Bot(command_prefix="!", intents=intents)

# Bot Events
@bot.event
async def on_ready( ):
  await bot.tree.sync()
  print("Bot is ready" )

@bot.tree. command(name= "jexi", description="Talk to Jexi" )
async def jexi(interaction: discord. Interaction, message: str):
  await interaction.response.defer()
  response = chat. send_message(message)
  await interaction. followup.send(response.text)

bot.run(discord_api_key)