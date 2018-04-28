from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from wagtailspace.home.forms import SignupForm
from wagtailspace.home.models import HomePage, EventDate
from django.core.mail import send_mail

path_to_icons = 'images/favicons'


def get_attendance(attendee, theday):
    if attendee.get('dates', '') == 'All dates':
        return True
    return theday in attendee.get('dates', '').lower()


def attendees(request):
    if not request.user.has_perm('website.add_homepage'):
        raise PermissionDenied
    homepage = HomePage.objects.first()
    attendees = []
    sizes = {
        'xxs': 0,
        'xs': 0,
        's': 0,
        'm': 0,
        'l': 0,
        'xl': 0,
        'xxl': 0,
    }
    food = {
        'normal': 0,
        'vegie': 0,
        'other': 0,
    }
    days = {
        'tuesday': 0,
        'wednesday': 0,
        'thursday': 0,
        'friday': 0
    }
    emails = []
    for block in filter(lambda x: x.block_type == 'who_there', homepage.page_content):
        _attendees = block.value['attendees']
        for att in _attendees:
            attendee = att.value
            for day in ['tuesday', 'wednesday', 'thursday', 'friday']:
                thisDay = get_attendance(attendee, day)
                attendee[day] = thisDay
                if thisDay and attendee.get('remote', 'no') == 'no':
                    days[day] += 1

            attendees.append(attendee)
            if attendee.get('tshirt', None):
                sizes[attendee['tshirt']] += 1
            if attendee.get('food', None):
                food[attendee['food']] += 1
            if attendee.get('email', None):
                emails.append(attendee['email'])

    return render(request, 'home/attendees.html', {
        'attendees': attendees,
        'sizes': sizes,
        'food': food,
        'days': days,
        'emails': ', '.join(emails),
    })


def send_mail_to_four_digits(registration):
    talk = "Yes" if registration.give_a_talk else "No"
    dates = ", ".join([str(x) for x in registration.dates.all()])
    roles = ", ".join([str(x) for x in registration.roles.all()])
    message = u"""
Someone has registered for Wagtail Space.
Their info:

Name: {full_name}
Email: {email}
Company: {company}
Github name: {github_nickname}
Dates: {dates}
Food allergies: {food_allergies}
Roles: {roles}
Would like to give a talk: {talk}
Talk title: {talk_title}
Comments:
{comments}

Kind regards,
Wagtail Space Registration System
""".format(
        full_name=registration.full_name,
        email=registration.email,
        github_nickname=registration.github_nickname,
        company=registration.company,
        dates=dates,
        food_allergies=registration.food_allergies,
        roles=roles,
        shirt_size=registration.shirt_size,
        talk=talk,
        talk_title=registration.talk_title,
        comments=registration.comments
    )
    send_mail(
        'New Wagtail Space Registration',
        message,
        'Wagtail Space <no-reply@wagtail.space>',
        ['support@fourdigits.nl'],
        fail_silently=False,
    )


def signup(request):
    initial_dates = EventDate.objects.exclude(date__icontains='remotely').values_list('id', flat=True)
    form = SignupForm(initial={'dates': initial_dates})
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            registration = form.save()
            context['registration'] = registration
            context['saved'] = True
            send_mail_to_four_digits(registration)
    return render(request, 'home/signup_form.html', context)
