from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailService:
    @staticmethod
    def send_welcome_email(user_email, username, token):
        subject = "Bienvenido a nuestra plataforma"
        html_content = render_to_string(
            "users/presentation/templates/welcome_email.html",
            {"username": username, "token": token}
        )

        email = EmailMultiAlternatives(
            subject, "",
            "noreply@tuempresa.com",
            [user_email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
