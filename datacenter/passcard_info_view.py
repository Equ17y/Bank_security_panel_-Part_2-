from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')

    this_passcard_visits = []
    for visit in visits:
        entered_at = localtime(visit.entered_at).strftime('%d-%B-%Y %H:%M')
        duration = visit.format_duration()
        is_strange = visit.is_visit_long(minutes=60)

        this_passcard_visits.append({
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
