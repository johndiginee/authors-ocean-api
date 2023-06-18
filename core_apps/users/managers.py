from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Creating custom user model."""

    def email_validator(self, email):
        """Validating user email."""
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_("You must provide a vaild email address."))

    def create_user(self, first_name, last_name, email, password, **extrafields):
        """Creating normal user."""
        if not first_name:
            raise ValueError(_("Users must have a first name."))
        if not last_name:
            raise ValueError(_("Users must have a last name."))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Users must have an email address."))

        user = self.model(
            first_name=first_name, last_name=last_name, email=email, **extrafields
        )
        user.set_password(password)

        extrafields.setdefault("is_staff", False)
        extrafields.setdefault("is_superuser", False)

        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password, **extrafields):
        """Creating superuser."""
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_superuser", True)
        extrafields.setdefault("is_active", True)

        if extrafields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extrafields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        if not password:
            raise ValueError(_("Superuser must have a password."))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Superuser must have an email address."))

        user = self.create_user(first_name, last_name, email, password, **extrafields)
        user.save(using=self._db)
        return user
