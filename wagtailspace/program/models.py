from __future__ import unicode_literals
from wagtail.core.models import Page

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel


class ProgramEntryBlock(blocks.StructBlock):
    timeslot = blocks.CharBlock(required=True)
    activity = blocks.TextBlock(required=True)
    notes = blocks.TextBlock(required=False)

    class Meta:
        template = 'program/blocks/program_entry_block.html'
        icon = 'time'
        label = 'Entry'


class DayBlock(blocks.StructBlock):
    date = blocks.DateBlock(required=True)
    program = blocks.ListBlock(ProgramEntryBlock())

    class Meta:
        template = 'program/blocks/day_block.html'
        icon = 'date'
        label = 'Day'


class ProgramPage(Page):

    program = StreamField([
        ('day', DayBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('program'),
    ]
