from sre_constants import SUCCESS
from tempfile import template
from unicodedata import name
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .form import loginform,changepassword,Mypassword,Mypasswordconfrim
from app import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.products.as_view(),name='producvt'),
    path('product-detail/<int:pk>',views.product_detail.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profileview.as_view(), name='profile'),
    path('address/<int:pk>', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=changepassword,success_url='/changepassworddone/'),name='changepassword'),
    path('changepassworddone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/home.html'),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=Mypassword,),name='Password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=Mypasswordconfrim,),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=loginform), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/',views.customerregistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
