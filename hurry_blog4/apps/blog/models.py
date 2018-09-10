from django.db import models
from django.utils.timezone import now
# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', blank=True, null=True)
    status = models.CharField(verbose_name='状态', max_length=1, choices=STATUS_CHOICES, default='p')
    pub_time = models.DateTimeField(verbose_name='发布时间', blank=True, null=True)


    # 使对象在后台显示更友好
    def __str__(self):
        return self.title


    # 下一篇
    def next_article(self):  # id比当前id大，状态为已发布，发布时间不为空
        return Article.objects.filter(id__gt=self.id, status='p', pub_time__isnull=False).first()

    # 前一篇
    def prev_article(self):  # id比当前id小，状态为已发布，发布时间不为空
        return Article.objects.filter(id__lt=self.id, status='p', pub_time__isnull=False).first()

    class Meta:
        ordering = ['-pub_time']  # 按文章创建日期降序
        verbose_name = '文章'  # 指定后台显示模型名称
        verbose_name_plural = '文章列表'  # 指定后台显示模型复数名称
        db_table = 'article'  # 数据库表名