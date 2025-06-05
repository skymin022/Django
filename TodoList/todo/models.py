from django.db import models

# Create your models here.
class Todo(models.Model):
    STATUS_CHOICE = [
        ('WAIT', '대기'),
        ('ING', '진행'),
        ('DONE', '완료')
    ]
    no = models.AutoField(primary_key=True)     # 자동 증가 필드(PK)
    title = models.CharField(max_length=255)
    status = models.CharField(
                            max_length=20,
                            choices=STATUS_CHOICE,
                            default='WAIT'
                            )
    creadted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} : {}".format(self.title, self.status)