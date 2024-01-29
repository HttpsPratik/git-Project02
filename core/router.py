from rest_framework import routers
from crud.views import  CommentViewsets

router = routers.DefaultRouter()
router.register(r'comment', CommentViewsets)