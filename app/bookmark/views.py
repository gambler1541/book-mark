from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Bookmark

class BookmarkListView(ListView):
    # html에서 object라는 변수명으로 사용
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    # 입력 받을 필드
    fields = ['site_name', 'url']
    # 글쓰기를 완료하고 이동할 페이지
    # 보통 상세페이지로 이동
    success_url = reverse_lazy('list')
    # 기본적으로 설정되어 잇는 템플릿 이름들은 모델명_xxx의 형태
    # CreateView와 UpdateView는 form이 접미사인데 이걸 변경해서 bookmark_create라는 이름의 템플릿 파일을 사용하도록 설정
    template_name_suffix = '_create'


class BookmarkDetail(DetailView):
    model = Bookmark


class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name',
              'url',
              ]
    template_name_suffix = '_update'


