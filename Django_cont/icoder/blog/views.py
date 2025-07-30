from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from collections import defaultdict


def bloghome(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return render(request, 'blog/bloghome.html', context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    # comments = BlogComment.objects.filter(post=post)
    # print(request.user)
    # context = {'post': post, 'comments': comments, 'user': request.user, 'comment_count': comments.count()}
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    # print(replyDict)
    context = {
        'post': post,
        'comments': comments,
        'replyDict': replyDict,
        'user': request.user,
        'count': BlogComment.objects.filter(post=post).count()
    }
    return render(request, 'blog/blogpost.html', context)

@login_required
def handle_comment(request):
    if request.method == "POST":
        comment_text = request.POST.get("Comment")
        post_sno = request.POST.get("postSno")
        parent_sno = request.POST.get("parentSno")
        
        post = Post.objects.get(sno=post_sno)
        user = request.user

        if parent_sno:
            parent = BlogComment.objects.get(sno=parent_sno)
            comment = BlogComment(comment=comment_text, user=user, post=post, parent=parent)
            
        else:
            comment = BlogComment(comment=comment_text, user=user, post=post)
        
        comment.save()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'Comment saved'}, status=200)

        return redirect(f"/blog/{post.slug}")

