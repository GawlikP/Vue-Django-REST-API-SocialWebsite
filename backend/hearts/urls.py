
from .views import HeartViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', HeartViewSet, basename='heart')
urlpatterns = router.urls