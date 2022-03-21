from rest_framework.routers import SimpleRouter

from credit_carts.views import CartCreditView

router = SimpleRouter()

router.register('cards', CartCreditView)

urlpatterns = []

urlpatterns += router.urls
