import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("ัะตัั")

bot.run("OTc0NzUyOTExNjg5MTU0NjQw.G4tCKx.LgAQOY4gZEuDxMw3u0ldkHm0g4khhMtXr4uinY")
