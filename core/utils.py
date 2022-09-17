# this file consists of custom made class and functions
from django.conf import settings
from django.views.generic import View, CreateView
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string


class Viewer(View):
    form_class = object
    template_name = None
    context = dict()

    def __init__(self, **kwargs) -> None:
        self.context['form'] = self.form_class()
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.get_template_name(), self.get_context())

    def post(self, request):
        self.form = request.POST
        self.form_valid()
        return render(request, self.get_template_name(), self.get_context())

    def form_valid(self):
        return render(self.request, self.get_template_name(), self.get_context())

    def get_context(self):
        return self.context

    def get_template_name(self):
        return self.template_name


class CustomCreateView(CreateView):
    thank_you_template = None
    mail_template = None
    mail_field_name = "email"
    mail_subject = ""
    mail_context = dict()

    def send_email(self, form):
        message = render_to_string(self.mail_template, self.mail_context)
        to_email = form.cleaned_data[self.mail_field_name]
        email = send_mail(
            subject=self.mail_subject,
            message = message,
            html_message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email]
        )
        if email == 1:
            return True
        else:
            raise "Email not sent by server"
        
    def form_valid(self, form):

        if self.mail_template is not None:
            self.send_email(form)
        if self.thank_you_template is not None:
            self.template_name = self.thank_you_template
        return super().form_valid(form)

    def post(self, request, *args: str, **kwargs):
        super().post(request, *args, **kwargs)
        return render(request, self.thank_you_template)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.required_css_class = "required"
        return form
