from django.core.mail import send_mail
from .models import BaseSettings

try: 
  email_clients = BaseSettings.objects.get().email
except:
  email_clients = "default"

EMAIL_FROM = "info@xn----7sbah6bllcobpj.xn--p1ai"
# email_clients = "saniagolovanev@gmail.com"

def email_callback(messages, title):
  send_mail(
    title,
    messages,
    EMAIL_FROM,
    email_clients.split(','),
    fail_silently=False,
  )
  