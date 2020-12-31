from django.db import models


class IntellPropRecordTable(models.Model):
    """知识产权记录模型类"""
    softwork = models.CharField(max_length=30, verbose_name='软著')
    paper = models.CharField(max_length=30, verbose_name='论文')
    patent = models.CharField(max_length=30, verbose_name='专利')

    class Meta:
        db_table = 'df_intell_prop_record'
        verbose_name = '知识产权记录'
        verbose_name_plural = verbose_name


class SoftworkTable(models.Model):
    """软著模型类"""
    sw_model_choices = (
        (0, '独立开发'),
        (1, '委托开发')
    )
    sw_state_choices = (
        (0, '登记'),
        (1, '申请')
    )
    sw_name = models.CharField(max_length=30, verbose_name='软著名称')
    sw_model = models.CharField(max_length=20, choices=sw_model_choices, verbose_name='软著类型')
    sw_reg_num = models.IntegerField(verbose_name='登记号')
    sw_reg_date = models.DateField(verbose_name='登记日期')
    sw_state = models.CharField(max_length=10, choices=sw_state_choices, verbose_name='软著状态')
    sw_author = models.CharField(max_length=10, verbose_name='著作权人')
    uploade_people = models.CharField(max_length=10, verbose_name='上传人')

    class Meta:
        db_table = 'df_softwork'
        verbose_name = '软著'
        verbose_name_plural = verbose_name


class ViewSoftworkTable(models.Model):
    """查看软著模型类"""
    sw_model_choices = (
        (0, '独立开发'),
        (1, '委托开发')
    )
    sw_state_choices = (
        (0, '登记'),
        (1, '申请')
    )
    sw_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    sw_name = models.CharField(max_length=30, verbose_name='软著名称')
    sw_model = models.CharField(max_length=20, choices=sw_model_choices, verbose_name='软著类型')
    sw_reg_date = models.DateField(verbose_name='登记日期')
    sw_author = models.CharField(max_length=10, verbose_name='著作权人')
    sw_reg_num = models.IntegerField(verbose_name='登记号')
    sw_state = models.CharField(max_length=10, choices=sw_state_choices, verbose_name='软著状态')
    sw_enclosure = models.FileField(choices=sw_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_view_softwork'
        verbose_name = '查看软著'
        verbose_name_plural = verbose_name


class NewSoftworkTable(models.Model):
    """新增软著模型类"""
    sw_model_choices = (
        (0, '独立开发'),
        (1, '委托开发')
    )
    sw_state_choices = (
        (0, '登记'),
        (1, '申请')
    )
    sw_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    sw_name = models.CharField(max_length=30, verbose_name='软著名称')
    sw_model = models.CharField(max_length=20, choices=sw_model_choices, verbose_name='软著类型')
    sw_reg_date = models.DateField(verbose_name='登记日期')
    sw_author = models.CharField(max_length=10, verbose_name='著作权人')
    sw_reg_num = models.IntegerField(verbose_name='登记号')
    sw_state = models.CharField(max_length=10, choices=sw_state_choices, verbose_name='软著状态')
    sw_enclosure = models.FileField(choices=sw_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_new_softwork'
        verbose_name = '新增软著'
        verbose_name_plural = verbose_name


class DeleteSoftworkTable(models.Model):
    """删除软著模型类"""
    sw_model_choices = (
        (1, '独立开发'),
        (2, '委托开发')
    )
    sw_state_choices = (
        (0, '登记'),
        (1, '申请')
    )
    sw_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    sw_name = models.CharField(max_length=30, verbose_name='软著名称')
    sw_model = models.CharField(max_length=20, choices=sw_model_choices, verbose_name='软著类型')
    sw_reg_date = models.DateField(verbose_name='登记日期')
    sw_author = models.CharField(max_length=10, verbose_name='著作权人')
    sw_reg_num = models.IntegerField(verbose_name='登记号')
    sw_state = models.CharField(max_length=10, choices=sw_state_choices, verbose_name='软著状态')
    sw_enclosure = models.FileField(choices=sw_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_delete_softwork'
        verbose_name = '删除软著'
        verbose_name_plural = verbose_name


class PaperTable(models.Model):
    """论文模型类"""
    pap_state_choices = (
        (0, '已录用'),
        (1, '已发表')
    )
    pap_model_choices = (
        (0, 'SCI'),
        (1, 'EI'),
        (2, '核心'),
        (3, '普通')
    )
    pap_subject = models.CharField(max_length=30, verbose_name='论文题目')
    pap_paper = models.CharField(max_length=30, verbose_name='论文期刊')
    pap_model = models.CharField(max_length=20, choices=pap_model_choices, verbose_name='论文类型')
    pap_publish_date = models.DateField(verbose_name='发表日期')
    pap_author = models.CharField(max_length=10, verbose_name='论文作者')
    uploade_people = models.CharField(max_length=10, verbose_name='上传人')
    pap_state = models.CharField(max_length=10, choices=pap_state_choices, verbose_name='状态')

    class Meta:
        db_table = 'df_paper'
        verbose_name = '论文'
        verbose_name_plural = verbose_name


class ViewPaperTable(models.Model):
    """查看论文模型类"""
    pap_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    pap_subject = models.CharField(max_length=30, verbose_name='论文题目')
    pap_paper = models.CharField(max_length=30, verbose_name='论文期刊')
    pap_model = models.CharField(max_length=20, verbose_name='论文类型')
    pap_publish_date = models.DateField(verbose_name='发表日期')
    pap_author = models.CharField(max_length=10, verbose_name='论文作者')
    pap_enclosure = models.FileField(choices=pap_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_view_paper'
        verbose_name = '查看论文'
        verbose_name_plural = verbose_name


class NewPaperTable(models.Model):
    """新增论文模型类"""
    pap_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    pap_subject = models.CharField(max_length=30, verbose_name='论文题目')
    pap_paper = models.CharField(max_length=30, verbose_name='论文期刊')
    pap_model = models.CharField(max_length=20, verbose_name='论文类型')
    pap_publish_date = models.DateField(verbose_name='发表日期')
    pap_author = models.CharField(max_length=10, verbose_name='论文作者')
    pap_enclosure = models.FileField(choices=pap_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_new_paper'
        verbose_name = '新增论文'
        verbose_name_plural = verbose_name


class DeletePaperTable(models.Model):
    """删除论文模型类"""
    pap_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    pap_subject = models.CharField(max_length=30, verbose_name='论文题目')
    pap_paper = models.CharField(max_length=30, verbose_name='论文期刊')
    pap_model = models.CharField(max_length=20, verbose_name='论文类型')
    pap_publish_date = models.DateField(verbose_name='发表日期')
    pap_author = models.CharField(max_length=10, verbose_name='论文作者')
    pap_enclosure = models.FileField(choices=pap_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_delete_paper'
        verbose_name = '删除论文'
        verbose_name_plural = verbose_name


class PatentTable(models.Model):
    """专利模型类"""
    pat_model_choices = (
        (0, '实用新型'),
        (1, '发明专利'),
        (2, '外观专利')
    )
    pat_name = models.CharField(max_length=20, verbose_name='专利名称')
    pat_model = models.CharField(max_length=20, verbose_name='专利类型')
    pat_num = models.IntegerField(verbose_name='专利号')
    pat_apply_date = models.DateField(verbose_name='专利申请日期')
    pat_author = models.CharField(max_length=10, verbose_name='作者')
    pat_grant_auth_date = models.DateField(verbose_name='授权公告日期')
    pat_grant_auth_num = models.IntegerField(verbose_name='授权号')
    uploade_people = models.CharField(max_length=10, verbose_name='上传人')

    class Meta:
        db_table = 'df_patent'
        verbose_name = '专利'
        verbose_name_plural = verbose_name


class ViewPatentTable(models.Model):
    """查看专利模型类"""
    pat_model_choices = (
        (0, '实用新型'),
        (1, '发明专利'),
        (2, '外观专利')
    )
    pat_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    pat_name = models.CharField(max_length=20, verbose_name='专利名称')
    pat_model = models.CharField(max_length=20, choices=pat_model_choices, verbose_name='专利类型')
    pat_apply_date = models.DateField(verbose_name='专利申请日期')
    pat_author = models.CharField(max_length=10, verbose_name='作者')
    pat_grant_auth_num = models.IntegerField(verbose_name='授权号')
    pat_grant_auth_date = models.DateField(verbose_name='授权公告日期')
    pat_enclosure = models.FileField(choices=pat_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_view_patent'
        verbose_name = '查看专利'
        verbose_name_plural = verbose_name


class NewPatentTable(models.Model):
    """新增专利模型类"""
    pat_model_choices = (
        (0, '实用新型'),
        (1, '发明专利'),
        (2, '外观专利')
    )
    pat_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    pat_name = models.CharField(max_length=20, verbose_name='专利名称')
    pat_model = models.CharField(max_length=20, choices=pat_model_choices, verbose_name='专利类型')
    pat_apply_date = models.DateField(verbose_name='专利申请日期')
    pat_author = models.CharField(max_length=10, verbose_name='作者')
    pat_grant_auth_num = models.IntegerField(verbose_name='授权号')
    pat_grant_auth_date = models.DateField(verbose_name='授权公告日期')
    pat_enclosure = models.FileField(choices=pat_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_new_patent'
        verbose_name = '新增专利'
        verbose_name_plural = verbose_name


class DeletePatentTable(models.Model):
    """删除专利模型类"""
    pat_model_choices = (
        (0, '实用新型'),
        (1, '发明专利'),
        (2, '外观专利')
    )
    pat_enclosure_choices = (
        (0, '选择'),
        (1, '上传'),
        (2, '删除')
    )
    pat_name = models.CharField(max_length=20, verbose_name='专利名称')
    pat_model = models.CharField(max_length=20, choices=pat_model_choices, verbose_name='专利类型')
    pat_apply_date = models.DateField(verbose_name='专利申请日期')
    pat_author = models.CharField(max_length=10, verbose_name='作者')
    pat_grant_auth_num = models.IntegerField(verbose_name='授权号')
    pat_grant_auth_date = models.DateField(verbose_name='授权公告日期')
    pat_enclosure = models.FileField(choices=pat_enclosure_choices, verbose_name='附件')

    class Meta:
        db_table = 'df_delete_patent'
        verbose_name = '删除专利'
        verbose_name_plural = verbose_name



