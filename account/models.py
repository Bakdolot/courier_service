from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django_2gis_maps import fields as map_fields
from django_2gis_maps.mixins import DoubleGisMixin

from account.validators import PhoneValidator, RegionCodeValidator
from account.managers import UserManager
from account.choices import PaymentHistoryType, UserRole


class User(AbstractUser):
    phone_validator = PhoneValidator

    phone = models.CharField(
        _('user phone number'), 
        max_length=15, 
        unique=True,
        help_text=_('Required. 9 digits in format: 996*********** without "+".'),
        validators=[phone_validator],
        error_messages={
            'unique': _("A user with that phone number already exists."),
        },
        )
    info = models.CharField(_('user info'), max_length=255)
    region = models.ForeignKey('Region', on_delete=models.DO_NOTHING, verbose_name=_('region'), null=True)
    district = models.ForeignKey('District', on_delete=models.DO_NOTHING,  verbose_name=_('district'), null=True)
    role = models.PositiveSmallIntegerField(_('role'), choices=UserRole.choices, default=UserRole.CLIENT)
    points = models.PositiveIntegerField(_('user bonus points'), default=0)
    avatar = models.ImageField(_('avatar'), upload_to='user/', blank=True)
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    
    def __str__(self) -> str:
        return self.phone


    username = None
    email = None

    objects = UserManager()

    EMAIL_FIELD = None
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone'

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

        

class Region(DoubleGisMixin, models.Model):
    name = map_fields.AddressField(_('name'), max_length=100)
    geolocation = map_fields.GeoLocationField(_('geolocation'), blank=True)
    code = models.CharField(_('code'), max_length=4, validators=[RegionCodeValidator])
    
    def __str__(self):
        return self.name


class District(DoubleGisMixin, models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_('region'))
    name = map_fields.AddressField(_('name'), max_length=100)
    geolocation = map_fields.GeoLocationField(_('geolocation'), blank=True)
    code = models.CharField(_('code'), max_length=4, validators=[RegionCodeValidator])

    def __str__(self):
        return self.name


class Village(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_('region'), null=True)
    name = map_fields.AddressField(_('name'), max_length=100)
    geolocation = map_fields.GeoLocationField(_('geolocation'), blank=True)
    code = models.CharField(_('code'), max_length=4, validators=[RegionCodeValidator])

    def __str__(self):
        return self.name


class DiscountHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    sum = models.PositiveIntegerField(_('sum'))
    # parcel = models.ForeignKey('Parcel', on_delete=models.DO_NOTHING, verbose_name=_('parcel'))
    
    def __str__(self) -> str:
        return f'{self.user} -> {self.sum}'


class PaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('user'))
    # payment = models.ForeignKey('Payment', on_delete=models.DO_NOTHING, verbose_name=_('payment'))
    sum = models.PositiveIntegerField(_('sum'))
    payment_type = models.PositiveSmallIntegerField(_('payment type'), choices=PaymentHistoryType.choices)
    
    def __str__(self) -> str:
        return f'{self.user} -> {self.sum}'
