from django.db import models
from django.forms import DateField

# Create your models here.
class comreg1(models.Model):
    
    #comid=models.CharField( max_length=10)
    comname=models.CharField( max_length=100)
    comgstno=models.CharField( max_length=20)
    commob=models.CharField( max_length=10)
    comemail=models.CharField( max_length=50)
    comaddress=models.CharField( max_length=320)
    compassword=models.CharField( max_length=10)
    comrepassword=models.CharField( max_length=10)
    comgstcopy=models.FileField(max_length=20, upload_to='company', blank=True, null=True )
    
    class Meta:
        db_table="comreg"

class proddetails1(models.Model):
    #comid=models.CharField( max_length=10)
	#id=models.IntegerField()
    proid=models.IntegerField()
    proname=models.CharField( max_length=50)
    procatag=models.CharField( max_length=10)
    protype=models.CharField( max_length=10)
    proquant=models.CharField(max_length=100)
    propic=models.FileField(max_length=300, upload_to='product', blank=True, null=True )
    proprice=models.CharField( max_length=10)
    prodisc=models.CharField( max_length=300)
    Bidstartdate=models.DateField()
    Bidenddate=models.DateField()
    
    class Meta:
        db_table="tblprodetails"

class quatationdet(models.Model):

    prod_id=models.IntegerField()
    prod_name=models.CharField( max_length=100)
    com_name=models.CharField( max_length=100)
    com_mob=models.CharField( max_length=100)
    price=models.CharField( max_length=100)
    delev_date=models.DateField()
    status=models.CharField( max_length=100)

    class Meta:
        db_table="quatation"


class activeorder1(models.Model):

    proid=models.IntegerField()
    proname=models.CharField( max_length=100)
    com_name=models.CharField( max_length=100)
    com_mob=models.CharField( max_length=100)
    price=models.CharField( max_length=100)
    delev_date=models.DateField()
    status=models.CharField( max_length=100)
    Order_Status=models.CharField( max_length=100)

    class Meta:
        db_table="active_order"


class orderstatus1(models.Model):

    proid=models.IntegerField()
    proname=models.CharField( max_length=100)
    com_name=models.CharField( max_length=100)
    com_mob=models.CharField( max_length=100)
    price=models.CharField( max_length=100)
    delev_date=models.DateField()
    Order_Status=models.CharField( max_length=100)

    class Meta:
        db_table="order_active_status"