from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class ShopManager(BaseUserManager):
    def create_user(self, ph_number, id, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not ph_number:
            raise ValueError('Users must have an email address')

        user = self.model(
            ph_number=ph_number,
            id = id
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, ph_number, id, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            ph_number,
            id=id,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, ph_number, id, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            ph_number,
            id = id,
            password=password,

        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Shop(AbstractBaseUser):
    shop_name           = models.CharField(max_length=60)
    owner_name          = models.CharField(max_length=120)
    ph_number           = models.CharField(max_length=10, null=False, unique=True, verbose_name="Phone Number")
    id                  = models.CharField(max_length=15, primary_key=True, unique=True)
    active              = models.BooleanField(default=True)
    staff               = models.BooleanField(default=False)  # a admin user; non super-user
    admin               = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'ph_number'
    REQUIRED_FIELDS = ['id']

    def get_full_name(self):
        # The user is identified by their email address
        return self.shop_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.shop_name

    def __str__(self):              # __unicode__ on Python 2
        return self.shop_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects = ShopManager()