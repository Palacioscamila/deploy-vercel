from django.shortcuts import render
from django.shortcuts import redirect 
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
# Create your views here.
def index(request):
    articles = Article.objects.all() 
    params = {    
        'articles': articles,
    }
    return render(request, 'blog/index.html', params) 


def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title=title, content=content)
        article.save()
        messages.add_message(request, messages.SUCCESS, "Blog creado por.")    # añadir
        return redirect('index')
    else:
        params = {
            'form': ArticleForm(),
        }
        return render(request, 'blog/create.html', params)
    
def detail(request, article_id): # --- 1
    article = Article.objects.get(id=article_id) # --- 2
    params = {
        'article': article,
    }
    return render(request, 'blog/detail.html', params)

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('detail', article_id)  # 1
    else:
       form = ArticleForm(initial={
            'title': article.title,
            'content': article.content,
            })
       params = {
            'article': article,
            'form': form,
        }
       return render(request, 'blog/edit.html', params)
   
def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article.delete()
        return redirect('index')
    else:
        params = {
            'article': article,
        }
        return render(request, 'blog/delete.html', params)
