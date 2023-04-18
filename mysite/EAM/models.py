from django.db import models
# 资产表
class Asset(models.Model):
    ip=models.CharField(max_length=30)
    region=models.CharField(max_length=30,null=True,blank=True)
    area=models.CharField(max_length=30,null=True,blank=True)
    asset_name=models.CharField(max_length=30,null=True,blank=True)
    product_name=models.CharField(max_length=30,null=True,blank=True)
    system_classification=models.CharField(max_length=30,null=True,blank=True)
    system_grading=models.CharField(max_length=30,null=True,blank=True)
    administrator=models.CharField(max_length=30,null=True,blank=True)
    create_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ip
#扫描结果表
class scan(models.Model):
    ip=models.CharField(max_length=30)
    port=models.IntegerField()
    service=models.CharField(max_length=30,null=True,blank=True)
    asset_name=models.CharField(max_length=30,null=True,blank=True)
    system_classification=models.CharField(max_length=30,null=True,blank=True)
    system_grading=models.CharField(max_length=30,null=True,blank=True)
    administrator=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.ip
#端口表
class ip_port(models.Model):
    ip=models.ForeignKey(Asset,on_delete=models.CASCADE)
    port=models.IntegerField()
    service=models.CharField(max_length=30)
    def __str__(self):
        return self.ip
#端口新增表
class increase(models.Model):
    ip=models.CharField(max_length=30)
    port=models.CharField(max_length=30)
    service=models.CharField(max_length=30)
    is_first_increase=models.BooleanField()
    def __str__(self):
        return self.ip
#端口减少表
class decrease(models.Model):
    ip=models.CharField(max_length=30)
    port=models.IntegerField()
    service=models.CharField(max_length=30)
    is_last_decrease=models.BooleanField()
    def __str__(self):
        return self.ip
#通知表
class notification(models.Model):
    ip=models.CharField(max_length=30)
    port=models.IntegerField()
    asset_name=models.CharField(max_length=30,null=True,blank=True)
    product_name=models.CharField(max_length=30,null=True,blank=True)
    administrator=models.CharField(max_length=30,null=True,blank=True)
    Increase_or_Decrease=models.TextChoices('Increase_or_Decrease','新增 减少')
    increase_or_decrease=models.CharField(max_length=30,choices=Increase_or_Decrease.choices)
    def __str__(self):
        return self.ip
#漏洞表
class vulnerabilities(models.Model):
    ip=models.ForeignKey(Asset,on_delete=models.CASCADE)
    hole=models.CharField(max_length=30)
    IS_FIX=models.TextChoices('IS_FIX','修复 未修复')
    is_fix=models.CharField(max_length=30,choices=IS_FIX.choices)
    def __str__(self):
        return self.ip
#弱口令表
class Weak_password(models.Model):
    ip=models.ForeignKey(Asset,on_delete=models.CASCADE)
    weak_type=models.CharField(max_length=30)
    user=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.ip



