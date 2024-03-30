from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError, send_mail
from django.utils.html import strip_tags


def email_send(order):
  subject = "Заказ №" + str(order.id)
  html_content = render_to_string("mail/order_mail.html", {"order": order})
  from_email = "info@xn----7sbah6bllcobpj.xn--p1ai"
  text_content = 'Не поддерживает HTML в письме'
  to = ['saniagolovanev@gmail.com']
  msg = EmailMultiAlternatives(subject, text_content, from_email, to)
  msg.attach_alternative(html_content, "text/html")
  print("Вышел")
  try:
    msg.send()
  except Exception as e:
    print(f"Произошла ошибка при отправке письма: {e}")
    
# def email_callback(title, message):

#     send_mail(
#         title,
#         message,
#         EMAIL_FROM,
#         email_clients.split(','),
#         fail_silently=False,
#     )
    
