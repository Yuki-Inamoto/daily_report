from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Report(models.Model):
    user_id = models.ForeignKey(User)
    pub_date = models.DateField() # 日報の作成日
    edit_date = models.DateTimeField('edit') # 日報の最終更新日
    title = models.CharField(max_length=100)  # 日報タイトル(100文字制限)
    content = models.CharField(max_length=500)  # 日報内容(500文字制限)

    def __str__(self):              # __unicode__ on Python 2
        return self.title
    
    def was_published_recently(self):
        return self.edit_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'edit_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
# Create your models here.
