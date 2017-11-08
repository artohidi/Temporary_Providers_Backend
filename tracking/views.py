from django.http import Http404
from django.shortcuts import render, HttpResponse
from .models import Provider, ConversationDetail, Interviewer, ProviderBasicInfo, Skill
from dal import autocomplete


def providerData(request):
    result = "F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16\n"
    for p in Provider.objects.all():
        items = [p.basic_info.first_name, p.basic_info.last_name, p.provider_father_first_name,
                 p.basic_info.national_code, p.shenasname_code, p.born_city_1,
                 p.born_city_2, p.born_date, p.gender, p.married, p.tell_phone_number, p.cell_phone_number,
                 p.academic_licence, p.credit_cart_number, p.bank_name, p.bank_account_number]
        current_result = ", ".join(map(str, items))
        result += "%s\n" % current_result
    response = HttpResponse(result)

    response['Content-Type'] = "text/csv"
    response['Content-Disposition'] = "attachment;filename=providers.csv"

    return response


def form_1(request, pid):
    provider = Provider.objects.filter(id=pid).first()
    if provider is None:
        raise Http404

    return render(request, 'tracking/f1.html', {'provider': provider})


def form_2(request, pid):
    provider = Provider.objects.filter(id=pid).first()
    if provider is None:
        raise Http404

    return render(request, 'tracking/f2.html', {'provider': provider})


def form_3(request, pid):
    print(Provider.objects.all())
    provider = Provider.objects.filter(id=pid).first()

    if provider is None:
        raise Http404

    return render(request, 'tracking/f3.html', {'provider': provider})


class InformationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return ProviderBasicInfo.objects.none()

        qs = ProviderBasicInfo.objects.all()

        if self.q:
            qs = qs.filter(first_name__icontains=self.q) or qs.filter(last_name__icontains=self.q) or qs.filter(
                cell_phone_number__icontains=self.q)
        return qs.order_by("first_name", )


class InterviewerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Interviewer.objects.none()

        qs = Interviewer.objects.all()

        if self.q:
            qs = qs.filter(interviewer__icontains=self.q)

        return qs


def input(request):
    return render(request, 'tracking/input.html')
