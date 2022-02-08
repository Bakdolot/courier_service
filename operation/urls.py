from django.urls import path

from .views import (CreateParcelView,
                    UpdateParcelView,
                    ListParcelView,
                    PaymentParcelView,
                    PaymentParcelWithBonusView,
                    DirectionsView,
                    DirectionView,
                    ParametersView,
                    DeliveryTypeView,
                    EnvelopeView,
                    RecipientView,
                    ParcelDateView,
                    SenderView,
                    TownsView,
                    AreasView,
                    PackageTypeView,
                    ParcelStatusView,
                    GetDataView,
                    )
urlpatterns = [
    path('towns/', TownsView.as_view()),
    path('areas/', AreasView.as_view()),
    path('direction/', DirectionView.as_view()),
    path('directions/', DirectionsView.as_view()),
    path('parameters/', ParametersView.as_view()),
    path('delivery_type/', DeliveryTypeView.as_view()),
    path('package/', PackageTypeView.as_view()),
    path('envelope/', EnvelopeView.as_view()),
    path('recipient/', RecipientView.as_view()),
    path('delivery_date/', ParcelDateView.as_view()),
    path('sender/<int:pk>', SenderView.as_view()),
    path('create/', CreateParcelView.as_view()),

    path('status/<int:pk>', ParcelStatusView.as_view()),
    path('getparcelinfo/<int:pk>', GetDataView.as_view()),
    path('update/<int:pk>', UpdateParcelView.as_view()),
    path('list/', ListParcelView.as_view()),
    #path('bonus/<int:pk>', PaymentParcelWithBonusView.as_view())
]