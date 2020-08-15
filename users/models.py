import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string




class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, _("male")),
        (GENDER_FEMALE, _("female")),
        (GENDER_OTHER, _("other")),
    )

    LANGAUGE_ENGLISH = "en"
    LANGAUGE_KOREAN = "kr"

    LANGAUGE_CHOICES = (
        (LANGAUGE_ENGLISH, "en"),
        (LANGAUGE_KOREAN, "kr"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_KRW, "krw"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao"),
    )
    first_name = models.CharField(
        _("first name"), max_length=30, blank=True,
    )
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        _("gender"), choices=GENDER_CHOICES, max_length=10, blank=True
    )
    bio = models.TextField(_("bio"), default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGAUGE_CHOICES, max_length=2, blank=True, default=LANGAUGE_KOREAN
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW
    )
    host = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    email_verified = models.BooleanField(default=False)
    eamil_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                _("Verify Airbnb Account"),
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return