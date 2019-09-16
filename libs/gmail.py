import email
import imaplib

from common.config import config


class GmailService:
    mail_client = imaplib.IMAP4_SSL(config.GMAIL_SMTP_SERVER)

    def __init__(self, username, password):
        try:
            self.mail_client.login(username, password)
        except:
            pass

    @staticmethod
    def _get_decoded_email_body(msg):
        text = ""
        if msg.is_multipart():
            html = None
            for part in msg.get_payload():
                if part.get_content_charset() is None:
                    # We cannot know the character set, so return decoded "something"
                    text = part.get_payload(decode=True)
                    continue

                charset = part.get_content_charset()

                if part.get_content_type() == "text/plain":
                    text = str(
                        part.get_payload(decode=True), str(charset), "ignore"
                    ).encode("utf8", "replace")

                if part.get_content_type() == "text/html":
                    html = str(
                        part.get_payload(decode=True), str(charset), "ignore"
                    ).encode("utf8", "replace")

            if text is not None:
                return text.strip()
            else:
                return html.strip()
        else:
            text = str(
                msg.get_payload(decode=True), msg.get_content_charset(), "ignore"
            ).encode("utf8", "replace")
            return text.strip()

    def get_latest_unread_emails(self, sender=None, subject=None):
        self.mail_client.select("inbox")

        query_string = "UNSEEN"

        if sender:
            query_string = query_string + ' FROM "%s"' % sender

        if subject:
            query_string = query_string + ' SUBJECT "%s"' % subject

        query_string = "(" + query_string + ")"

        if sender:
            _, data = self.mail_client.search(None, query_string)
        else:
            _, data = self.mail_client.search(None, query_string)

        mails = []

        for email_id in data[0].split():
            _, data = self.mail_client.fetch(email_id, "(RFC822)")
            raw_content = data[0][1].decode("utf-8")
            msg = email.message_from_string(raw_content)

            mail = {
                "content": self._get_decoded_email_body(msg).decode("utf-8"),
                "subject": msg["subject"],
                "from": msg["from"],
                "to": msg["to"].replace("<", "").replace(">", ""),
                "id": email_id,
            }

            mails.append(mail)

        return mails
