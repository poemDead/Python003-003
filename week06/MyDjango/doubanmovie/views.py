from django.shortcuts import render

# Create your views here.
from .models import Douban1917
from django.db.models import Avg

def movies_short(request):
    shorts = Douban1917.objects.all()
    counts = Douban1917.objects.all().count()
    for short in shorts:
        if short.star == '力荐':
            short.star_num = 5
        elif short.star == '推荐':
            short.star_num = 4
        elif short.star == '还行':
            short.star_num = 3
        elif short.star == '较差':
            short.star_num = 2
        else:
            short.star_num = 1
    good_short = []
    for short in shorts:
        if short.star_num > 3:
            good_short.append(short)
    good_short_num = len(good_short)

    return render(request, 'results.html', locals())

