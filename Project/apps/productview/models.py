from django.db import models
# Create your models here.


# 产品模型类
class ProductTable(models.Model):
    """产品模型类"""
    pro_name = models.CharField(max_length=20, verbose_name='产品名称')
    pro_version = models.CharField(max_length=20, verbose_name='产品版本')
    pro_pict = models.ImageField(verbose_name='产品图片')

    class Meta:
        db_table = 'df_product'
        verbose_name = '产品'
        verbose_name_plural = verbose_name


# 产品图片模型类
class ProductPictureTable(models.Model):
    """产品图片模型类"""
    pro_pict = models.ImageField(verbose_name='产品图片')

    class Meta:
        db_table = 'df_product_picture'
        verbose_name = '产品图片'
        verbose_name_plural = verbose_name


# 产品版本模型类
class ProductVersionTable(models.Model):
    """产品版本模型类"""
    ver_name = models.CharField(max_length=20, verbose_name='版本名称')

    class Meta:
        db_table = 'df_product_version'
        verbose_name = '产品版本'
        verbose_name_plural = verbose_name


# 产品展示模型类
class ProductPerformTable(models.Model):
    """产品展示模型类"""
    pro_name = models.CharField(max_length=20, verbose_name='产品名称')
    pro_version = models.CharField(max_length=20, verbose_name='产品版本')
    pro_pict = models.ImageField(verbose_name='产品图片')

    class Meta:
        db_table = 'df_product_perform'
        verbose_name = '产品展示'
        verbose_name_plural = verbose_name


# 新增产品模型类
class NewProductTable(models.Model):
    """新增产品模型类"""
    pro_model = models.IntegerField(verbose_name='产品型号')
    pro_name = models.CharField(max_length=20, verbose_name='产品名称')
    pro_version = models.CharField(max_length=20, verbose_name='产品版本')

    class Meta:
        db_table = 'df_new_product'
        verbose_name = '新增产品'
        verbose_name_plural = verbose_name


# 产品价格模型类
class ProductPriceTable(models.Model):
    """产品价格模型类"""
    pro_version = models.CharField(max_length=20, verbose_name='产品版本')
    hardware_cost = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='硬件成本')
    fir_software_cost = models.DecimalField(max_digits=20, decimal_places=2,verbose_name='首次软件成本')
    deve_cycle = models.DateField(verbose_name='开发周期')
    single_hard_cost= models.DecimalField(max_digits=10, decimal_places=2,verbose_name='单次硬性成本')
    single_cost_total = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='单次成本合计')
    batch_cost_total = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='批量成本合计')
    cost_prop = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='成本比例')
    actual_exte = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='实际对外')
    agent_prop = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='代理比例')
    profit_shar = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='利润分成')
    exte_profit = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='对外利润')
    actual_profit = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='实际利润')
    profit_require = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='利润要求')
    pro_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='产品售价')
    actual_profit_margin = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='实际利润率')
    exte_profit_margin = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='对外利润率')


    class Meta:
        db_table = 'df_product_price'
        verbose_name = '产品售价'
        verbose_name_plural = verbose_name


# 产品记录模型类
class ProductRecordTable(models.Model):
    """产品记录模型类"""
    pro_model = models.CharField(max_length=10,verbose_name='产品型号')
    pro_name = models.CharField(max_length=20,verbose_name='产品名称')
    pro_version = models.CharField(max_length=20,verbose_name='产品版本')
    deve_cost = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='研发成本')
    batch_cost = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='批量成本')
    pro_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='产品售价')
    fill_in_date = models.DateField(verbose_name='填报时间')
    update_date = models.DateField(verbose_name='更新时间')
    persion = models.CharField(max_length=20,verbose_name='负责人')
    fill_in_state = models.CharField(max_length=10,verbose_name='填报状态')
    operation = models.CharField(max_length=10,verbose_name='操作')


    class Meta:
        db_table = 'df_product_record'
        verbose_name = '产品记录'
        verbose_name_plural = verbose_name


# 首页轮播产品模型类
class RotationProductTable(models.Model):
    """首页轮播产品模型类"""
    pro_name = models.CharField(max_length=20, verbose_name='产品名称')
    pro_pict = models.CharField(max_length=20, verbose_name='产品图片')


    class Meta:
        db_table = 'df_rotation_product'
        verbose_name = '首页轮播产品图片'
        verbose_name_plural = verbose_name


# 硬件产品模型类
class HardwareProductTable(models.Model):
    """硬件产品模型类"""
    hp_name = models.CharField(max_length=20, verbose_name='硬件名称')
    hp_model = models.CharField(max_length=10,verbose_name='硬件型号')
    hp_num = models.IntegerField(verbose_name='数量')
    hp_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价（万）')
    hp_total_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='总价（万）')
    hp_second = models.CharField(max_length=10, verbose_name='二次使用')
    hp_second_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='二次使用价格（万）')
    hp_boss_one = models.CharField(max_length=10, verbose_name='推荐供应商1')
    hp_boss_two = models.CharField(max_length=10, verbose_name='推荐供应商2')
    hp_boss_three = models.CharField(max_length=10, verbose_name='推荐供应商3')

    class Meta:
        db_table = 'df_hardware_product'
        verbose_name = '硬件产品'
        verbose_name_plural = verbose_name


# 软件产品模型类
class SoftwareProductTable(models.Model):
    """软件产品模型类"""
    sp_name = models.CharField(max_length=20, verbose_name='软件名称')
    sp_content = models.CharField(max_length=10,verbose_name='主要内容')
    sp_num = models.IntegerField(verbose_name='数量')
    sp_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价（万）')
    sp_total_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='总价（万）')
    sp_second = models.CharField(max_length=10, verbose_name='二次使用')
    sp_second_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='二次使用价格（万）')
    sp_boss_one = models.CharField(max_length=10, verbose_name='推荐供应商1')
    sp_boss_two = models.CharField(max_length=10, verbose_name='推荐供应商2')
    sp_boss_three = models.CharField(max_length=10, verbose_name='推荐供应商3')

    class Meta:
        db_table = 'df_software_product'
        verbose_name = '软件产品'
        verbose_name_plural = verbose_name