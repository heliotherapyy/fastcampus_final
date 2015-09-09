"""Pystagram MVP version tests.
Usage : python manage.py test
"""
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import (
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    HttpResponseForbidden,
    HttpResponseServerError,
)
from django.contrib.auth.decorators import login_required

from .models import (
    Photo,
    Comment,
)
from .forms import (
    PhotoForm,
    CommentForm,
)

from django.contrib import messages


def list_photo(request):
    """사진을 목록으로 나열합니다.
    """
    # todo
    photos = Photo.objects.all()

    return render(request, 'list_photo.html', {
        'photos': photos,
    })

# 최상단 화면의 Upload 버튼이 동작하질 않음
def create_photo(request):
    """새 사진을 게시합니다.
    """
    status_code = 200
    # todo```

    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()

            messages.success(request, "새로운 사진이 업로드 되었습니다!")

            return redirect('mvp.views.list_photo')
    else:
        form = PhotoForm()
    return render(request, 'create_photo.html', {
        'form': form,
    }, status=status_code)


def detail_photo(request, pk):
    """개별 사진과 사진에 달린 댓글을 보여줍니다.
    :param str pk: photo primary key.
    """
    # todo
    photo = get_object_or_404(Photo, pk=pk)

    return render(request, 'detail_photo.html', {
        'photo': photo,
    })


def delete_photo(request, pk):
    """지정한 사진을 지웁니다.
    :param str pk: photo primary key.
    """
    if request.method != 'POST':
        return HttpResponseNotAllowed('not allowed method')
    photo = get_object_or_404(Photo, pk=pk)

    if (
        photo.user != request.user and
        not request.user.is_staff and
        not request.user.is_superuser
    ):
        return HttpResponseForbidden('required permission to delete')

    try:
        photo.delete()
    except Exception:
        return HttpResponseServerError('something wrong')

    return redirect('mvp.views.list_photo')


def create_comment(request, pk):
    """지정한 사진에 댓글을 추가합니다.
    :param str pk: photo primary key.
    """
    status_code = 200
    # todo

    photo = get_object_or_404(Photo, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.photo = get_object_or_404(Photo, pk=pk)
            comment.save()
            messages.success(request, "댓글이 작성되었습니다")
            return redirect('mvp.views.detail_photo', pk)

    else:
        form = CommentForm()
    return render(request, 'form.html', {
        'photo': photo,
        'form': form,
    }, status=status_code)


def delete_comment(request, pk):
    """지정한 댓글을 지웁니다.
    :param str pk: comment primary key.
    """
    if request.method != 'POST':
        return HttpResponseNotAllowed('not allowed method')

    comment = get_object_or_404(Comment, pk=pk)

    if comment.user != request.user:
        return HttpResponseForbidden('required permission to delete')

    # todo
    comment.delete()
    return redirect('mvp.views.detail_photo', comment.photo.pk)


def like_photo(request, pk):
    """지정한 사진에 좋아요 표식을 남기거나 취소합니다.
    :param str pk: photo primary key.
    """
    # todo

    photo = get_object_or_404(Photo, pk = pk)

    if photo.user == request.user:
        return HttpResponseBadRequest('not allowed to like own photo')

    if photo.likes.filter(pk = request.user.pk).exists():
        photo.likes.remove(request.user)
        return redirect('mvp.views.detail_photo', photo.pk)

    else:
        if photo.user != request.user:
            photo.likes.add(request.user)
            return redirect('mvp.views.detail_photo', photo.pk)
        else:
            return render(request, 'detail_photo.html', {
                'photo': photo,
            }, status=400)
