from django.db import models
from django.conf import settings
# Create your models here.
#�� ����
class PostType(models.Model):
    name = models.CharField('',max_length=50)
    def __str__(self):
        return self.name
    
#��
class Post(models.Model):
    type = models.ForeignKey(PostType,on_delete=models.CASCADE)
    headline = models.CharField('제목',max_length = 200)
    content = models.TextField('글',null=True,blank=True)
    #auto_now_add = True : ��ü�� �����Ǵ� ������ ��¥/�ð� ������ �⺻������ ���
    pub_date = models.DateField('작성일',auto_now_add=True)
    #User ��Ŭ������ ����� ��
    
    #settings.AUTH_USER_MODEL �Ǵ� User�� Ŭ������ ��밡��
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#�̹���
class Image(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField('사진',upload_to='images/%Y/%m/%d')
    def delete(self,using=None,keep_parnets=False):
        #image������ ����� ����� ������ ����� �۾�
        #why? Image��ü�� �������� iamge����� ������ �������������Ƿ�
        #��ü�� �����Ǵ� delete�Լ� ���� �̹��������� �����Ǵ� �ڵ带 ����
        self.image.delete()
        return models.Model.delete(self,using=using,keep_parents=keep_parnets)
#����
class File(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    file = models.FileField('파일',upload_to='files/%Y/%m/%d')
    def delete(self, using=None, keep_parents=False):
        self.file.delete()
        return models.Model.delete(self, using=using, keep_parents=keep_parents)