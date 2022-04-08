from rest_framework import routers

from .api.view import EventsView

router = routers.SimpleRouter()
router.register(r'v1/events', EventsView)

urlpatterns = router.urls
