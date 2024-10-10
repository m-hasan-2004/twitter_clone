from django.db import models
from django.utils.translation import gettext as _
from uuid import uuid4

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    author = models.ForeignKey("users.User", verbose_name=_("Author"), on_delete=models.CASCADE)
    pic = models.ImageField(_("Post Image"), upload_to="images/posts", height_field=None, width_field=None, max_length=None)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_modified = models.DateTimeField(_("Date Modified"), auto_now=True)
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        
    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey("users.User", verbose_name=_("User"), on_delete=models.CASCADE)
    post = models.ForeignKey("social.Post", verbose_name=_("Post"), on_delete=models.CASCADE, related_name="likes")
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")

    def __str__(self):
        return f"|{self.user}| liked {self.post.title}"
    
    
class Follow(models.Model):
    follower = models.ForeignKey("users.User", verbose_name=_("Follower"), on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey("users.User", verbose_name=_("Following"), on_delete=models.CASCADE, related_name="following")
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Follow")
        verbose_name_plural = _("Follows")

    def __str__(self):
        return f"user: {self.follower} is following {self.following}"
    
    
class Comment(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"))
    post = models.ForeignKey("social.post", verbose_name=_("Post"), on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("users.user", verbose_name=_("User"), on_delete=models.CASCADE, related_name="user")
    date_created = models.TimeField(_("Date Created"), auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        
    def __str__(self):
        return f"COMMENT OF {self.author} ON {self.post}"
    