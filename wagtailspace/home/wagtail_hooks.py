from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from .models import DaySchedule, EventDate, ExperienceOption, Registration


class EventDateModelAdmin(ModelAdmin):
    model = EventDate
    menu_label = 'Event dates'
    menu_icon = 'date'
    menu_order = 600
    inspect_view_enabled = True


class DayScheduleModelAdmin(ModelAdmin):
    model = DaySchedule
    menu_label = 'Schedule'
    menu_icon = 'date'
    menu_order = 700
    inspect_view_enabled = True
    list_display = ('date', 'start_time', 'end_time', 'description')
    list_filter = ('date',)


class ExperienceOptionModelAdmin(ModelAdmin):
    model = ExperienceOption
    menu_label = 'Experience options'
    menu_icon = 'folder'
    menu_order = 800


class RegistrationModelAdmin(ModelAdmin):
    model = Registration
    menu_label = 'Registrations'
    menu_icon = 'user'
    menu_order = 850
    list_display = (
        'full_name',
        'email',
        # 'github_nickname',
        # 'company',
        # 'dates',
        # 'food_allergies',
        # 'roles',
        'shirt_size',
        'give_a_talk',
        'talk_title',
        # 'comments',
    )

class WagtailSpaceModelAdmin(ModelAdminGroup):
    menu_label = 'Wagtail Space'
    menu_icon = 'folder-open-inverse'
    menu_order = 600
    items = (
        EventDateModelAdmin,
        DayScheduleModelAdmin,
        ExperienceOptionModelAdmin,
        RegistrationModelAdmin,
    )

modeladmin_register(WagtailSpaceModelAdmin)
