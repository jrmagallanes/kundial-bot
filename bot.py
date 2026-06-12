import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} conectado")

@bot.command()
async def kundial(ctx):
    await ctx.send("🏆 KU'NDIAL 2026 BOT ACTIVO")

bot.run(TOKEN)
