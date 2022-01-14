from django.shortcuts import get_object_or_404
from cpovc_main.functions import convert_date
from .models import AFCMain, AFCForms, AFCEvents


def handle_alt_care(request, action, params={}):
    """Method to handle Alt Care"""
    try:
        if action == 0:
            save_alt_care(request, params)
        else:
            # This is to handle edits / deletion
            case_id = params['case_id']
            case = get_object_or_404(AFCMain, case_id=case_id)
            if case:
                # Void this record and delete case_info data
                case.is_void = True
                case.save(update_fields=["is_void"])
    except Exception as e:
        print('Error saving AFC %s' % (str(e)))
    else:
        return True


def get_alt_care(request, case_id):
    """Method to get Alt Care case."""
    try:
        case = AFCMain.objects.get(case_id=case_id, is_void=False)
    except Exception:
        return False
    else:
        return case


def save_alt_care(request, params):
    """Method to save Main case data."""
    try:
        case_id = params['case_id']
        person_id = params['person_id']
        case_date = request.POST.get('case_date')
        care_type = request.POST.get('care_option')
        event_date = convert_date(case_date)
        obj, created = AFCMain.objects.update_or_create(
            case_id=case_id,
            defaults={'case_date': event_date, 'care_type': care_type,
                      'person_id': person_id, 'is_void': False},
        )
        # Save the activity, means and purpose
        # activity_list = request.POST.getlist('ctip_activity')
    except Exception as e:
        print('Error saving AFC %s' % (str(e)))
    else:
        return True


def save_altcare_form(request, form_id, ev_id=0):
    """Method to save forms."""
    try:
        response = True
        case_id = request.POST.get('case_id')
        care_id = request.POST.get('care_id')
        person_id = request.POST.get('person_id')
        event_date = request.POST.get('event_date')
        lid = get_last_form(request, form_id)
        print('Last ID', lid)
        obj, created = AFCEvents.objects.update_or_create(
            case_id=case_id, form_id=form_id, care_id=care_id,
            defaults={'event_date': convert_date(event_date),
                      'person_id': person_id})
        event_id = obj.pk
        save_form_data(request, form_id, event_id)
        pref = 'qf%s' % (form_id)
        extract_params(request, pref)
    except Exception as e:
        print('Error saving form - %s' % (str(e)))
        return False
    else:
        return response


def get_last_form(request, form_id):
    """Method to get the last form."""
    try:
        last_form = AFCEvents.objects.filter(
            form_id=form_id).latest('event_count').event_count
    except Exception as e:
        print('Error querying last form ID - %s' % (str(e)))
        return 0
    else:
        return last_form


def save_form_data(request, form_id, event_id):
    """Method to save Main forms data."""
    try:
        print('event id', event_id)
        form_pref = 'qf%s' % (form_id)
        all_itms = extract_params(request, form_pref)
        for itms in all_itms:
            for itm in all_itms[itms]:
                print('itm', itms, itm)
                itdm = 'QTXT' if itms.endswith('_txt') else itm
                itdl = itm if itms.endswith('_txt') else None
                print('itm after', itms, itm, itdl)
                obj, created = AFCForms.objects.update_or_create(
                    event_id=event_id, question_id=itms,
                    item_value=itdm,
                    defaults={'item_value': itdm, 'item_detail': itdl},
                )
    except Exception as e:
        print('Error saving TIP %s' % (str(e)))
    else:
        return True


def extract_params(request, pref):
    """Method to extract charges items."""
    try:
        params, itms = {}, []
        for itm in request.POST:
            if itm.startswith(pref):
                itms.append(itm.replace(pref, ''))
        # print('items', itms)

        for dt in itms:
            itm_id = '%s%s' % (pref, dt)
            itm_value = request.POST.getlist(itm_id)
            if itm_value[0]:
                params[itm_id] = itm_value
        print(params)
    except Exception as e:
        print('Error extracting params - %s' % (e))
        return []
    else:
        return params
