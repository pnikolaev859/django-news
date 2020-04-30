from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from articles.models import Article, Comment
from .forms import CommentForm

class ArticlesListView(ListView):
    template_name = 'articles/articles_list.html'
    model = Article
    paginate_by = 3


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
            request,
            'articles/articles_detail.html',
            {
                'article': article,
                'comments': comments,
                'new_comment': new_comment,
                'comment_form': comment_form
            })

def about(request):
    return HttpResponse('О проекте')
