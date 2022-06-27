from django.shortcuts import redirect,  render, get_object_or_404

from .models import New, Comment, Like, Dislike
from .forms import NewForm, NewFormMine, CommentForm

def news_list(request):
    news = New.objects.all().order_by('-created') # queryset 
    # context dictionaly bu templatega berib yuborilgan o'zgaruvchilar to'plami
    # buyerda New modelidagi barcha object yani ikki yokii undan ortiq
    # objectni oldik
    # bu narsa QUERYSET deyiladi
    # queryset uchun model method ishlamaydi

    # context dictionary bu templatega berib yuborilgan oz'garuvchilar to'plami
    context = {'news': news}
    return render(request, 'new/news_list.html', context)

def news_detail(request, id):
    new= get_object_or_404(New, id=id)
    # bitta newni olayapmiz New degan modelning barcha objectlarni ichidan
    # shu narsa object deyeladi
    # model methodlarni faqat object uchun ishlaydi
    form = CommentForm()

    if request.method == "POST":
        # commet formaga postda kelayotgan malumotlarni
        # berib validatsiyadan o'tkazamiz
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = new
            if request.user.is_authenticated:
                comment.author = request.user
            comment.save()
            return redirect("new:detail", id=id)
    return render(request, 'new/news_detail.html', {'new': new, "form": form})


def create(request):
    form = NewForm()
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save()
            return redirect("new:list")

    return render(request, 'new/create.html', {"form": form})

def remove(request, id):
    new = get_object_or_404(New, id=id)
    new.delate()
    return redirect("new:list")

def my_news(request):
    news = New.objects.filter(author=request.user).order_by('created')
    return render(request, 'new/my_news.html', {'news': news})

def my_create(request):
    form = NewFormMine()
    if request.method == 'POST':
        form = NewFormMine(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.author = request.user
            new.save()
            return redirect("new:my_news")

    return render(request, 'new/create.html', {"form": form})

def my_detail(request, id):
    new = get_object_or_404(New, id=id)
    
    return render(request, 'new/my_detail.html', {'new': new})

def like(request, id):
    new = get_object_or_404(New, id=id)
    if request.user.is_authenticated:
        if new.likes.filter(user=request.user).exists():
            new.likes.get(user=request.user).delate()
            return JsonResponse({
                "success": True,
                "message": "Siz reaksiyangizni qaytarib oldingiz!",
                "likes": new.like.count()
                }
            )
        Like.object.create(user=request.user, post=new)
        return JsonResponse({
            "success": True,
            "message": "Sizga yoqgan postlar safiga qo'shiladi!",
            "likes": new.like.count()
            }
        )
    return JsonResponse({
            "success": False,
            "message": "Postga reaktsiya bildirish uchun iltimos royhatan o'ting",
            }
        )
    
def dislike(request, id):
    new = get_object_or_404(New, id=id)
    if request.user.is_authenticated:
        if new.dislikes.filter(user=request.user).exists():
            new.dislikes.get(user=request.user).delate()
            return JsonResponse({
                "success": True,
                "message": "Siz reaksiyangizni qaytarib oldingiz!",
                "dislikes": new.dislikes.count()
                }
            )
        Like.object.create(user=request.user, post=new)
        return JsonResponse({
            "success": True,
            "message": "Sizga yoqmagan postlar safiga qo'shiladi!",
            "likes": new.dislikes.count()
            }
        )
    return JsonResponse({
            "success": False,
            "message": "Postga reaktsiya bildirish uchun iltimos royhatan o'ting",
            }
        )