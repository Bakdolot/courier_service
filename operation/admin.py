from django.contrib import admin
from .models import (
    Parcel,
    UserInfo,
    PaymentType,
    DestinationType,
    ParcelOption,
    ParcelInfo,
    Town,
    Area,
    ParcelStatus,
    DeliveryType,
    Envelope,
    Directions,
    Direction,
    )

from account.models import User

admin.site.register(Parcel),
admin.site.register(Area),
admin.site.register(Town),
admin.site.register(UserInfo),
admin.site.register(PaymentType),
admin.site.register(DestinationType),
admin.site.register(ParcelOption),
admin.site.register(ParcelInfo),
admin.site.register(ParcelStatus),
admin.site.register(DeliveryType),
admin.site.register(Envelope),
admin.site.register(User),
admin.site.register(Directions),
admin.site.register(Direction),
