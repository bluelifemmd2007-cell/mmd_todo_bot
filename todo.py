import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


OWNER_ID = 626780353  

def is_owner(user_id):
    return user_id == OWNER_ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات فعال شد و همه می‌تونن ازش استفاده کنن.")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("آیتم اضافه شد.")

async def list_items(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("لیست آیتم‌ها:")


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id

    if not is_owner(uid):
        await update.message.reply_text("⛔ فقط صاحب ربات اجازه این کار را دارد.")
        return

    await update.message.reply_text("✔️ شما صاحب ربات هستید و دسترسی کامل دارید.")



def main():
    TOKEN = os.getenv("BOT_TOKEN")

    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is not set.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("list", list_items))
    app.add_handler(CommandHandler("admin", admin))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()


  
