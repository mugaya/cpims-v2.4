from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from cpovc_forms.forms import OVCSearchForm
from cpovc_forms.functions import get_person_ids
from .models import AFCMain, AFCEvents, AFCForms
from .forms import AltCareForm, AFCFormA
from cpovc_registry.models import (
    RegPerson, RegPersonsSiblings, RegPersonsExternalIds, RegPersonsGeo)
from cpovc_forms.models import OVCCaseRecord, OVCCaseCategory
from cpovc_main.functions import get_dict
from .functions import handle_alt_care, save_altcare_form
from .settings import FMS, CTS


@login_required
def alt_care_home(request):
    '''
    Some default page for forms home page
    '''
    try:
        form = OVCSearchForm(data=request.GET)
        # form = SearchForm(data=request.POST)
        # person_type = 'TBVC'
        afc_ids, case_ids = {}, {}
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)
        cases = RegPerson.objects.filter(is_void=False, id__in=pids)
        # Get case record sheet details
        crss = OVCCaseRecord.objects.filter(is_void=False, person_id__in=pids)
        for crs in crss:
            case_ids[crs.person_id] = {'clv': 1, 'cid': crs.case_id}
        # Check if there is a filled AFC Form
        afcs = AFCMain.objects.filter(is_void=False, person_id__in=pids)
        for afc in afcs:
            afc_ids[afc.person_id] = {'cid': afc.case_id,
                                      'clv': 2, 'cdt': afc.case_date}
        for case in cases:
            pid = case.id
            cid = afc_ids[pid]['cid'] if pid in afc_ids else 'N/A'
            cdt = afc_ids[pid]['cdt'] if pid in afc_ids else 'N/A'
            clvf = case_ids[pid]['clv'] if pid in case_ids else 0
            crs_id = case_ids[pid]['cid'] if pid in case_ids else None
            clv = afc_ids[pid]['clv'] if pid in afc_ids else clvf
            setattr(case, 'case_t', str(cid))
            setattr(case, 'case_date', cdt)
            setattr(case, 'case_level', clv)
            setattr(case, 'case_id', crs_id)
        return render(request, 'afc/home.html',
                      {'status': 200, 'cases': cases, 'form': form})
    except Exception as e:
        raise e


@login_required
def new_alternative_care(request, case_id):
    '''
    New Alternative Care main page
    '''
    try:
        form = AltCareForm(initial={'person_type': 'TBVC'})
        check_fields = ['sex_id', 'case_category_id']
        vals = get_dict(field_name=check_fields)
        # Case Categories
        case = OVCCaseRecord.objects.get(case_id=case_id)
        categories = OVCCaseCategory.objects.filter(case_id_id=case_id)

        if request.method == 'POST':
            afc_params = {}
            person_id = case.person_id
            afc_params['case_id'] = case_id
            afc_params['person_id'] = person_id
            handle_alt_care(request, 0, afc_params)
            url = reverse(view_alternative_care, kwargs={'case_id': case_id})
            msg = 'Alternative Care details saved successfully'
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect(url)
        return render(request, 'afc/new_alternative_care.html',
                      {'status': 200, 'case_id': case_id, 'vals': vals,
                       'categories': categories, 'case': case,
                       'form': form})
    except Exception as e:
        raise e


@login_required
def view_alternative_care(request, case_id):
    '''
    View Alternative Care main page
    '''
    try:
        case = AFCMain.objects.get(is_void=False, case_id=case_id)
        cid = str(case.care_type)[2:]
        cname = CTS[cid] if cid in CTS else 'Adoption'
        check_fields = ['sex_id', 'case_category_id',
                        'alternative_family_care_type_id']
        vals = get_dict(field_name=check_fields)
        # Events
        events = (AFCEvents.objects
                  .filter(case_id=case_id)
                  .values('form_id')
                  .annotate(dcount=Count('form_id'))
                  .order_by()
                  )
        forms = {}
        for event in events:
            forms[str(event['form_id'])] = event['dcount']
        return render(request, 'afc/view_alternative_care.html',
                      {'status': 200, 'case': case, 'vals': vals,
                       'cid': cid, 'care_name': cname, 'events': forms})
    except Exception as e:
        raise e


@login_required
def edit_alternative_care(request, case_id):
    '''
    Edit Alternative Care main page
    '''
    try:
        case = AFCMain.objects.get(is_void=False, case_id=case_id)
        cid = str(case.care_type)[2:]
        if request.method == 'POST':
            afc_params = {}
            person_id = case.person_id
            afc_params['case_id'] = case_id
            afc_params['person_id'] = person_id
            handle_alt_care(request, 0, afc_params)
            url = reverse(view_alternative_care, kwargs={'case_id': case_id})
            msg = 'Alternative Care details updated successfully'
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect(url)
        initial_info = {}
        cdate = case.case_date
        case_date = cdate.strftime('%d-%b-%Y')
        initial_info['care_option'] = case.care_type
        initial_info['case_date'] = case_date
        form = AltCareForm(initial=initial_info)
        cname = CTS[cid] if cid in CTS else 'Adoption'
        check_fields = ['sex_id', 'case_category_id',
                        'alternative_family_care_type_id']
        vals = get_dict(field_name=check_fields)
        categories = OVCCaseCategory.objects.filter(case_id_id=case_id)
        return render(request, 'afc/edit_alternative_care.html',
                      {'status': 200, 'case': case, 'vals': vals,
                       'cid': cid, 'care_name': cname,
                       'form': form, 'categories': categories})
    except Exception as e:
        raise e


@login_required
def alt_care_form(request, cid, form_id, case_id, ev_id=0):
    '''
    Some default page for CTiP forms home page
    '''
    try:
        check_fields = ['sex_id', 'case_category_id', 'religion_type_id',
                        'alternative_family_care_type_id']
        vals = get_dict(field_name=check_fields)
        # Handle saved items
        events = AFCEvents.objects.filter(
            case_id=case_id, form_id=form_id)
        print('Event', form_id, case_id, events)
        idata = {}
        if events:
            edate = events[0].event_date
            event_date = edate.strftime('%d-%b-%Y')
            idata['event_date'] = event_date
            event_id = events[0].pk
            fdatas = AFCForms.objects.filter(event_id=event_id)
            for fdata in fdatas:
                qid = fdata.question_id
                q_item = fdata.item_value
                q_detail = fdata.item_detail
                if qid.endswith('_txt'):
                    idata[qid] = q_detail
                elif qid.endswith('_rdo') or qid.endswith('_sdd'):
                    idata[qid] = q_item
                else:
                    if qid not in idata:
                        idata[qid] = []
                    idata[qid].append(q_item)
            print('idata', idata)
        form = get_form(form_id, idata)
        form_name = FMS[form_id] if form_id in FMS else 'Default'
        case = AFCMain.objects.get(is_void=False, case_id=case_id)
        person_id = case.person_id
        # Get persons registry info
        geos = RegPersonsGeo.objects.filter(
            person_id=person_id, is_void=False)
        for geo in geos:
            print('Geo', geo)
        siblings = RegPersonsSiblings.objects.select_related().filter(
            child_person=person_id, is_void=False, date_delinked=None)
        extids = RegPersonsExternalIds.objects.filter(
            person_id=person_id, is_void=False)
        ext_ids = {}
        for extid in extids:
            ext_ids[str(extid.identifier_type_id)] = extid.identifier
        # Save submitted records
        if request.method == 'POST':
            form.data = request.POST
            res = save_altcare_form(request, form_id)
            if res:
                url = reverse(
                    view_alternative_care, kwargs={'case_id': case_id})
            msg = 'Form - %s saved successfully' % (form_id)
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect(url)
        tmpl = 'afc/new_form_%s.html' % (form_id)
        case_uid = str(case_id).replace('-', '')
        return render(request, tmpl,
                      {'status': 200, 'case': case, 'form_id': form_id,
                       'form_name': form_name, 'vals': vals,
                       'form': form, 'case_id': case_uid, 'cid': cid,
                       'siblings': siblings, 'ext_ids': ext_ids})
    except Exception as e:
        raise e


def get_form(form_id, initial_data):
    """ Get the forms by ids."""
    try:
        form = AFCFormA(initial=initial_data)
        if form_id == 'A':
            form = AFCFormA(initial=initial_data)
    except Exception as e:
        raise e
    else:
        return form
