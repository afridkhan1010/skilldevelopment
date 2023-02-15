from django.urls import path
from . import views

urlpatterns = [





    path('links/', views.AllLinks.as_view(),name="links"),
    path('', views.AllLinks.as_view(),name="links"),

    # path('test/', views.Simple.as_view(), name='test'),

    # path('test/<id>/', views.Update_det.as_view(), name='test'),
    path('links/<id>', views.Links.as_view(),name="links"),

    # path('links/<id>/', views.Update_link.as_view(), name='updatelink'),
    path('comments/<id>',views.Comments.as_view(), name='comments'),
    path('comments/',views.AllComments.as_view(), name='comments'),
    # # path('commentsonly/<id>',views.Commentsonly.as_view(), name='commentsonly'),
    path('report/<id>',views.Reports.as_view(), name='report'),
    path('report/',views.Reports.as_view(), name='report'),
    path("hotlinks", views.DashBoard.as_view(),name='hotlinks')


]