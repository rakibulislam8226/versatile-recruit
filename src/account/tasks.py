from django.core.mail import EmailMultiAlternatives, EmailMessage


def send_mail_for_active_account(employee, pdf, html_body, subject):
    email = EmailMultiAlternatives()
    email.subject = f'{subject} of {employee.full_name}'
    email.attach_alternative(html_body, 'text/html')
    email.to = [employee.email]
    email.from_email = '"Versatile Recruit" <rakibkhan9065@gmail.com>'
    email.attach_file(pdf)
    email.send()