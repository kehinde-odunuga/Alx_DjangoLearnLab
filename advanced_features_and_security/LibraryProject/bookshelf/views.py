from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

@permission_required('your_app_name.can_view', raise_exception=True)
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})

@permission_required('your_app_name.can_create', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        # Handle post creation
        pass
    return render(request, 'create_post.html')

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Handle post editing
        pass
    return render(request, 'edit_post.html', {'post': post})

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
    return render(request, 'delete_post.html')
