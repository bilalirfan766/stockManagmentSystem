from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('adduser/',views.adduser,name="adduser"),
    path('addSale/',views.addsale,name="addsale"),
    path('addstock/',views.addstockData,name="addstock"),
    path('addpurchase/',views.addpurchase,name="addpurchase"),
    path('addrecivable/',views.addrecivable,name="addrecivable"),
    path('addpayable/',views.addpayable,name="addpayable"),
    path('EditSale/',views.EditSale,name="editsale"),
    path('EditSaleRecord/<int:userid>/<int:stid>/<int:stsale>/<int:stpri>/<int:Recivebale>/',views.Editpruchase,name="salerecord"),
    path('EditPurchase/',views.Editpruchase,name="editPurchase"),
    path('EditPurchaseRecord/<int:userid>/<int:stid>/<int:stpurchase>/<int:stpri>/<int:payable>/',views.EditpruchaseRecord,name="purchaserecord"),
    path('editrecivable/',views.EditRecivable,name="editrecivable"),
    path('editrecivableRecord/<int:userid>/<int:recivableAmount>/',views.EditRecivableRecord,name="editrecivableRecord"),
    path('editPayable/',views.EditPayable,name="editPayable"),
    path('editpayableRecord/<int:userid>/<int:PayableAmount>/',views.EditPayableRecord,name="editpayablerecord"),
    path('totalBalance/',views.AllUserBalance,name="totalbalance"),
]
