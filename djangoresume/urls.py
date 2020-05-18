from django.contrib import admin
from django.urls import path
from resumebuilder import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),

    # AUTH
    path('signup', views.Signup.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    # CRUD
    # path('resume/create', views.CreateResume.as_view(), name='create_resume'),
    path('resume/create', views.create_resume, name='create_resume'),
    path('resume/<int:pk>', views.DetailResume.as_view(), name='detail_resume'),
    path('resume/<int:pk>/update', views.UpdateResume.as_view(), name='update_resume'),
    path('resume/<int:pk>/delete', views.DeleteResume.as_view(), name='delete_resume'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
