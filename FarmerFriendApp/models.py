from distutils.command.upload import upload
from django.db import models

# Create your models here.

class variety(models.Model):
    vr_rid = models.AutoField(primary_key=True)
    vr_name = models.CharField(max_length=50)

class crop(models.Model):
    crop_rid = models.AutoField(primary_key=True)
    crop_type = models.IntegerField()
    crop_name = models.CharField(max_length=75)
    crop_variety = models.ForeignKey('variety',on_delete=models.CASCADE)
    crop_disease = models.ForeignKey('disease',on_delete=models.CASCADE)
    crop_duration = models.IntegerField()
    crop_image_url = models.ImageField(upload_to='crop/')

class user(models.Model):
    u_rid = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=50)
    u_contact = models.CharField(max_length=15)
    u_password = models.CharField(max_length=50)
    u_email = models.CharField(max_length=50)
    u_address = models.CharField(max_length=100)
    u_pin = models.CharField(max_length=10)

class sell(models.Model):
    sell_rid = models.AutoField(primary_key=True)
    sell_user_rid = models.ForeignKey('user',on_delete=models.CASCADE)
    sell_crop_rid = models.ForeignKey('crop',on_delete=models.CASCADE)
    sell_quantity = models.FloatField()
    sell_unit_price = models.FloatField()
    sell_total_price = models.FloatField()
    sell_date = models.CharField(max_length=20)
    sell_desc = models.CharField(max_length=500)

class buy(models.Model):
    buy_rid = models.AutoField(primary_key=True)
    buy_user_rid = models.ForeignKey('user',on_delete=models.CASCADE)
    buy_sell_rid = models.ForeignKey('sell',on_delete=models.CASCADE)
    buy_qty = models.FloatField()
    buy_date = models.CharField(max_length=20)

class disease(models.Model):
    ds_rid = models.AutoField(primary_key=True)
    ds_name = models.CharField(max_length=45)
    ds_desc = models.CharField(max_length=500)
    ds_control_methods = models.CharField(max_length=500)

class symptom(models.Model):
    sym_rid = models.AutoField(primary_key=True)
    sym_name = models.CharField(max_length=50)

class disease_symptom_map(models.Model):
    dsm_rid = models.AutoField(primary_key=True)
    dsm_disease_rid = models.ForeignKey('disease',on_delete=models.CASCADE)
    dsm_symptom_rid = models.ForeignKey('symptom',on_delete=models.CASCADE)

class machines(models.Model):
    mc_rid = models.AutoField(primary_key=True)
    mc_id = models.CharField(max_length=45)
    mc_name = models.CharField(max_length=45)
    mc_price = models.IntegerField()
    mc_contact = models.CharField(max_length=15)
    mc_image_url = models.ImageField(upload_to='machines/')

class news(models.Model):
    nw_rid = models.AutoField(primary_key=True)
    nw_title = models.CharField(max_length=50)
    nw_body = models.CharField(max_length=500)
    nw_date_time = models.CharField(max_length=20)
    nw_img_url = models.ImageField(upload_to='news/')

class notification(models.Model):
    not_rid = models.AutoField(primary_key=True)
    not_title = models.CharField(max_length=50)
    not_body = models.CharField(max_length=500)
    not_date_time = models.CharField(max_length=20)

class price(models.Model):
    pr_rid = models.AutoField(primary_key=True)
    pr_crop_id = models.ForeignKey('crop',on_delete=models.CASCADE)
    pr_price = models.IntegerField()
    pr_updated_datetime = models.CharField(max_length=20)

class schemes(models.Model):
    sc_rid = models.AutoField(primary_key=True)
    sc_id = models.CharField(max_length=50)
    sc_title = models.CharField(max_length=75)
    sc_description = models.CharField(max_length=500)
    sc_img_url = models.ImageField(upload_to='schemes/')
    sc_date_time = models.CharField(max_length=20)

class video(models.Model):
    vd_rid = models.AutoField(primary_key=True)
    vd_title = models.CharField(max_length=75)
    vd_thumbnail_url = models.ImageField(upload_to='video/')
    vd_video_url = models.FileField(upload_to='video/')
    vd_type = models.IntegerField()

class weather(models.Model):
    wt_rid = models.AutoField(primary_key=True)
    wt_precipitation = models.IntegerField()
    wt_humidity = models.IntegerField()
    wt_wind = models.IntegerField()
    wt_date = models.CharField(max_length=20)
