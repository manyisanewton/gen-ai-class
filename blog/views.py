from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm


# View for displaying list of blog posts
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Latest posts first
    return render(request, 'blog/post_list.html', {'posts': posts})

# View for individual blog post + comment form
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)  # ✅ Match URL name

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })
