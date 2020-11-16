from django.shortcuts import render
from django.http import HttpResponse

from .models import CommentItem
# Create your views here.
def index(request):
    all_count = CommentItem.objects.all().count()
    plus = CommentItem.objects.filter(comment_sen__gt = 0.5).count()
    minus = CommentItem.objects.filter(comment_sen__lte = 0.5).count()
    top10_info = []
    for i in range(1,11):
        rank = i

        comments = CommentItem.objects.filter(comment_rank=i)

        title = comments[0].comment_title
        comment_count = comments.count()

        good_count = 0
        good_all = 0
        bad_count = 0
        bad_all = 0
        for comment in comments:
            temp = comment.comment_sen
            if temp>0.5:
                good_all += temp
                good_count += 1
            else:
                bad_all += temp
                bad_count += 1
        
        if good_count != 0:
            good_avg = good_all/good_count
        else:
            good_avg = 0
        if bad_count != 0:
            bad_avg = bad_all/bad_count
        else:
            bad_avg = 0
        if comment_count != 0:
            avg = (good_all+bad_all)/comment_count
        else:
            avg = 0

        info = [rank,title,comment_count,good_count,bad_count,avg]
        top10_info.append(info)

    return render(request, 'index.html', locals())