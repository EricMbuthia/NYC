"""NYC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from passenger import views
app_name="passenger"
urlpatterns = [
path('newcustomer/<slug:token>/<slug:description>/',views.create_customer,name="create_customer"),
path('buyTickets/',views.buyTickets,name="buyTickets"),
path('buySingleTicket/',views.buySingleTickets,name="buySingleTickets"),
path('buyMultipleTickets/',views.buyMultipleTickets,name="buyMultipleTickets"),
path('paymentMethod/', views.CardList.as_view(),name="paymentMethod"),
path('paymentMethodManage/', views.CardListForManager.as_view(),name="paymentMethodManage"),
path('paymentMethodDetailManage/<int:pk>/',views.CardDetailForManagement.as_view(), name="paymentMethodDetailManage"),
path('paymentMethodDetail/<int:pk>/',views.CardDetail.as_view(), name="paymentMethodDetail"),
path('useCard/<slug:card_email_id>/<slug:payment_method>',views.createCharge,name="useCard"),
path('paymentMethod23/',views.paymentMethod23,name="paymentMethod23"),
path('viewTickets/',views.viewTickets,name="viewTickets"),
path('ticketList/', views.TicketList.as_view(),name="ticketList"),
path('ticketDetail/<int:pk>/',views.TicketDetail.as_view(), name="ticketDetail"),
path('useTicket/<int:id>',views.useTicket,name="useTicket"),
path('payTicket/',views.payTicket,name="payTicket"),
path('addCard/',views.addCard,name='addCard'),
path('addPaypal/',views.addPaypal, name="addPaypal"),
path('home/',views.home, name="home"),

]
