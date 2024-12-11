import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler


BOT_TOKEN = "7755314548:AAEbn3EhrlLWxxw5swAJhDfo8FQzeBN9lr8"


PAYTM_VERIFY_API = ""

DEFAULT_AMOUNT = 249


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("💳 𝙋𝘼𝙔 ₹249 𝙑𝙄𝘼 𝙋𝘼𝙔𝙏𝙀𝙈🇮🇳", url="https://paytm.com/8604328478@ptyes")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"👋 Hi {user.first_name}!\n\n"
        "To gain access, you need to pay *₹249* via Paytm.\n\n"
        "✅ Please use the link below to make the payment.\n𝙊𝙐𝙍 𝙎𝙀𝙍𝙑𝙄𝘾𝙀 𝙄𝙎 100 % 𝙏𝙍𝙐𝙎𝙏𝙀𝘿"
        "🔄 Once done, send me the *Transaction ID* for verification.\n\n𝙈𝘼𝘿𝙀 𝘽𝙔 𝙋𝙍𝘼𝙆𝙃𝘼𝙍 𝙑𝘼𝙍𝘿𝙃𝘼𝙉 ©️"
        "💡 Click the button below to pay:𝙏𝙝𝙖𝙣𝙠𝙨 𝙛𝙤𝙧 𝙪𝙨𝙞𝙣𝙜 𝙊𝙪𝙧 𝙎𝙚𝙧𝙫𝙞𝙘𝙚 🇮🇳",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


async def handle_transaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    transaction_id = update.message.text.strip()
    user_id = update.effective_user.id

    # Inform user that verification is in progress
    await update.message.reply_text(f"🔄 𝙑𝙀𝙍𝙄𝙁𝙄𝙔𝙄𝙉𝙂 Transaction ID: `{transaction_id}`...\n𝙋𝙇𝙀𝘼𝙎𝙀 𝙒𝘼𝙄𝙏 𝘼 𝙈𝙊𝙈𝙀𝙉𝙏.", parse_mode="Markdown")

    response = requests.post(PAYTM_VERIFY_API, json={"transaction_id": transaction_id, "user_id": user_id})


    if response.status_code == 200:
        data = response.json()
        status = data.get("status")
        amount = data.get("amount")

        if status == "success" and amount == DEFAULT_AMOUNT:
            await update.message.reply_text("✅ 𝙋𝘼𝙔𝙈𝙀𝙉𝙏 𝙎𝙐𝘾𝘾𝙀𝙎𝙁𝙐𝙇 \n🎉𝙔𝙊𝙐 𝘼𝙍𝙀 𝙉𝙊𝙒 𝘼𝘾𝘾𝙀𝙎𝙎 𝙀𝙉𝙅𝙊𝙔 💥𝙏𝙃𝘼𝙉𝙆𝙎 𝙁𝙊𝙍 𝙋𝙐𝙍𝘾𝙃𝘼𝙎𝙀⭐")
            
        elif status == "success" and amount != DEFAULT_AMOUNT:
            await update.message.reply_text(
                f"❌ 𝙋𝘼𝙔𝙈𝙀𝙉𝙏 𝘼𝙈𝙊𝙐𝙉𝙏 𝙈𝙄𝙎𝙈𝘼𝙏𝘾𝙃𝙀𝘿\n𝙔𝙊𝙐 𝙋𝘼𝙄𝘿 ₹{amount}, 𝙍𝙀𝙌𝙐𝙄𝙍𝙀𝘿 𝘼𝙈𝙊𝙐𝙉𝙏 *₹{DEFAULT_AMOUNT}*.\n 𝙄𝙁 𝙔𝙊𝙐 𝙒𝘼𝙉𝙏 𝙍𝙀𝙁𝙐𝙉𝘿 𝘾𝙊𝙉𝙏𝘼𝘾𝙏 - @LORDX88"
                "Please pay the exact amount to get access.",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text("❌ Verification failed.\nPlease double-check the Transaction ID and try again.")
    else:
        await update.message.reply_text("⚠️𝙐𝙉𝘼𝘽𝙇𝙀 𝙏𝙊 𝘾𝙊𝙉𝙉𝙀𝘾𝙏 𝙏𝙊 𝙑𝙀𝙍𝙄𝙁𝙔 𝙎𝙀𝙍𝙑𝙀𝙍 .\n𝙋𝙇𝙀𝘼𝙎𝙀 𝙏𝙍𝙔 𝘼𝙂𝘼𝙄𝙉 𝙇𝘼𝙏𝙀𝙍 𝘾𝙊𝘿𝙀 :404")


async def invalid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚠🚫 𝙀𝙍𝙍𝙊𝙍 𝙋𝙇𝙀𝘼𝙎𝙀 𝙎𝙀𝙉𝘿 𝙑𝘼𝙇𝙄𝘿 𝙋𝘼𝙔𝙈𝙀𝙉𝙏 *Transaction ID* or type /start 𝙏𝙊 𝙍𝙀𝙎𝙏𝘼𝙍𝙏 𝘽𝙊𝙏✅ ", parse_mode="Markdown")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_transaction))
    app.add_handler(MessageHandler(filters.COMMAND, invalid_command))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()