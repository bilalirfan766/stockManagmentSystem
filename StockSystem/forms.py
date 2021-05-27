from django import forms


from .models import USER,StockData,SALE,Purchase,AddRecivable,AddPayable

from bootstrap_datepicker_plus import DatePickerInput
class UserForm(forms.ModelForm):
    class Meta:
        model = USER
        fields = ['username']


class UserStockDataForm(forms.ModelForm):
    class Meta:
        model = StockData
        fields = ['StockName','StockPrice','TotalStockQuantity']

class DateInput(forms.DateInput):
    input_type = 'date'

class SaleFormm(forms.ModelForm):
    class Meta:
        model = SALE
        fields = ['userID','stockID','StockQuantitySale','StockPrice','DateData']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets={'DateData':DateInput()}


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['userID','stockID','StockQuantityPurchase','StockPrice','DateData']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets={'DateData':DateInput()}

class AddRecivableForm(forms.ModelForm):
    class Meta:
        model = AddRecivable
        fields = ['userID','DateData','RecivableAmount']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets={'DateData':DateInput()}

class AddPayableForm(forms.ModelForm):
    class Meta:
        model = AddPayable
        fields = ['userID', 'DateData', 'PayableAmount']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets = {'DateData': DateInput()}


class EditSaleFormm(forms.ModelForm):
    class Meta:
        model = SALE
        fields = ['userID','stockID']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets={'DateData':DateInput()}

class EditSaleFormmRecords(forms.ModelForm):
    class Meta:
        model = SALE
        fields = ['userID','stockID','StockQuantitySale','StockPrice','DateData']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets={'DateData':DateInput()}



class EditPurchaseFormm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['userID','stockID']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets={'DateData':DateInput()}

class EditPurchaseFormmRecords(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['userID','stockID','StockQuantityPurchase','StockPrice','DateData']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets={'DateData':DateInput()}

class EditRecivableForm(forms.ModelForm):
    class Meta:
        model = AddRecivable
        fields = ['userID']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets = {'DateData': DateInput()}


class EditRecivableFormRecord(forms.ModelForm):
    class Meta:
        model = AddRecivable
        fields = ['userID', 'DateData', 'RecivableAmount']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets = {'DateData': DateInput()}


class EditPurchaseableForm(forms.ModelForm):
    class Meta:
        model = AddPayable
        fields = ['userID']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets = {'DateData': DateInput()}


class EditPurchasableFormRecord(forms.ModelForm):
    class Meta:
        model = AddPayable
        fields = ['userID', 'DateData', 'PayableAmount']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets = {'DateData': DateInput()}