# Main Views of NPUSPTA

from datetime import date
from django.shortcuts import render
from django.urls import reverse_lazy
from core.utils import Viewer, CustomCreateView
from main.models import *
from django.views.generic import CreateView
from django import forms
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

PAGES = {
    "private-school-fee-regulation-bill": 1,
    "security-of-service-to-employees-bill": 2,
    "donate-us": 3,
    "free-health-and-accident-insurance-cover-for-member-students": 4,
    "free-cet-neet-coaching": 5,
    "essay-competition": 6
}


class IndexView(Viewer):
    template_name = "index.html"

    def get_context(self):
        self.context['is_mobile'] = True if "Mobile" in self.request.headers.get(
            "User-Agent") else False
        self.context["notices"] = Notice.objects.all()
        return super().get_context()


class AboutView(Viewer):
    template_name = "about.html"


class ContactView(CreateView):
    template_name = "contact.html"
    model = Contact
    fields = "__all__"
    success_url = reverse_lazy("main:contact")

    def form_valid(self, form):
        text = f'''
        We have received your message. If your inquiry is urgent, please use the phone number to talk to us. 
        Otherwise, we will reply by email as soon as possible.
        Talk to you soon,'''
        messages.success(self.request, text)
        name = form.cleaned_data["name"]
        mail_context = form.cleaned_data
        send_mail(
            subject=f"NPUSPTA | User: {name} sent a message",
            message = "simple message",
            html_message = render_to_string("email templates/contact_admin.html", mail_context),
            from_email="mail@npuspta.org",
            recipient_list=["bharat.anaik2003@gmail.com"])
        return super().form_valid(form)




class PageView(Viewer):
    def get(self, request, *args, **kwargs):
        page_slug = kwargs.get("slug")
        self.template_name = f"pages/page{PAGES[page_slug]}.html"
        return super().get(request, *args, **kwargs)


class MembershipView(Viewer):
    template_name = "membership/membership.html"


class ScholorshipView(CreateView):
    template_name = "scholorship.html"
    model = Scholorship
    fields = "__all__"
    success_url = reverse_lazy("main:scholorship")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form['present_school'].field.widget.attrs.update({'rows': '4'})
        form.required_css_class = "required"

        return form

    def post(self, request):
        super(ScholorshipView, self).post(request)
        return render(request, "thank_you/scholorship.html")


class MembershipTeacherView(CustomCreateView):
    template_name = "membership/teacher.html"
    model = MembershipTeacher
    fields = "__all__"
    success_url = reverse_lazy("main:membership-teacher")
    thank_you_template = "thank_you/membership.html"
   
    def get_form(self):
        form = super().get_form()
        form.fields['dob'].widget = forms.SelectDateWidget(
            years=(range(1960, date.today().year-18)))
        return form


class Membership10thView(CreateView):
    template_name = "membership/10th.html"
    model = Membership10th
    fields = "__all__"
    success_url = reverse_lazy("main:membership-below-10th")

    def post(self, request):
        super(Membership10thView, self).post(request)
        return render(request, "thank_you/membership.html")


class Membership12thView(CreateView):
    template_name = "membership/12th.html"
    model = Membership12th
    fields = "__all__"
    success_url = reverse_lazy("main:membership-12th")

    def get_form(self):
        form = super().get_form()
        form.fields["assistance"].widget = forms.CheckboxSelectMultiple()
        form.fields["assistance"].queryset = AssistanceChoices.objects.all()
        return form

    def post(self, request):
        super(Membership12thView, self).post(request)
        return render(request, "thank_you/membership.html")


class FreeCounsellingView(CreateView):
    template_name = "free_counselling.html"
    model = FreeCounselling
    fields = "__all__"
    success_url = reverse_lazy("main:free_counselling")

    def post(self, request):
        super(FreeCounsellingView, self).post(request)
        return render(request, "thank_you/free_counselling.html")
