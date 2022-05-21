from django.urls import path
from main.views import *

app_name = "main"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about-us", AboutView.as_view(), name="about"),
    path("contact-us", ContactView.as_view(), name="contact"),
    path("page/<slug:slug>", PageView.as_view(), name="page"),
    path("apply-scholorship", ScholorshipView.as_view(), name="scholorship"),
    path("membership", MembershipView.as_view(), name="membership"),
    path("membership/teacher", MembershipTeacherView.as_view(),
         name="membership-teacher"),
    path("membership/below-10th", Membership10thView.as_view(),
         name="membership-below-10th"),
    path("membership/12th", Membership12thView.as_view(), name="membership-12th"),
    path("free-counselling", FreeCounsellingView.as_view(), name="free_counselling"),
]
