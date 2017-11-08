from dal import autocomplete
from django.contrib import admin
from .models import Provider, Skill, Presenter, ConversationDetail, Interviewer, Product, License, ProviderBasicInfo, \
    CheckDocument
from django import forms


class InterviewerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class PresentInline(admin.StackedInline):
    model = Presenter
    extra = 1


class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1


class ProviderAdmin(admin.ModelAdmin):
    inlines = [SkillInline, PresentInline]
    fieldsets = (
        ("اطلاعات پایه همکار", {
            'fields': ('basic_information', 'onboarding_date',)
        }),
        ("تصاویر", {
            'fields': ('picture_0', 'picture_11', 'picture_12', 'picture_2',)
        }),
        ("مدارک", {
            'fields': ('checkDocument',)
        }),
        ("اطلاعات تکمیلی", {
            'fields': (
                'provider_father_name', 'national_code', 'shenasname_code', 'born_city_1', 'born_city_2', 'born_date',
                'gender',
                'married', 'tell_phone_number', 'cell_phone_number', 'academic_licence')
        }),
        ("اطلاعات بانکی", {
            'fields': ('credit_cart_number', 'bank_name', 'bank_account_number')
        }),
        ("آدرس", {
            'fields': ('city', 'region', 'address', 'postal_code')
        }),
    )

    def show_url_1(self, obj):
        return '<a href="http://127.0.0.1:8000/tracking/f1/%s/">دریافت</a>' % (obj.pk)

    show_url_1.allow_tags = True
    show_url_1.short_description = "فرم شماره ۱"
    list_display = ["basic_information", "show_url_1"]

    def photo_0(self, obj):
        return "<img src='%s' width=100px height=100px>" % obj.picture_0.url

    photo_0.allow_tags = True

    def photo_1(self, obj):
        return "<img src='%s' height=100px width=100px>" % obj.picture_11.url

    photo_1.allow_tags = True

    def photo_2(self, obj):
        return "<img src='%s' height=100px width=100px>" % obj.picture_12.url

    photo_2.allow_tags = True

    def photo_3(self, obj):
        return "<img src='%s' height=100px width=100px>" % obj.picture_2.url

    photo_3.allow_tags = True
    readonly_fields = ('id', 'photo_0', 'photo_1', 'photo_2', 'photo_3')


class InterviewerDetailForm(forms.ModelForm):
    interviewer = forms.ModelChoiceField(label="نام مصاحبه کننده", queryset=Interviewer.objects.all(),
                                         widget=autocomplete.ModelSelect2(url='/tracking/interview-autocomplete'))

    class Meta:
        model = ConversationDetail
        fields = ('__all__')


class ConversationDetailAdmin(admin.ModelAdmin):
    form = InterviewerDetailForm

    def show_url_2(self, obj):
        return '<a href="http://127.0.0.1:8000/tracking/f2/%s/">دریافت</a>' % (obj.pk)

    show_url_2.allow_tags = True
    show_url_2.short_description = "فرم شماره ۲"

    def show_url_3(self, obj):
        return '<a href="http://127.0.0.1:8000/tracking/f3/%s/">دریافت</a>' % (obj.pk)

    show_url_3.allow_tags = True
    show_url_3.short_description = "فرم شماره ۳"

    list_display = ["provider", "interviewer", "show_url_2", "show_url_3"]
    fieldsets = (
        ("مشخصات اولیه", {
            'fields': (
                'conversationDate', 'documentNum', 'conversationNum', 'interviewer', 'provider')
        }),
        ("ظاهر", {
            'fields': ('rate_11', 'rate_12', 'rate_13', 'rate_14', 'rate_15', 'detail_1')
        }),
        ("آشنایی با تکنولوژی", {
            'fields': ('rate_21', 'rate_22', 'rate_23', 'rate_24', 'rate_25', 'detail_2')
        }),
        ("موارد فنی", {
            'fields': ('rate_31', 'rate_32', 'rate_33', 'rate_34', 'rate_35', 'detail_3')
        }),
        ("هوش اجتماعی", {
            'fields': ('rate_41', 'rate_42', 'rate_43', 'rate_44', 'rate_45', 'detail_4')
        }),
        ("بهداشت", {
            'fields': ('rate_51', 'rate_52', 'rate_53', 'rate_54', 'rate_55', 'detail_5')
        }),
        ("نحوه برخورد", {
            'fields': ('rate_61', 'rate_62', 'rate_63', 'rate_64', 'rate_65', 'detail_6')
        }),
        ("ایمنی در کار", {
            'fields': ('rate_71', 'rate_72', 'rate_73', 'rate_74', 'rate_75', 'detail_7')
        }),
        ("ثبات عاطفی", {
            'fields': ('rate_81', 'rate_82', 'rate_83', 'rate_84', 'rate_85', 'detail_8')
        }),
        ("توضیح کلی", {
            'fields': ('moreDetails',)
        }),

    )


admin.site.register(Provider, ProviderAdmin)
admin.site.register(ConversationDetail, ConversationDetailAdmin)
admin.site.register(Interviewer, InterviewerAdmin)
admin.site.register(Product)
admin.site.register(License)
admin.site.register(ProviderBasicInfo)
admin.site.register(CheckDocument)
