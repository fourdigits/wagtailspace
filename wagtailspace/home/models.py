from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.embeds.blocks import EmbedBlock
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


class OneColumnBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False, max_length=255)
    color = blocks.CharBlock(required=True, max_length=255)

    one_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
        ], icon='arrow-left', label='One column content')

    class Meta:
        template = 'home/one_column_block.html'
        icon = 'placeholder'
        label = 'One Column'


class ThreeColumnBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False, max_length=255)
    color = blocks.CharBlock(required=True, max_length=255)

    one_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
        ], icon='arrow-left', label='One column content')

    two_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
        ], icon='arrow-right', label='Two column content')

    three_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
        ], icon='arrow-right', label='Three column content')

    class Meta:
        template = 'home/three_column_block.html'
        icon = 'placeholder'
        label = 'Three Columns'


class TwoColumnBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=False, max_length=255)
    color = blocks.CharBlock(required=True, max_length=255)

    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('embedded_video', EmbedBlock()),
        ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('button', blocks.PageChooserBlock(classname="btn")),
            ('embedded_video', EmbedBlock()),
        ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'home/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class WhoIsThere(blocks.StructBlock):

    title = blocks.CharBlock(required=False, max_length=255)
    color = blocks.CharBlock(required=True, max_length=255)


    attendees = blocks.StreamBlock(
        [
            (
                'attendee', blocks.StructBlock(
                    [
                        ('name', blocks.CharBlock()),
                        ('nickname', blocks.CharBlock()),
                        ('company', blocks.CharBlock()),
                        ('dates', blocks.CharBlock()),
                        ('sure', blocks.CharBlock()),
                        ('remote', blocks.CharBlock()),
                        ('tshirt', blocks.ChoiceBlock(choices=[
                            ('xxs', 'xxs'),
                            ('xs', 'xs'),
                            ('s', 's'),
                            ('m', 'm'),
                            ('l', 'l'),
                            ('xl', 'xl'),
                            ('xxl', 'xxl')])),
                        ('food', blocks.ChoiceBlock(choices=[('normal', 'normal'),
                                                             ('vegie', 'vegie'),
                                                             ('other', 'other')])),
                        ('email', blocks.CharBlock(required=False)),
                        ('comment', blocks.CharBlock(required=False))
                    ],
                    template='home/blocks/attendee_content.html'
                )
            ),
        ],
        icon='cogs',
    )

    class Meta:
        template = 'home/who_column_block.html'
        icon = 'placeholder'
        label = 'WHOS THERE'


class HomePage(Page):
    subtitle = models.CharField(blank=True, max_length=255)

    intro_intro = models.TextField(blank=True)
    intro_content = RichTextField(blank=True)

    talks_sprint_title = models.CharField(blank=True, max_length=255)
    talks_content = RichTextField(blank=True)
    sprint_content = RichTextField(blank=True)

    schedule_title = models.CharField(blank=True, max_length=255)
    schedule_content = RichTextField(blank=True)

    location_facilities_title = models.CharField(blank=True, max_length=255)
    location_content = RichTextField(blank=True)
    facilities_content = RichTextField(blank=True)

    travel_hotels_title = models.CharField(blank=True, max_length=255)
    hotels_content = RichTextField(blank=True)
    travel_content = RichTextField(blank=True)

    signup_title = models.CharField(blank=True, max_length=255)
    signup_content = RichTextField(blank=True)
    signup_button_title = models.CharField(blank=True, max_length=100)

    attendees_title = models.CharField(blank=True, max_length=255)
    attendees_content = RichTextField(blank=True)

    sponsors_title = models.CharField(blank=True, max_length=255)
    sponsors_content = RichTextField(blank=True)

    house_rules_title = models.CharField(blank=True, max_length=255)
    house_rules_content = RichTextField(blank=True)

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('subtitle', classname="full title"),
        MultiFieldPanel(
            [
                FieldPanel('intro_intro', classname="full"),
                FieldPanel('intro_content', classname="full"),
            ]
        ),
        MultiFieldPanel(
            [
                FieldPanel('talks_sprint_title'),
                FieldPanel('talks_content'),
                FieldPanel('sprint_content'),
            ],
            heading='Talks & Sprint'
        ),
        MultiFieldPanel(
            [
                FieldPanel('schedule_title'),
                FieldPanel('schedule_content'),
            ],
            heading='Schedule'
        ),
        MultiFieldPanel(
            [
                FieldPanel('location_facilities_title'),
                FieldPanel('location_content'),
                FieldPanel('facilities_content'),
            ],
            heading='Location & Facilities'
        ),
        MultiFieldPanel(
            [
                FieldPanel('travel_hotels_title'),
                FieldPanel('hotels_content'),
                FieldPanel('travel_content'),
            ],
            heading='Travel & Hotels'
        ),
        MultiFieldPanel(
            [
                FieldPanel('signup_title'),
                FieldPanel('signup_content'),
                FieldPanel('signup_button_title'),
            ],
            heading='Signup'
        ),
        MultiFieldPanel(
            [
                FieldPanel('attendees_title'),
                FieldPanel('attendees_content'),
            ],
            heading='Attendees'
        ),
        MultiFieldPanel(
            [
                FieldPanel('sponsors_title'),
                FieldPanel('sponsors_content'),
            ],
            heading='Sponsors'
        ),
        MultiFieldPanel(
            [
                FieldPanel('house_rules_title'),
                FieldPanel('house_rules_content'),
            ],
            heading='House rules'
        ),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['attendees'] = Registration.objects.all()
        context['dates'] = EventDate.objects.all()
        return context


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):

    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('main_image'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


SHIRT_SIZES = (
    ('XXS', 'XXS'),
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('noshirt', "I don't want a shirt"),
)


class EventDate(models.Model):
    date = models.DateField(blank=False, unique=True, max_length=100)

    def __unicode__(self):
        return self.date.strftime('%A %d %B %Y')

    def __str__(self):
        return self.date.strftime('%A %d %B %Y')

    class Meta:
        ordering = ('date',)


class DaySchedule(models.Model):
    date = models.ForeignKey(
        EventDate,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='timeslots'
    )
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    description = models.CharField(max_length=1000)

    def representation(self):
        date = self.date.date.strftime('%A %d %B %Y')
        start = self.start_time.strftime('%H:%M')
        end = ''
        if self.end_time:
            end = ' - ' + self.end_time.strftime('%H:%M')
        return date + ' ' + start + end

    def __unicode__(self):
        return self.representation()

    def __str__(self):
        return self.representation()

    class Meta:
        ordering = ('date', 'start_time', )


class ExperienceOption(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=100)
    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('order',)


class Registration(models.Model):
    full_name = models.CharField('Name', max_length=255, blank=False)
    email = models.EmailField('Email address', blank=False)
    github_nickname = models.CharField('Github nickname', blank=False, max_length=255)
    company = models.CharField('Company', max_length=255)
    dates = models.ManyToManyField('EventDate')
    food_allergies = models.CharField('Food allergies', max_length=255, blank=True)
    roles = models.ManyToManyField('ExperienceOption')
    shirt_size = models.CharField('Shirt size', choices=SHIRT_SIZES, max_length=255)
    give_a_talk = models.BooleanField('I would like to give a talk on Friday', default=False)
    talk_title = models.CharField('Talk subject', max_length=1000, blank=True)
    comments = models.TextField('Comments', blank=True)
