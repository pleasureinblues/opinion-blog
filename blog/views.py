from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Category, Post, Comment, Tag, Contact, Feedback
from blog.forms import ContactForm, CategoryForm, FeedbackForm, CommentForm, PostForm, TagForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-name')[:5]
    post_list = Post.objects.order_by('-posted')[:7]
    context_dict = {'categories': category_list, 'post_list': post_list}
    response = render(request,'blog/index.html', context_dict)
    return response


def home(request):
    context_dict = {'ahmed' : 'Ahmed Khan'}
    response = render(request,'blog/index.html', context_dict)
    return response


def categories(request):
    category_list = Category.objects.order_by('-name')
    context_dict = {'categories': category_list}
    response = render(request,'blog/categories.html', context_dict)
    return response


def blog_post(request, blog_post_slug):
    post_detail = Post.objects.get(slug=blog_post_slug)
    current_user = request.user
    comments = Comment.objects.filter(post=post_detail.id)
    tags = Tag.objects.filter(post=post_detail.id)
    form = CommentForm(request.POST or None)
    tagform = TagForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post_detail
        comment.commenter = current_user
        comment.save()
        return redirect(request.path)

    if tagform.is_valid():
        post_id = post_detail.id
        post_for_tag = Post.objects.get(id=post_id)

        tag_title_from_form = tagform['tag_title'].value().strip().lower()
        tag_title_from_form = tag_title_from_form.rstrip(',')
        striped_tags = tag_title_from_form.split(',')
        for t in striped_tags:
            print (t)
            try:
                nt = t.strip()
                existing_tag = Tag.objects.get(tag_title__iexact=nt)
                post_for_tag.tag_set.add(existing_tag)
            except Tag.DoesNotExist:
                nt = t.strip()
                new_tag = Tag(tag_title=nt)
                new_tag.save()
                post_for_tag.tag_set.add(new_tag)
            continue
        return redirect(request.path)
    context_dict = {'post': post_detail, 'slug': blog_post_slug, 'comments':comments, 'tags':tags, 'form':form, 'tagform':tagform}
    response = render(request,'blog/blog_post.html', context_dict)
    return response


def add_post(request):
    if request.method == 'POST':
        form1Post = PostForm(request.POST)
        form2Tags = TagForm(request.POST)

        if form1Post.is_valid() and form2Tags.is_valid():
            post = form1Post.save()
            #post_instance_for_tag = post.save()
            tag_title_from_form = form2Tags['tag_title'].value().strip().lower()
            tag_title_from_form = tag_title_from_form.rstrip(',')
            striped_tags = tag_title_from_form.split(',')
            for t in striped_tags:
                received_tag = t.strip()
                tag, created = Tag.objects.get_or_create(tag_title=received_tag)
                post.tag_set.add(tag)
            return index(request)
        else:
            print (form1Post.errors)
            print (form2Tags.errors)
    else:
        form1Post = PostForm()
        form2Tags = TagForm()

    return render(request, 'blog/add_post.html', {'form1':form1Post,'form2':form2Tags})


def comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index (request)
        else:
            print (form.errors)
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form':form})


def category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    context_dict = {}
    context_dict['category_name'] = category.name
    posts = Post.objects.filter(category=category)
    context_dict['posts'] = posts
    context_dict['category'] = category
    return render(request, 'blog/category.html', context_dict)


#Add Category Veiw
#@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print (form.errors)
    else:
        form = CategoryForm()

    return render(request, 'blog/add_category.html', {'form':form})



def tag(request, tag_name_slug):
    tag_name = Tag.objects.filter(tag_title=tag_name_slug)
    tag_id = Tag.objects.get(pk=tag_name)
    posts = Post.objects.all().filter(tag=tag_id)
    context_dict = {}
    context_dict['tag_name'] = tag_name_slug
    context_dict['posts'] = posts
    return render(request, 'blog/posts_by_tags.html', context_dict)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index (request)
        else:
            print (form.errors)
    else:
        form = ContactForm()

    return render(request, 'blog/contact_form.html', {'form':form})


def contact_messages(request):
    message_list = Contact.objects.all()
    context_dict = {'messages': message_list}
    return render(request,'blog/contact_messages.html',context_dict,)


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index (request)
        else:
            print (form.errors)
    else:
        form = FeedbackForm()

    return render(request, 'blog/feedback_form.html', {'form':form})


def feedback(request):
    message_list = Feedback.objects.all()
    context_dict = {'messages': message_list}
    return render(request,'blog/feedback_rcvd.html',context_dict,)