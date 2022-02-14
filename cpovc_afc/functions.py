from django.shortcuts import get_object_or_404
from cpovc_main.functions import convert_date
from .models import AFCMain, AFCForms, AFCEvents
from cpovc_main.models import SetupGeography
from cpovc_ovc.models import OVCEducation
from cpovc_main.functions import get_dict


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
        # Schoool details in some forms
        ecare = get_alt_care(request, case_id)
        if form_id == '1A':
            school_level = request.POST.get('school_level')
            # Save School details
            if school_level and school_level != 'SLNS':
                school_class = request.POST.get('school_class')
                school_id = request.POST.get('school')
                admin_type = request.POST.get('admission_type')
                obj, created = OVCEducation.objects.update_or_create(
                    person_id=person_id, is_void=False,
                    defaults={'school_id': school_id,
                              'school_level': school_level,
                              'school_class': school_class,
                              'admission_type': admin_type, 'is_void': False},
                )
            # Update main table
            if ecare:
                ecare.school_level = school_level
                ecare.save(update_fields=["school_level"])
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


def get_area(area_id):
    """Get area name from id."""
    try:
        area = SetupGeography.objects.get(area_id=area_id)
    except Exception:
        return 'N/A'
    else:
        return area.area_name


def get_education(person_id):
    """Get area name from id."""
    try:
        ed = OVCEducation.objects.get(person_id=person_id, is_void=False)
    except Exception:
        return None
    else:
        return ed


def get_class_levels():
    """Method to get all class levels."""
    try:
        # Class levels
        vals = get_dict(field_name=['class_level_id'])
        levels = {}
        levels["SLNS"] = []
        levels["SLEC"] = ["BABY,Baby Class", "MIDC,Middle Class",
                          "PREU,Pre-Unit"]
        levels["SLPR"] = ["CLS1,Class 1", "CLS2,Class 2", "CLS3,Class 3",
                          "CLS4,Class 4", "CLS5,Class 5", "CLS6,Class 6",
                          "CLS7,Class 7", "CLS8,Class 8"]
        levels["SLSE"] = ["FOM1,Form 1", "FOM2,Form 2", "FOM3,Form 3",
                          "FOM4,Form 4", "FOM5,Form 5", "FOM6,Form 6"]
        levels["SLUN"] = ["YER1,Year 1", "YER2,Year 2", "YER3,Year 3",
                          "YER4,Year 4", "YER5,Year 5", "YER6,Year 6"]
        levels["SLTV"] = ["TVC1,Year 1", "TVC2,Year 2", "TVC3,Year 3",
                          "TVC4,Year 4", "TVC5,Year 5"]
        for level in levels:
            for lvl in levels[level]:
                c_lvl, c_nm = lvl.split(",")
                new_cnm = vals[c_lvl] if c_lvl in vals else c_nm
                n_lvl = "%s,%s" % (c_lvl, new_cnm)
                # print(lvl, n_lvl)
    except Exception as e:
        print('Error getting class levels - %s' % (str(e)))
        return {}
    else:
        return levels
