import discord
from discord.ext import commands
from datetime import timedelta, datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ====== ตั้งค่าเองตรงนี้ ======
WELCOME_CHANNEL_ID = 1452689383684575337
LEAVE_CHANNEL_ID = 1452870570948428079
ROLE_ID = 1443735823412625529
RULE_CHANNEL_ID = 1436593142425194496
WELCOME_IMAGE = "https://cdn.polyspeak.ai/speakmaster/153a9f03e07d5d2e481ed00291d7a5a0.webp"
LEAVE_IMAGE = "https://cdn.polyspeak.ai/speakmaster/153a9f03e07d5d2e481ed00291d7a5a0.webp"
# ==============================

@bot.event
async def on_ready():
     print(f"Bot online as {bot.user}")

# ================== คนเข้าเซิร์ฟ ==================
@bot.event
async def on_member_join(member):
     guild = member.guild
     channel = guild.get_channel(WELCOME_CHANNEL_ID)

     member_count = guild.member_count

     join_time = member.joined_at + timedelta(hours=7)
     join_text = join_time.strftime("%d/%m/%Y เวลา %H:%M")

     embed = discord.Embed(
          title=f"Welcome To {guild.name}",
          description=(
               f"╔══°❀•°✮°•❀°══╗\n"
               f"{member.mention} เข้ามาแล้วอย่าลืมรับยศกันน้ายน้าาา\n"
               f"สมาชิกคนที่ **{member_count}**\n"
               f"รับยศที่ <#{ROLE_ID}>\n"
               f"อ่านกฎที่ <#{RULE_CHANNEL_ID}>\n"
               f"╚══°❀•°✮°•❀°══╝"
          ),
          color=0x0D2F9FE
     )

     embed.set_image(url=WELCOME_IMAGE)
     embed.set_thumbnail(url=member.avatar.url)
     embed.set_footer(text=f"เข้าร่วมเซิร์ฟเมื่อ: {join_text}")

     await channel.send(embed=embed)

# ================== คนออกจากเซิร์ฟ ==================
@bot.event
async def on_member_remove(member):
     guild = member.guild
     channel = guild.get_channel(LEAVE_CHANNEL_ID)

     member_count = guild.member_count
     leave_time = datetime.utcnow() + timedelta(hours=7)
     leave_text = leave_time.strftime("%d/%m/%Y เวลา %H:%M")

     embed = discord.Embed(
          title=f"Leave To {guild.name}",
          description=(
               f"╔══°❀•°✮°•❀°══╗\n"
               f"**{member.name}** ได้ออกจากเซิร์ฟเวอร์แล้ว\n"
               f"สมาชิกคงเหลือ **{member_count}** คน\n"
               f"╚══°❀•°✮°•❀°══╝"
          ),
          color=0x0D2F9FE
     )

     embed.set_image(url=LEAVE_IMAGE)
     embed.set_thumbnail(url=member.avatar.url)
     embed.set_footer(text=f"ออกจากเซิร์ฟเมื่อ: {leave_text}")

     await channel.send(embed=embed)

import os
bot.run(os.getenv("DISCORD_TOKEN"))
