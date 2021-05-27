from django.contrib import admin

# Register your models here.

from .models import USER,StockData,SALE,Purchase,AddPayable,AddRecivable,UserBalance


@admin.register(USER)
class ADMINUSER(admin.ModelAdmin):
    list_display = ['username']

@admin.register(StockData)
class ADMINStock(admin.ModelAdmin):
    list_display = ['StockName','TotalStockQuantity','StockPrice']


@admin.register(SALE)
class ADMINAddSALE(admin.ModelAdmin):
    list_display = ['userID','stockID','StockQuantitySale','StockPrice','TotalRecivable','DateData']


@admin.register(Purchase)
class ADMINAddPurchase(admin.ModelAdmin):
    list_display = ['userID','stockID','StockQuantityPurchase','StockPrice','Totalpayable','DateData']

@admin.register(AddPayable)
class ADMINAddPayable(admin.ModelAdmin):
    list_display = ['userID','DateData','PayableAmount']


@admin.register(AddRecivable)
class ADMINAddRecivable(admin.ModelAdmin):
    list_display = ['userID','DateData','RecivableAmount']

@admin.register(UserBalance)
class ADMINUserBalance(admin.ModelAdmin):
    list_display = ['userID','DateData','TotalBalance']