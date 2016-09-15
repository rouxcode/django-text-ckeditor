from __future__ import unicode_literals

from django.contrib import admin

from ..admin import DjangoLinkAdmin
from .models import Link


@admin.register(Link)
class LinkAdmin(DjangoLinkAdmin):
    pass
