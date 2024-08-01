from imap_tools import MailBox, AND
from app.config.gmail_config import gmailSettings
from bs4 import BeautifulSoup
import re

def fetch_mail():
    with MailBox("imap.gmail.com").login(gmailSettings.G_USER, gmailSettings.G_PWD, "Inbox") as mb:
        for msg in mb.fetch(reverse=True, mark_seen=True):
            if msg.subject.startswith('Fwd'):
                _from = re.search(r'From:\s*(.+)', msg.text).group(1)
                if 'noreply@phonepe.com' in _from:
                    txn_id = re.search(r'Txn\. ID\s*:\s*(\S+)', msg.text).group(1)
                    paid_to = re.search(r'Paid to\s*(.+?)\s*₹', msg.text).group(1)
                    txn_status = re.search(r'Txn\. status\s*:\s*(\S+)', msg.text).group(1)
                    debited_from = re.search(r'Debited from\s*:\s*(.+)', msg.text).group(1)
                    bank_ref_no = re.search(r'Bank Ref\. No\.\s*:\s*(\S+)', msg.text).group(1)
                    message_match = re.search(r'Message\s*:\s*(.*?)(?:\s*Hi|\s*$)', msg.text, re.DOTALL)
                    message = message_match.group(1).strip() if message_match else ""
                    date = re.search(r'Date:\s*(.+?)\sat', msg.text).group(1)
                    amount = re.search(r'Sent ₹\s*(\d+)', msg.text).group(1)

                elif('alerts@hdfcbank.net' in _from):
                    print(_from)
                
                
                