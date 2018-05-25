from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(FacebookInfo)
admin.site.register(TwitterInfo)
admin.site.register(GoogleInfo)
#admin.site.register(CardsAdd)
admin.site.register(Cards)
admin.site.register(PayPal)
admin.site.register(TicketsStore)
admin.site.register(Tickets)
admin.site.register(RegFinance)
admin.site.register(FinanceTransac)
admin.site.register(DailyActivities)
admin.site.register(BusFare)




