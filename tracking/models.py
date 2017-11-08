from django.core.validators import RegexValidator
from django.db import models


class ProviderBasicInfo(models.Model):
    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = "اطلاعات پایه همکار"
        verbose_name_plural = "اطلاعات پایه همکار"

    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    cell_phone_number = models.CharField(verbose_name="شماره تلفن همراه برای اپ", max_length=11,
                                         validators=[
                                             RegexValidator(regex='^.{11}$', message='توجه: شماره تلفن ۱۱ رقمی است',
                                                            code='nomatch')])

    def __str__(self):
        return "{0}_{1}_{2}".format(self.first_name, self.last_name, self.cell_phone_number)


class Product(models.Model):
    class Meta:
        verbose_name = "سرویس های قابل ارائه"
        verbose_name_plural = "سرویس های قابل ارائه"

    product_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="سرویس", unique=True)

    def __str__(self):
        return "{0}".format(self.product_name)


class License(models.Model):
    expert = models.CharField(max_length=100, blank=True, null=False, default="", verbose_name="مهارت", unique=True)

    class Meta:
        ordering = ("expert",)
        verbose_name = "مدرک"
        verbose_name_plural = "مدرک"

    def __str__(self):
        return self.expert


class Skill(models.Model):
    class Meta:
        verbose_name = "مهارت"
        verbose_name_plural = "مهارت ها"

    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, related_name="provider_skill")
    product_list = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='سرویس', blank=True,
                                     null=False)
    expectize = models.CharField(max_length=100, verbose_name="مهارت", blank=True, null=False, choices=(
        ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('ضعیف', 'ضعیف')))
    license = models.ForeignKey(License, on_delete=models.CASCADE, related_name='skills', verbose_name="مدرک",
                                blank=True, null=False)
    work_experience = models.CharField(max_length=100, verbose_name="سابقه کار", blank=True, null=False)
    explanation = models.CharField(max_length=500, verbose_name="توضیحات", blank=True, null=False, default="ندارد")

    def __str__(self):
        return "{0}".format(self.product_list)


class Presenter(models.Model):
    class Meta:
        verbose_name = "معرف"
        verbose_name_plural = "معرف ها"

    provider = models.ForeignKey('Provider', on_delete=models.CASCADE, related_name="provider_presenter")
    presenterName = models.CharField(default="", max_length=50, verbose_name="نام و نام خانوادگی معرف", blank=True,
                                     null=False)
    presenterJob = models.CharField(default="", max_length=50, verbose_name="شغل معرف", blank=True, null=False)
    presenterAcademicLicence = models.CharField(default="", max_length=50, verbose_name="تحصیلات معرف", blank=True,
                                                null=False)
    presenterRelation = models.CharField(default="", max_length=50, verbose_name="نسبت آشنایی", blank=True, null=False)
    presenterTelephone = models.CharField(default="", max_length=50, verbose_name="شماره تماس معرف", blank=True,
                                          null=False)

    def __str__(self):
        return self.presenterName


def directory_path(instance, filename):
    filename = "%s.%s" % (instance, 'jpg')
    return 'ProvidersDate/{0}/{1}{2}'.format(instance, instance, filename)


class CheckDocument(models.Model):
    class Meta:
        verbose_name = "مدارک فردی"
        verbose_name_plural = "مدارک فردی"

    check1 = models.CharField(max_length=10, choices=(('دارد', 'دارد'), ('ندارد', 'ندارد')),
                              verbose_name="فرم ثبت نام")
    check2 = models.CharField(max_length=10, choices=(('دارد', 'دارد'), ('ندارد', 'ندارد')),
                              verbose_name="چک لیست مصاحبه")
    check3 = models.CharField(max_length=10, choices=(('دارد', 'دارد'), ('ندارد', 'ندارد')),
                              verbose_name="قرارداد امضا شده")
    check4 = models.CharField(max_length=10, choices=(('دارد', 'دارد'), ('ندارد', 'ندارد')),
                              verbose_name="کپی شناسنامه")
    check5 = models.CharField(max_length=10, choices=(('دارد', 'دارد'), ('ندارد', 'ندارد')),
                              verbose_name="کپی کارت ملی")
    check6 = models.CharField(max_length=10, choices=(('دارد', 'دارد'), ('ندارد', 'ندارد')),
                              verbose_name="سند اقامتگاه")
    check7 = models.CharField(max_length=10, choices=(('دارد', 'دارد'), ('ندارد', 'ندارد')),
                              verbose_name="گواهی سوء پیشینه")
    check8 = models.CharField(max_length=10, choices=(('دارد', 'دارد'), ('ندارد', 'ندارد')), verbose_name="تضمینات")

    detail = models.CharField(max_length=500, verbose_name="شرح همکاری", blank=True, null=False, default="")

    def __str__(self):
        return "{0}".format(self.check)


class Provider(models.Model):
    class Meta:
        verbose_name = "فرم ثبت نام (فرم شماره ۱)"
        verbose_name_plural = "فرم ثبت نام (فرم شماره ۱)"

    checkDocument = models.OneToOneField(CheckDocument, on_delete=models.CASCADE, verbose_name="مدارک",
                                         related_name="provider_check")
    basic_information = models.OneToOneField(ProviderBasicInfo, on_delete=models.CASCADE,
                                             verbose_name="اطلاعات پایه همکار جدید",
                                             related_name="provider_basic_information")
    onboarding_date = models.DateTimeField(verbose_name="تاریخ", blank=True, null=True)
    picture_0 = models.ImageField(verbose_name="تصویر همکار", blank=True, null=True, upload_to=directory_path)
    picture_11 = models.ImageField(verbose_name="تصویر روی کارت ملی", blank=True, null=True, upload_to=directory_path)
    picture_12 = models.ImageField(verbose_name="تصویر پشت کارت ملی", blank=True, null=True, upload_to=directory_path)
    picture_2 = models.ImageField(verbose_name="تصویر شناسنامه", blank=True, null=True, upload_to=directory_path)
    provider_father_name = models.CharField(max_length=100, verbose_name="نام پدر", blank=True, null=False,
                                            default="")
    national_code = models.CharField(max_length=10, verbose_name="کد ملی", default="", blank=True, null=False)
    shenasname_code = models.CharField(max_length=20, verbose_name="شماره شناسنامه", blank=True, null=False, default="")
    born_city_1 = models.CharField(max_length=100, verbose_name="محل تولد", blank=True, null=False, default="")
    born_city_2 = models.CharField(max_length=100, verbose_name="صادره از", blank=True, null=False, default="")
    born_date = models.CharField(max_length=10, default=" 1370/01/01", verbose_name="تاریخ تولد", blank=True,
                                 null=False)
    gender = models.CharField(max_length=10, choices=(('مرد', 'مرد'), ('زن', 'زن')), verbose_name="جنسیت", blank=True,
                              null=False, default="")
    married = models.CharField(max_length=10, choices=(('مجرد', 'مجرد'), ('متاهل', 'متاهل')), verbose_name="وضعیت تاهل",
                               blank=True, null=False, default="")
    tell_phone_number = models.CharField(max_length=20, verbose_name="شماره ثابت", blank=True, null=False, default="")
    cell_phone_number = models.CharField(max_length=20, verbose_name="تلفن همراه برای نرم افزار", blank=True,
                                         null=False, default="")
    academic_licence = models.CharField(max_length=50, verbose_name="مدرک تحصیلی", blank=True, null=False, default="")
    credit_cart_number = models.CharField(max_length=16, verbose_name="شماره کارت بانکی", blank=True, null=False,
                                          default="")
    bank_name = models.CharField(max_length=30, verbose_name="نام بانک", blank=True, null=False, default="")
    bank_account_number = models.CharField(max_length=30, verbose_name="شماره حساب بانکی", blank=True, null=False,
                                           default="")
    city = models.CharField(max_length=100, verbose_name="شهر", blank=True, null=False, default="")
    region = models.CharField(max_length=10, choices=(
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10'), ('11', '11'), ('12', '12'), ('3', '3'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'),
        ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22')),
                              verbose_name="منطقه شهری", blank=True, null=False, default="")
    address = models.CharField(max_length=100, verbose_name="آدرس", blank=True, null=False, default="")
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی", blank=True, null=False, default="")

    def __str__(self):
        return "{0}) {1}_{2}_{3}".format(self.id, self.basic_information.first_name, self.basic_information.last_name,
                                         self.basic_information.cell_phone_number)


class Interviewer(models.Model):
    interviewer = models.CharField(max_length=200, verbose_name="نام مصاحبه کننده", unique=True)

    class Meta:
        ordering = ("interviewer",)
        verbose_name = "مصاحبه کننده"
        verbose_name_plural = "مصاحبه کنندگان"

    def __str__(self):
        return self.interviewer


class ConversationDetail(models.Model):
    class Meta:
        verbose_name = "فرم مصاحبه (فرم شماره ۲)"
        verbose_name_plural = "فرم مصاحبه (فرم شماره ۲)"

    detail_1 = models.CharField(max_length=200, verbose_name="توضیح ۱", blank=True, null=False, default="")
    detail_2 = models.CharField(max_length=200, verbose_name="توضیح ۲", blank=True, null=False, default="")
    detail_3 = models.CharField(max_length=200, verbose_name="توضیح ۳", blank=True, null=False, default="")
    detail_4 = models.CharField(max_length=200, verbose_name="توضیح ۴", blank=True, null=False, default="")
    detail_5 = models.CharField(max_length=200, verbose_name="توضیح ۵", blank=True, null=False, default="")
    detail_6 = models.CharField(max_length=200, verbose_name="توضیح ۶", blank=True, null=False, default="")
    detail_7 = models.CharField(max_length=200, verbose_name="توضیح ۷", blank=True, null=False, default="")
    detail_8 = models.CharField(max_length=200, verbose_name="توضیح ۸", blank=True, null=False, default="")
    provider = models.OneToOneField(Provider, on_delete=models.CASCADE, verbose_name="همکار",
                                    related_name="provider_ConversationDetail")
    interviewer = models.OneToOneField(Interviewer, on_delete=models.CASCADE, verbose_name="مصاحبه کننده")
    documentNum = models.CharField(max_length=50, verbose_name="شماره پرونده")
    conversationDate = models.DateTimeField(verbose_name="تاریخ مصاحبه")
    conversationNum = models.CharField(max_length=50, verbose_name="شماره مصاحبه")
    rate_11 = models.IntegerField(verbose_name="لباس مناسب و تمیز",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_12 = models.IntegerField(verbose_name="توانایی جسمانی",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_13 = models.IntegerField(verbose_name="فقدان علایم اعتیاد",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_14 = models.IntegerField(verbose_name="فقدان خالکوبی و یقه باز",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_15 = models.IntegerField(verbose_name="چهره و ظاهر قابل اعتماد ( زخم و غیره )",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_21 = models.IntegerField(verbose_name="داشتن تلفن همراه",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_22 = models.IntegerField(verbose_name="آشنایی با تلفن هوشمند (دیتا، آپدیت و غیره)",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_23 = models.IntegerField(verbose_name="داشتن اکانت تلگرام",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_24 = models.IntegerField(verbose_name="میزان آشنایی با اسنپ و تپسی",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_25 = models.IntegerField(verbose_name="دریافت و درک درست از استادکار",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_31 = models.IntegerField(verbose_name="میزان تبحر در رشته فعالیت خود",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_32 = models.IntegerField(verbose_name="میزان آشنایی با علم روز کار",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_33 = models.IntegerField(verbose_name="میزان آشنایی با ابزار ها",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_34 = models.IntegerField(verbose_name="در اختیار داشتن ابزار های مورد نیاز",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_35 = models.IntegerField(verbose_name="اطلاعات فرد در خصوص سایر خدمات",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_41 = models.IntegerField(verbose_name="آرامش و اعتماد بنفس در صحبت",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_42 = models.IntegerField(verbose_name="توانایی متقاعد سازی",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_43 = models.IntegerField(verbose_name="خوب گوش دادن و صحبت به نوبت",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_44 = models.IntegerField(verbose_name="توجه و تجزیه و تحلیل صحبت  ها",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_45 = models.IntegerField(verbose_name="خوش رویی در هنگام مصاحبه",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_51 = models.IntegerField(verbose_name="نظافت ناخن",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_52 = models.IntegerField(verbose_name="بهداشت دهان و دندان",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_53 = models.IntegerField(verbose_name="بهداشت و نظافت چهره ( استحمام )",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_54 = models.IntegerField(verbose_name="مرتب و معقول و متعارف بودن مو و ریش",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_55 = models.IntegerField(verbose_name="فقدان بوی نامطبوع بدن",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_61 = models.IntegerField(verbose_name="نحوه سلام و احوال پرسی",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_62 = models.IntegerField(verbose_name="استفاده از افعال و القاب مناسب",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_63 = models.IntegerField(verbose_name="انتخاب سنجیده محتوای کلام",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_64 = models.IntegerField(verbose_name="میزان صداقت در پاسخگویی",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_65 = models.IntegerField(verbose_name="شفافیت در کلام و تعیین قیمت ( طفره نرفتن )",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_71 = models.IntegerField(verbose_name="استفاده از لباس و کفش کار",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_72 = models.IntegerField(verbose_name="میزان آشنایی با موارد ایمنی",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_73 = models.IntegerField(verbose_name="میزان آشنایی با بیمه مسئولیت مدنی",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_74 = models.IntegerField(verbose_name="میزان آشنایی یا قوانین صنفی",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_75 = models.IntegerField(verbose_name="داشتن مجوز های ضروری",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_81 = models.IntegerField(verbose_name="آرامش مقابل مخالفت و انتقاد پذیری",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_82 = models.IntegerField(verbose_name="عکس العمل معقول",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_83 = models.IntegerField(verbose_name="میزان انعطاف پذیری",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_84 = models.IntegerField(verbose_name="فقدان تکبر یا تحکم در کلام",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    rate_85 = models.IntegerField(verbose_name="اعتماد وخوش بینی به استادکار",
                                  choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))

    moreDetails = models.CharField(max_length=1000, verbose_name="توضیح کلی")

    def sum(self):
        s = self.rate_11 + self.rate_12 + self.rate_13 + self.rate_14 + self.rate_15 + \
            self.rate_21 + self.rate_22 + self.rate_23 + self.rate_24 + self.rate_25 + \
            self.rate_31 + self.rate_32 + self.rate_33 + self.rate_34 + self.rate_35 + \
            self.rate_41 + self.rate_42 + self.rate_43 + self.rate_44 + self.rate_45 + \
            self.rate_51 + self.rate_52 + self.rate_53 + self.rate_54 + self.rate_55 + \
            self.rate_61 + self.rate_62 + self.rate_63 + self.rate_64 + self.rate_65 + \
            self.rate_71 + self.rate_72 + self.rate_73 + self.rate_74 + self.rate_75 + \
            self.rate_81 + self.rate_82 + self.rate_83 + self.rate_84 + self.rate_85

        return "{0}".format(s)

    def sum_1(self):
        s = self.rate_11 + self.rate_12 + self.rate_13 + self.rate_14 + self.rate_15

        return "{0}".format(s)

    def sum_2(self):
        s = self.rate_21 + self.rate_22 + self.rate_23 + self.rate_24 + self.rate_25

        return "{0}".format(s)

    def sum_3(self):
        s = self.rate_31 + self.rate_32 + self.rate_33 + self.rate_34 + self.rate_35

        return "{0}".format(s)

    def sum_4(self):
        s = self.rate_41 + self.rate_42 + self.rate_43 + self.rate_44 + self.rate_45

        return "{0}".format(s)

    def sum_5(self):
        s = self.rate_51 + self.rate_52 + self.rate_53 + self.rate_54 + self.rate_55

        return "{0}".format(s)

    def sum_6(self):
        s = self.rate_61 + self.rate_62 + self.rate_63 + self.rate_64 + self.rate_65

        return "{0}".format(s)

    def sum_7(self):
        s = self.rate_71 + self.rate_72 + self.rate_73 + self.rate_74 + self.rate_75

        return "{0}".format(s)

    def sum_8(self):
        s = self.rate_81 + self.rate_82 + self.rate_83 + self.rate_84 + self.rate_85

        return "{0}".format(s)

    def __str__(self):
        return "{0}{1}".format(self.provider, self.interviewer)
