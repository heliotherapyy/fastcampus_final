from django.db import models
from django.conf import settings


class Photo(models.Model):
    """사진 정보를 담는 모델. 필요한 모델 필드를 추가하세요.
    """
    title = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photo_owner')  # noqa
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_users', blank=True)  # noqa
    image_file = models.ImageField(upload_to='%Y/%m/%d/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    """사진에 다는 댓글 모델. 필요한 모델 필드를 추가하세요.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comment_owner')  # noqa
    photo = models.ForeignKey(Photo)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content
