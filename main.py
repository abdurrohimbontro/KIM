import pyrogram
import telethon
import tgcrypto

print("\nAssslamualaikum selamat datang di online StringSession generator\n")

print("[p]: Pyrogram (docs.pyrogram.org)")
print("PyroGramUserBot ==> https://GitHub.com/SpEcHiDe/PyroGramBot")

print("[t]: Telethon (docs.telethon.dev)")
print("Telethon UserBot ==> https://GitHub.com/SpEcHiDe/UniBorg")

print("\n Masukkan opsi yang anda pilih sesuai kebutuhan anda : ")
s_l = input("\nmasukkan p / t ==> ")

if s_l == "p":
  print("\nanda memiih Pyrogram")
  APP_ID = int(input("\nSilahkan masukkan APP ID anda di sini : "))
  API_HASH = input("Silahkan masukkan API HASH anda di sini : ")
  import pyrogram
  app = pyrogram.Client(
    ":memory:",
    api_id=APP_ID,
    api_hash=API_HASH
  )
  app.start()
  session_str = app.export_session_string()
  s_m = app.send_message("Dikirim oleh 𝓚𝓲𝓶 𝓸𝓯𝓯𝓲𝓬𝓲𝓪𝓵", session_str)
  s_m.reply_text("☕ santuy aja dulu🚬 \n ⚠️perhatian : jangan berikan StringSession kepada orang lain\nJika anda ingin masuk grup random : @crazy_people345 jangan lupa gabung ya...sampai ketemu di grup", quote=True)
  app.stop()
  print("\nSesion string anda telah siap silahkan cek pesan tersimpan di telegram anda by 𝓚𝓲𝓶 𝓸𝓯𝓯𝓲𝓬𝓲𝓪𝓵")

elif s_l == "t":
  print("\nanda memilih Telethon")
  # (c) https://t.me/TelethonChat/37677
  from telethon.sync import TelegramClient
  from telethon.sessions import StringSession
  APP_ID = int(input("\nMasukkan APP ID anda di sini : "))
  API_HASH = input("\nMasukkan API HASH anda di sini : ")
  client = TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
  )
  client.start()
  session_str = client.session.save()
  s_m = client.send_message("di kirim oleh 𝓚𝓲𝓶 𝓸𝓯𝓯𝓲𝓬𝓲𝓪𝓵", session_str)
  s_m.reply("☕ Santuy aja dulu 🚬\n⚠️ perhatian :\njangan berikan Sesiom string ini kepada orang lain\nJika anda ingin Masuk grup random : @crazy_people345 jangan lupa gabung ya...sampai ketemu di grup")
  client.stop()
  print("\nStringSession anda siap di gunakan Silahkan cek pesan tersimpan anda by 𝓚𝓲𝓶 𝓸𝓯𝓯𝓲𝓬𝓲𝓪𝓵")

else:
  print("Silahkan pilih opsi yang anda butuhkan p / t, terima kasih.")
