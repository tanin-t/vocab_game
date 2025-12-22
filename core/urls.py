"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vocab.views import learn_word, welcome, choose_vocab_set, game_eng_thai, game_eng_thai_answer
from user.views import login_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('welcome/', welcome),
    path('vocab-set/<int:vocab_set_id>/vocab/<int:vocab_index>/', learn_word), # learn_word(request, pk=5)
    path('vocab-set/', choose_vocab_set),

    path('login/', login_view),

    path('game/eng-thai/', game_eng_thai),
    path('game/eng-thai/answer/', game_eng_thai_answer),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
