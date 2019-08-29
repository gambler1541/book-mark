from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # 장고에서 사용하는 메서드
    # 객체의 상세 화면 주소를 반환하게 만듬(detail)
    # reverse메서드는 URL패턴의 이름과 추가 인자를 전달받아 URL을 생성하는 메서드
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])