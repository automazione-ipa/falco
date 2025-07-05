import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# account credentials
username = "d.falco@reply.it"
password = "yourpassword" # get from env
imap_server = "outlook.office365.com"

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)