from django.contrib import admin
from blog.models import Category, Post, Comment, Tag, Contact, Feedback

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'posted', 'category')
    prepopulated_fields = {'slug':('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('tag_title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','commented_on','comment_body','commenter')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name','email','like_dislike','feedback_msg')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Feedback, FeedbackAdmin)