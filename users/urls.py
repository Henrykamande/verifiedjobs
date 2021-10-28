from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

path('login/', views.loginUser, name='login'),
path('logout/', views.logoutUser, name='logout'),
path('register/', views.registerUser, name='register'),


path('', views.profiles, name="profiles"),
path('profile/<str:pk>', views.userProfile, name="user_profile"),
path('account/', views.userAccount, name='account'),

path('edit-account/', views.editAccount, name='edit_account'),

path('account-pending_approval/', views.AccountPendingApproval, name='pending_approval'),

path('admin-dashboard/', views.adminAccount, name='admin_dashboard'),
path('view-application/<str:pk>', views.viewapplication, name= "view_agency_application"),
path('approve/<str:pk>', views.approveAgency, name= "approve_agency"),
path('suspend/<str:pk>', views.suspendAgency, name= "suspend_agency"),
path('reapprove/<str:pk>', views.reapproveAgency, name= "reapprove_agency"),


#path('create-skill/', views.createSkill, name='create_skill'),

#path('update-skill/<str:pk>', views.updateSkill, name='update_skill'),
#path('delete-skill/<str:pk>', views.deleteSkill, name='delete_skill'),




path('inbox/', views.inbox, name="inbox"),
path('applications/', views.applications, name="applications"),

path('message/<str:pk>', views.viewMessage, name="message"),
path('viewapplication/<str:pk>', views.viewApplication, name="viewApplication"),

path("send-message/<str:pk>/",views.createMessage, name="create_message"),
path("application/<str:pk>/",views.applicationMessage, name="application"),


path('reset_password/',auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name= "reset_password"),
path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"), name="password_reset_done"),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/reset_password_form.html"), name="password_reset_confirm"),
path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_done.html"), name= "password_reset_complete"),


] 