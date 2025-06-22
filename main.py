from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "8080534314:AAHfpvpUZN4ALE8mX7_9VgaVZGC972uNLyg"

keyboard = [
    ["👥 রেফার", "💰 ডিপোজিট", "📤 উইথড্র"],
    ["💎 ভিআইপি", "👤 একাউন্ট", "✅ টাস্ক"],
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "স্বাগতম! নিচের বাটনগুলো থেকে বেছে নিন:", reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👥 রেফার":
        reply = "আপনার রেফার লিংক: https://t.me/your_bot?start=12345"
    elif text == "💰 ডিপোজিট":
        reply = "ডিপোজিট করতে বিকাশ নাম্বার: 01XXXXXXXXX"
    elif text == "📤 উইথড্র":
        reply = "উইথড্র করার জন্য মিনিমাম ৫০ টাকা দরকার।"
    elif text == "💎 ভিআইপি":
        reply = "ভিআইপি মেম্বার হলে আপনি বেশি ইনকাম করতে পারবেন।"
    elif text == "👤 একাউন্ট":
        reply = "নাম: জন, ব্যালেন্স: ২০ টাকা"
    elif text == "✅ টাস্ক":
        reply = "আজকের টাস্ক: একটি চ্যানেল জয়েন করুন।"
    else:
        reply = "দুঃখিত, আমি বুঝতে পারিনি। নিচের বাটন থেকে বেছে নিন।"

    await update.message.reply_text(reply, reply_markup=reply_markup)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot started...")
    app.run_polling()