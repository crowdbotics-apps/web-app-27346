from django.contrib import admin

from home.models import App, Plan, Subscription


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'framework', 'domain_name', 'user', 'created_at', 'updated_at')
    list_filter = ('type', 'framework',)
    search_fields = ('name', 'description', 'domain_name')
    list_max_show_all = 100
    readonly_fields = ('created_at', 'updated_at',)
    ordering = ('-id',)

    fieldsets = (
        ('APP METADATA', {
            'fields': (
                'name', 'description', 'type', 'framework', 'domain_name', 'screenshot', 'user'
            )
        }),
        ('APP TIMESTAMPS', {
            'fields': (
                'created_at', 'updated_at',
            )
        }),
    )


class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_max_show_all = 100
    readonly_fields = ('created_at', 'updated_at',)
    ordering = ('-id',)

    fieldsets = (
        ('PLAN METADATA', {
            'fields': (
                'name', 'description', 'price'
            )
        }),
        ('PLAN TIMESTAMPS', {
            'fields': (
                'created_at', 'updated_at',
            )
        }),
    )


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'app', 'plan', 'active', 'user', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_max_show_all = 100
    readonly_fields = ('user', 'created_at', 'updated_at',)
    ordering = ('-id',)

    fieldsets = (
        ('SUBSCRIPTION METADATA', {
            'fields': (
                'plan', 'app', 'user', 'active'
            )
        }),
        ('SUBSCRIPTION TIMESTAMPS', {
            'fields': (
                'created_at', 'updated_at',
            )
        }),
    )

    def delete(self, *args, **kwargs):
        self.active = False
        self.save()


admin.site.register(App, AppAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
