from django.db import models

# Create your models here.
# 我们新建了一个Person类，继承自models.Model,
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.__doc__ + ":name>" + self.name

# 新增一张用户表，表名为user 字段user_name, psw ,mail 都是字符串类型
class User(models.Model):
    user_name = models.CharField(max_length=30,
                                 primary_key=True)   # 设置为主键
    psw = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    def __str__(self):
        return self.__doc__ + ":user_name->" + self.user_name


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=30)  # 标题
    body = models.TextField()  # 正文
    auth = models.CharField(max_length=10)  # 作者
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_time = models.DateTimeField(auto_now=True)  # 最后更新时间
    def __str__(self):
        return self.__doc__ + "title->" + self.title


class Card(models.Model):
    '''银行卡 基本信息 '''
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    card_id = models.CharField(max_length=30, verbose_name="卡号", default="")
    card_user = models.CharField(max_length=10, verbose_name="姓名", default="")
    add_time = models.DateField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = '银行卡账户'
        verbose_name = "银行卡账户_基本信息"

    def __str__(self):
        return self.card_id