from django.db import models

CLASS = (
        ("11th", "11th"), ("12th", "12th"))

STREAM = (
        ("Science", "Science"), ("Commerce", "Commerce"), ("Arts", "Arts"))

class FreeCounselling(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    contact = models.CharField(max_length=10, verbose_name="Contact Number")
    Class = models.CharField(max_length=100, choices=CLASS)
    stream = models.CharField(max_length=10, choices=STREAM)
    combination = models.CharField(max_length=1000)
    career = models.CharField(
        max_length=1000, verbose_name="Career Choice After 12th")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Scholorship(models.Model):
    name = models.CharField(
        max_length=1000, verbose_name="Name of the Student")
    contact = models.CharField(max_length=10, verbose_name="Contact / Whatsapp Number")
    email = models.EmailField(verbose_name="Email Id")
    stream = models.CharField(max_length=10, choices=STREAM)
    combination = models.CharField(max_length=1000)

    religion = models.CharField(max_length=100, null=True, blank=True)
    caste = models.CharField(max_length=100, null=True, blank=True)
    present_school = models.TextField(
        verbose_name="Name of School/ College studied in 12th:")
    marks = models.CharField(
        max_length=100, verbose_name="% of Marks Obtained in PUC")
    course = models.CharField(
        max_length=100, verbose_name="Name of Course joined after 12th:")
    college = models.CharField(
        max_length=100, verbose_name="Name of the college joined after 12th:")
    fees = models.CharField(
        max_length=1000, verbose_name="Total estimated Fees:")
    income = models.CharField(
        max_length=1000, verbose_name="Annual Family Income:")
    loan = models.CharField(
        max_length=1000, verbose_name="Availing Education Loan:", choices=(("Yes", "Yes"), ("No", "No")))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Membership10th(models.Model):
    
    name = models.CharField(
        max_length=1000, verbose_name="Name of the Student")
    Class = models.CharField(max_length=1000, verbose_name='Class studying')

    contact = models.CharField(max_length=10, verbose_name="Contact Number")
    email = models.EmailField(verbose_name="Email Id")
    fname = models.CharField(max_length=1000, verbose_name='Name of Father')
    focc = models.CharField(
        max_length=1000, verbose_name="Father's Occupation", null=True, blank=True)
    fcon = models.CharField(
        max_length=1000, verbose_name="Father's Contact Number")
    fmail = models.CharField(max_length=1000, verbose_name="Father's Email Id", null=True, blank=True)
    mname = models.CharField(max_length=1000, verbose_name='Name of Mother', null=True, blank=True)
    mocc = models.CharField(
        max_length=1000, verbose_name="Mother's Occupation", null=True, blank=True)
    mcon = models.CharField(
        max_length=1000, verbose_name="Mother's Contact Number", null=True, blank=True)
    mmail = models.CharField(max_length=1000, verbose_name="Mother's Email Id", null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    caste = models.CharField(max_length=100, null=True, blank=True)
    school = models.CharField(
        max_length=1000, verbose_name='Name of the school studying')

    city = models.CharField(
        max_length=1000, verbose_name='City / Town / Place')
    district = models.CharField(max_length=1000, verbose_name='District')
    state = models.CharField(max_length=1000, verbose_name='State')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        self.name


class AssistanceChoices(models.Model):
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.desc


class Membership12th(models.Model):
    name = models.CharField(
        max_length=1000, verbose_name="Name of the Student")
    wno = models.CharField(
        max_length=1000, verbose_name="Student's Whatsapp Number")
    email = models.EmailField(verbose_name="Email Id")
    fname = models.CharField(max_length=1000, verbose_name='Name of Father')
    focc = models.CharField(
        max_length=1000, verbose_name="Father's Occupation", null=True, blank=True)
    fcon = models.CharField(
        max_length=1000, verbose_name="Father's Contact Number")
    fmail = models.CharField(max_length=1000, verbose_name="Father's Email Id", null=True, blank=True)

    mname = models.CharField(max_length=1000, verbose_name='Name of Mother', null=True, blank=True)
    mocc = models.CharField(
        max_length=1000, verbose_name="Mother's Occupation", null=True, blank=True)
    mcon = models.CharField(
        max_length=1000, verbose_name="Mother's Contact Number", null=True, blank=True)
    mmail = models.CharField(max_length=1000, verbose_name="Mother's Email Id", null=True, blank=True)
    Class = models.CharField(max_length=100, choices=CLASS)
    stream = models.CharField(max_length=10, choices=STREAM)
    combination = models.CharField(max_length=1000)
    college = models.CharField(max_length=1000, verbose_name='College Name')
    city = models.CharField(
        max_length=1000, verbose_name='City / Town / Place')

    religion = models.CharField(max_length=100, null=True, blank=True)
    caste = models.CharField(max_length=100, null=True, blank=True)

    career = models.CharField(
        max_length=1000, verbose_name="Career Choice After 12th")
    assistance = models.ManyToManyField(
        AssistanceChoices, verbose_name="What assistance you looking for:", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MembershipTeacher(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Name')
    dob = models.DateField(verbose_name="Date of birth:")
    contact = models.CharField(max_length=1000, verbose_name='Contact Number')
    email = models.EmailField()
    job = models.CharField(max_length=1000, verbose_name='Job Title:')
    subject = models.CharField(
        max_length=1000, verbose_name='Subject Specialization')
    school = models.CharField(
        max_length=1000, verbose_name='School / College Working For: ')
    city = models.CharField(
        max_length=1000, verbose_name='City / Town / Place')
    district = models.CharField(max_length=1000, verbose_name='District')
    state = models.CharField(max_length=1000, verbose_name='State')
    exp = models.CharField(
        max_length=1000, verbose_name='Working experience in years:')
    qualification = models.CharField(
        max_length=1000, verbose_name='Highest Education Qualification :')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Notice(models.Model):
    notice = models.TextField()
    
    def __str__(self) -> str:
        return self.notice


class Contact(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name