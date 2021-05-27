from django.db import models

class USER(models.Model):
    username = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class StockData(models.Model):
    TotalStockQuantity = models.IntegerField()
    StockName = models.CharField(max_length=50)
    StockPrice = models.IntegerField(default=0)
    def __str__(self):
        return self.StockName

class SALE(models.Model):
    userID = models.ForeignKey(USER,on_delete=models.CASCADE)
    stockID = models.ForeignKey(StockData,on_delete=models.CASCADE)
    StockQuantitySale = models.IntegerField()
    StockPrice = models.IntegerField()
    TotalRecivable = models.IntegerField()
    DateData = models.DateField()


class Purchase(models.Model):
    userID = models.ForeignKey(USER,on_delete=models.CASCADE)
    stockID = models.ForeignKey(StockData,on_delete=models.CASCADE)
    StockQuantityPurchase = models.IntegerField()
    StockPrice = models.IntegerField()
    Totalpayable = models.IntegerField()
    DateData = models.DateField()


class AddPayable(models.Model):
    userID = models.ForeignKey(USER,on_delete=models.CASCADE)
    DateData = models.DateField()
    PayableAmount = models.IntegerField()

class AddRecivable(models.Model):
    userID = models.ForeignKey(USER,on_delete=models.CASCADE)
    DateData = models.DateField()
    RecivableAmount = models.IntegerField()

class UserBalance(models.Model):
    userID = models.ForeignKey(USER,on_delete=models.CASCADE)
    TotalBalance = models.IntegerField(default=0)
    DateData = models.DateField()
