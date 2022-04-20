from rest_framework import routers

from .api.views import EventsView

router = routers.SimpleRouter()
router.register(r'v1/events', EventsView)

urlpatterns = router.urls
