#!/usr/bin/env python3

# Before begin you need to change Gmail settings:
# 1. Turn off 2-step verification
# 2. Enable: Allow less secure apps

from sender import Mail, Message

mail = Mail(
    "smtp.gmail.com",
    port = 587,
    username = "sender_address@gmail.com", password = "sender_password", use_tls = True,
    use_ssl = False,
    debug_level = None
)
mail.fromaddr = ("Sender Name", "sender_address@gmail.com")

msg = Message("msg subject")
msg.fromaddr = ("Sender Name", "sender_address@gmail.com")
msg.to = "receiver_address@gmail.com"
msg.body = "this is a msg plain text body"
msg.html = "<b>this is a msg text body</b>"
msg.reply_to = "sender_address@gmail.com"
msg.charset = "utf-8"
msg.extra_headers = {}
msg.mail_options = []
msg.rcpt_options = []

# Send message
mail.send(msg)