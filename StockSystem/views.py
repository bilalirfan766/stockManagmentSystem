from django.shortcuts import render
from .forms import UserForm,UserStockDataForm,SaleFormm,PurchaseForm,AddPayableForm,AddRecivableForm,EditSaleFormm,EditSaleFormmRecords,EditPurchaseFormmRecords,EditPurchaseFormm,EditRecivableForm,EditPurchaseableForm
from .models import USER,StockData,SALE,Purchase,AddRecivable,AddPayable,UserBalance
from .forms import EditRecivableFormRecord,EditPurchasableFormRecord
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'dashboard.html')

def addsale(request):
    if request.method == "POST":
        fm = SaleFormm(request.POST)
        if fm.is_valid():
            UserID = fm.cleaned_data['userID']
            stockID=fm.cleaned_data['stockID']
            StockQuantitySale=fm.cleaned_data['StockQuantitySale']
            StockPrice=fm.cleaned_data['StockPrice']
            DateData=fm.cleaned_data['DateData']
            print("Stock ID",stockID)
            Total_R=(float(StockPrice))*(float(StockQuantitySale))
            FetchStockData = StockData.objects.get(StockName=str(stockID))
            stockName=FetchStockData.StockName
            print("Stock Name",stockName)
            stockQualtityStockTabel=FetchStockData.TotalStockQuantity
            print("Stock Quantity",stockQualtityStockTabel)
            total_sum=stockQualtityStockTabel-StockQuantitySale
            if total_sum>0:
                StockData.objects.filter(StockName=stockID).update(StockName=str(stockID),TotalStockQuantity=total_sum)
                print("Stock Updated")
            stockData = SALE(userID=UserID,stockID=stockID,StockQuantitySale=StockQuantitySale,StockPrice=StockPrice,TotalRecivable=Total_R,DateData=DateData)
            stockData.save()
            userBalance=UserBalance.objects.get(userID=UserID)
            getBalance=userBalance.TotalBalance
            TotalBalance=getBalance+Total_R
            UserBalance.objects.filter(userID=UserID).update(userID=UserID,TotalBalance=TotalBalance,DateData=DateData)
            messages.success(request, 'Your Sale Has been Added in Database')
            fm = UserStockDataForm()
            print("Sale is save in Database")
    else:
        fm = SaleFormm()
        print("Sale is not save")
    return render(request,'addSale.html',{'form':fm})


def addpurchase(request):
    if request.method == "POST":
        fm = PurchaseForm(request.POST)
        if fm.is_valid():
            UserID = fm.cleaned_data['userID']
            stockID=fm.cleaned_data['stockID']
            StockQuantityPurchase=fm.cleaned_data['StockQuantityPurchase']
            StockPrice=fm.cleaned_data['StockPrice']
            DateData=fm.cleaned_data['DateData']
            print("Stock ID",stockID)
            Total_P=(float(StockPrice))*(float(StockQuantityPurchase))
            FetchStockData = StockData.objects.get(StockName=str(stockID))
            stockName=FetchStockData.StockName
            print("Stock Name",stockName)
            stockQualtityStockTabel=FetchStockData.TotalStockQuantity
            print("Stock Quantity",stockQualtityStockTabel)
            total_sum=stockQualtityStockTabel+StockQuantityPurchase
            if total_sum>0:
                StockData.objects.filter(StockName=stockID).update(StockName=str(stockID),TotalStockQuantity=total_sum)
                print("Stock Updated")
            stockData = Purchase(userID=UserID,stockID=stockID,StockQuantityPurchase=StockQuantityPurchase,StockPrice=StockPrice,Totalpayable=Total_P,DateData=DateData)
            stockData.save()

            userBalance = UserBalance.objects.get(userID=UserID)
            getBalance = userBalance.TotalBalance
            TotalBalance = getBalance - Total_P
            UserBalance.objects.filter(userID=UserID).update(userID=UserID, TotalBalance=TotalBalance,
                                                             DateData=DateData)
            messages.success(request, 'Your Purchase Has been Added in Database')
            fm = UserStockDataForm()
            print("Purchase is save in Database")
    else:
        fm = PurchaseForm()
        print("Purchase is not save")
    return render(request,'addpurchase.html',{'form':fm})

def addrecivable(request):
    if request.method == "POST":
        fm = AddRecivableForm(request.POST)
        if fm.is_valid():
            userid=fm.cleaned_data['userID']
            DateData=fm.cleaned_data['DateData']
            RecivableAmount=fm.cleaned_data['RecivableAmount']
            userrec=AddRecivable(userID=userid,DateData=DateData,RecivableAmount=RecivableAmount)
            messages.success(request, 'Amount Has been Receieved')
            userrec.save()

            userBalance = UserBalance.objects.get(userID=userid)
            getBalance = userBalance.TotalBalance
            TotalBalance = getBalance - RecivableAmount
            UserBalance.objects.filter(userID=userid).update(userID=userid, TotalBalance=TotalBalance,
                                                             DateData=DateData)
            fm = AddRecivableForm()
    else:
        fm = AddRecivableForm()
    return render(request, 'addrecivable.html', {'form': fm})

def addpayable(request):
    if request.method == "POST":
        fm = AddPayableForm(request.POST)
        if fm.is_valid():
            userid=fm.cleaned_data['userID']
            DateData=fm.cleaned_data['DateData']
            PayableAmount=fm.cleaned_data['PayableAmount']
            userrec=AddPayable(userID=userid,DateData=DateData,PayableAmount=PayableAmount)
            messages.success(request, 'Amount Has been Paid')
            userrec.save()

            userBalance = UserBalance.objects.get(userID=userid)
            getBalance = userBalance.TotalBalance
            TotalBalance = getBalance + PayableAmount
            UserBalance.objects.filter(userID=userid).update(userID=userid, TotalBalance=TotalBalance,
                                                             DateData=DateData)
            fm = AddPayableForm()
    else:
        fm =AddPayableForm()
    return render(request, 'addpayable.html', {'form': fm})


def adduser(request):
    if request.method == "POST":
        fm = UserForm(request.POST)
        if fm.is_valid():
            usernameinput = fm.cleaned_data['username']
            userdata = USER(username=usernameinput)
            userdata.save()
            user = USER.objects.get(username=usernameinput)
            userbalance=UserBalance(userID=user,TotalBalance=0,DateData='2021-01-01')
            userbalance.save()
            messages.success(request,'Your record Has been Added in Database')
            fm = UserForm()
            print("User is save in Database")
    else:
        fm = UserForm()
        print("User is not save")
    return render(request,'adduser.html',{'form':fm})
def addstockData(request):
    if request.method == "POST":
        fm = UserStockDataForm(request.POST)
        if fm.is_valid():
            stockNameInput = fm.cleaned_data['StockName']
            StockPrice=fm.cleaned_data["StockPrice"]
            TotalStockQuantity=fm.cleaned_data["TotalStockQuantity"]
            stockData = StockData(StockName=stockNameInput,StockPrice=StockPrice,TotalStockQuantity=TotalStockQuantity)
            stockData.save()
            messages.success(request, 'Your Stock Has been Added in Database')
            fm = UserStockDataForm()
            print("Stock is save in Database")
    else:
        fm = UserStockDataForm()
        print("Stock is not save")
    return render(request,'addstock.html',{'form':fm})


def EditSale(request):
    if request.method == "POST":
        fm = EditSaleFormm(request.POST)
        if fm.is_valid():
            userid=fm.cleaned_data['userID']
            stockid=fm.cleaned_data['stockID']
            sale_data = SALE.objects.filter(userID=userid,stockID=stockid).values('userID','stockID','StockQuantitySale', 'StockPrice','TotalRecivable','DateData')
            print(sale_data)
            messages.info(request,'Edit Sale Data')
            return render(request, 'EditSale.html', {'form': fm,'SALE':sale_data})

    else:
        fm = EditSaleFormm()
    return render(request, 'EditSale.html', {'form': fm})


def EditSaleRecord(request,stid,userid,stsale,stpri,Recivebale):
    print("id",stid)
    print("user",userid)
    print("stsale",stsale)
    print("price",stpri)
    if request.method == "POST":
        fm = EditSaleFormmRecords(request.POST)
        if fm.is_valid():
            userID=fm.cleaned_data['userID']
            stockID=fm.cleaned_data['stockID']
            StockQuantitySale=fm.cleaned_data['StockQuantitySale']
            StockPrice=fm.cleaned_data['StockPrice']
            totalRec=StockQuantitySale*StockPrice
            DateTime=fm.cleaned_data['DateData']
            SALE.objects.filter(userID=userid,stockID=stid,StockQuantitySale=stsale,StockPrice=stpri).update(userID=userID,stockID=stockID,StockQuantitySale=StockQuantitySale,StockPrice=StockPrice,TotalRecivable=totalRec,DateData=DateTime)
            messages.success(request,"Your Data Has Been Updated")
            fm = EditSaleFormmRecords()
            userBalanceuserID = UserBalance.objects.get(userID=userid)
            userBalancevalue=(userBalanceuserID.TotalBalance)
            userBalancevalue=int(userBalancevalue)
            if int(userBalancevalue)>0:
                userBalancevalue=userBalancevalue-int(Recivebale)
                userBalancevalue=userBalancevalue+int(totalRec)
            elif int(userBalancevalue)<0:
                userBalancevalue=userBalancevalue+int(Recivebale)
                userBalancevalue=userBalancevalue-int(totalRec)
            UserBalance.objects.filter(userID=userid).update(userID=userid, TotalBalance=int(userBalancevalue),
                                                             DateData=DateTime)
    else:
        fm = EditSaleFormmRecords(initial = {'userID': userid,'stockID':stid,'StockQuantitySale':stsale,'StockPrice':stpri})
    return render(request, 'EditSaleRecords.html', {'form': fm})

def Editpruchase(request):
    if request.method == "POST":
        fm = EditPurchaseFormm(request.POST)
        if fm.is_valid():
            userid=fm.cleaned_data['userID']
            stockid=fm.cleaned_data['stockID']
            purchase_data = Purchase.objects.filter(userID=userid,stockID=stockid).values('userID','stockID','StockQuantityPurchase','StockPrice','DateData','Totalpayable')
            print(purchase_data)
            messages.info(request,'Purchase Data')
            return render(request, 'EditPurchase.html', {'form': fm,'Purchase': purchase_data})

    else:
        fm = EditPurchaseFormm()
    return render(request, 'EditPurchase.html', {'form': fm})


def EditpruchaseRecord(request,stid,userid,stpurchase,stpri,payable):
    print("id",stid)
    print("user",userid)
    print("stsale",stpurchase)
    print("price",stpri)
    if request.method == "POST":
        fm = EditPurchaseFormmRecords(request.POST)
        if fm.is_valid():
            userID=fm.cleaned_data['userID']
            stockID=fm.cleaned_data['stockID']
            StockQuantityPurchase=fm.cleaned_data['StockQuantityPurchase']
            StockPrice=fm.cleaned_data['StockPrice']
            totalPay=StockQuantityPurchase*StockPrice
            DateTime=fm.cleaned_data['DateData']
            Purchase.objects.filter(userID=userid,stockID=stid,StockQuantityPurchase=stpurchase,StockPrice=stpri).update(userID=userID,stockID=stockID,StockQuantityPurchase=StockQuantityPurchase,StockPrice=StockPrice,Totalpayable=totalPay,DateData=DateTime)
            messages.success(request,"Your Data Has Been Updated")
            fm = EditPurchaseFormmRecords()
            userBalanceuserID = UserBalance.objects.get(userID=userid)
            userBalancevalue=(userBalanceuserID.TotalBalance)
            userBalancevalue=int(userBalancevalue)
            if payable>0:
                Payable=payable*(-1)
            if int(userBalancevalue) < 0:
                userBalancevalue=userBalancevalue+int(Payable)
                userBalancevalue=userBalancevalue-int(totalPay)
            elif int(userBalancevalue) > 0:
                userBalancevalue=userBalancevalue-int(Payable)
                userBalancevalue=userBalancevalue+int(totalPay)
            UserBalance.objects.filter(userID=userid).update(userID=userid, TotalBalance=int(userBalancevalue),
                                                             DateData=DateTime)
    else:
        fm = EditPurchaseFormmRecords(initial = {'userID': userid,'stockID':stid,'StockQuantityPurchase':stpurchase,'StockPrice':stpri})
    return render(request, 'EditPurchaseRecord.html', {'form': fm})


def EditRecivable(request):
    if request.method == "POST":
        fm = EditRecivableForm(request.POST)
        if fm.is_valid():
            userID = fm.cleaned_data['userID']
            recivable = AddRecivable.objects.filter(userID=userID).values('userID','RecivableAmount','DateData')
            messages.info(request, 'Recivable Data')
            return render(request, 'EditRecivable.html', {'form': fm, 'recivable': recivable})
    else:
        fm = EditRecivableForm()
    return render(request, 'EditRecivable.html', {'form': fm})



def EditPayable(request):
    if request.method == "POST":
        fm = EditPurchaseableForm(request.POST)
        if fm.is_valid():
            userID = fm.cleaned_data['userID']
            payable = AddPayable.objects.filter(userID=userID).values('userID','PayableAmount','DateData')
            messages.info(request, 'Purchasable Data')
            return render(request, 'EditPurchasbale.html', {'form': fm, 'payable': payable})
    else:
        fm = EditPurchaseableForm()
    return render(request, 'EditPurchasbale.html', {'form': fm})



def EditRecivableRecord(request,userid,recivableAmount):
    if request.method == "POST":
        fm = EditRecivableFormRecord(request.POST)
        if fm.is_valid():
            userID=fm.cleaned_data['userID']
            RecivableAmount=fm.cleaned_data['RecivableAmount']
            AddRecivable.objects.filter(userID=userid,RecivableAmount=recivableAmount).update(RecivableAmount=RecivableAmount)
            messages.success(request,"Your Data Has Been Updated")
            fm = EditRecivableFormRecord()
            userBalanceuserID = UserBalance.objects.get(userID=userid)
            userBalancevalue=(userBalanceuserID.TotalBalance)
            userBalancevalue=int(userBalancevalue)
            if int(userBalancevalue) < 0:
                userBalancevalue=userBalancevalue+int(recivableAmount)
                userBalancevalue=userBalancevalue-int(RecivableAmount)
            elif int(userBalancevalue) > 0:
                userBalancevalue=userBalancevalue-int(recivableAmount)
                userBalancevalue=userBalancevalue+int(RecivableAmount)
            UserBalance.objects.filter(userID=userid).update(userID=userid, TotalBalance=int(userBalancevalue))
    else:
        fm = EditRecivableFormRecord(initial = {'userID': userid,'RecivableAmount':recivableAmount})
    return render(request, 'EditSaleRecords.html', {'form': fm})



def EditPayableRecord(request,userid,PayableAmount):
    if request.method == "POST":
        fm =EditPurchasableFormRecord(request.POST)
        if fm.is_valid():
            userID=fm.cleaned_data['userID']
            PayableAmountinput=fm.cleaned_data['PayableAmount']
            AddPayable.objects.filter(userID=userid,PayableAmount=PayableAmount).update(PayableAmount=PayableAmountinput)
            messages.success(request,"Your Data Has Been Updated")
            fm = EditPurchasableFormRecord()
            userBalanceuserID = UserBalance.objects.get(userID=userid)
            userBalancevalue=(userBalanceuserID.TotalBalance)
            userBalancevalue=int(userBalancevalue)
            if int(userBalancevalue) < 0:
                userBalancevalue=userBalancevalue-int(PayableAmount)
                userBalancevalue=userBalancevalue+int(PayableAmountinput)
            elif int(userBalancevalue) > 0:
                userBalancevalue = userBalancevalue + int(PayableAmount)
                userBalancevalue = userBalancevalue - int(PayableAmountinput)
            UserBalance.objects.filter(userID=userid).update(userID=userid, TotalBalance=int(userBalancevalue))
    else:
        fm = EditPurchasableFormRecord(initial = {'userID': userid,'PayableAmount':PayableAmount})
    return render(request, 'EditPurchaseRecord.html', {'form': fm})


def AllUserBalance(request):
    print(request.method)
    allData = UserBalance.objects.all()
    valueGet=allData.values()
    Sum=0
    for k in range(0,len(valueGet)):
        extractValue=valueGet[k]
        Sum=Sum+(int(extractValue['TotalBalance']))
    print("Sum",Sum)
    return render(request,'AllUsers.html',{'balance':allData,'Results':Sum})







