from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import openpyxl

# relative import of forms
from .models import ChecklistSeiscompModel, OperatorModel, StationListModel
from .forms import InputForm, OperatorForm, StationListForm


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    context['dataset'] = ChecklistSeiscompModel.objects.all().order_by('-tanggal')[:2]

    # add the dictionary during initialization
    input_form = InputForm(request.POST or None)
    if input_form.is_valid():
        input_form.save()
        # Resetting the form after it has been submitted.
        input_form = InputForm()

    context['input_form'] = input_form
    return render(request, "create_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = ChecklistSeiscompModel.objects.all().order_by('-tanggal')

    return render(request, "list_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(ChecklistSeiscompModel, id=id)

    # pass the object as instance in form
    form = OperatorForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def operator_delete(request, id):
    ob = OperatorModel.objects.get(id=id)
    ob.delete()
    return HttpResponseRedirect("/checklist-seiscomp/operator_view")


def data_delete(request, id):
    ob = ChecklistSeiscompModel.objects.get(id=id)
    ob.delete()
    return HttpResponseRedirect("/checklist-seiscomp/list_view")


def operator_update(request, id):
    ob = OperatorModel.objects.get(id=id)
    ob.name = request.POST.get('field1')
    ob.save()
    return HttpResponseRedirect("/checklist-seiscomp/operator_view")


def operator_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["operators"] = OperatorModel.objects.all()

    add_operator_form = OperatorForm(request.POST or None)
    if add_operator_form.is_valid():
        add_operator_form.save()

        # Resetting the form after it has been submitted.
        add_operator_form = OperatorForm()

    context['add_operator_form'] = add_operator_form

    return render(request, "operator_view.html", context)


def edit_operator_name(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(OperatorModel, id=id)

    # pass the object as instance in form
    form = OperatorForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "operator_view.html", context)


def export_excel_instant(request):
    """This function is used to export excel file containing last 2 records"""

    from django.conf import settings
    from .output_generator import generate_excel
    import ast


    data = ChecklistSeiscompModel.objects.all().order_by('-tanggal')[:2]
    metadata = {'kelompok': data[0].kelompok,
            'operator1': data[0].operator,
            'operator2': data[1].operator,
            'tanggal': date_range_to_string([data[1].tanggal, data[0].tanggal])}
    
    data1 = {}
    if data[1].gaps:
        data1['gaps'] = ast.literal_eval(data[1].gaps)
    else:
        data1['gaps'] = []

    if data[1].spikes:
        data1['spikes'] = ast.literal_eval(data[1].spikes)
    else:
        data1['spikes'] = []

    if data[1].blanks:
        data1['blanks'] = ast.literal_eval(data[1].blanks)
    else:
        data1['blanks'] = []    

    data2 = {}
    if data[0].gaps:
        data2['gaps'] = ast.literal_eval(data[0].gaps)
    else:
        data2['gaps'] = []    

    if data[0].spikes:
        data2['spikes'] = ast.literal_eval(data[0].spikes)
    else:
        data2['spikes'] = [] 

    if data[0].blanks:
        data2['blanks'] = ast.literal_eval(data[0].blanks)
    else:
        data2['blanks'] = [] 

    # Get the path of the Excel file in static folder
    file_path = str(settings.STATIC_ROOT) + '/ChecklistSeiscomp/template.xlsx'

    # Save the workbook to a byte stream
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    generate_excel(filename=file_path,
                   response=response,
                   metadata=metadata,
                   data1=data1,
                   data2=data2)
    
    # Set the file name and attachment header
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    # Return the response
    return response


def export_pdf_instant(request):
  from django.http import FileResponse
  
  file = open('path/to/your/pdf/file.pdf', 'rb')
  response = FileResponse(file)
  response['Content-Type'] = 'application/pdf'
  response['Content-Disposition'] = 'inline; filename="file.pdf"'
  return response


def date_range_to_string(date_range):
    import locale
    
    weekdays = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    date_strings = date_range
    start_date = date_strings[0].strftime('%d')
    end_date = date_strings[-1].strftime('%d')
    locale.setlocale(locale.LC_TIME, "id_ID.utf8")
    start_month = date_strings[0].strftime('%B')
    end_month = date_strings[-1].strftime('%B')
    start_year = date_strings[0].strftime('%Y')
    end_year = date_strings[-1].strftime('%Y')
    start_weekday = weekdays[date_strings[0].weekday()]
    end_weekday = weekdays[date_strings[-1].weekday()]
    if (start_year != end_year) and (start_month != end_month):
        return f"{start_weekday} - {end_weekday}, {start_date} {start_month} {start_year} - {end_date} {end_month} {end_year}"
    elif (start_year == end_year) and (start_month != end_month):
        return f"{start_weekday} - {end_weekday}, {start_date} {start_month} - {end_date} {end_month} {start_year}"
    else:
        return f"{start_weekday} - {end_weekday}, {start_date} - {end_date} {start_month} {start_year}"

def station_list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["station_list"] = StationListModel.objects.all()

    add_station_list_form = StationListForm(request.POST or None)
    if add_station_list_form.is_valid():
        add_station_list_form.save()

        # Resetting the form after it has been submitted.
        add_station_list_form = StationListForm()

    context['add_station_list_form'] = add_station_list_form

    return render(request, "station_list_view.html", context)        

def station_list_delete(request, id):
    ob = StationListModel.objects.get(id=id)
    ob.delete()
    return HttpResponseRedirect("/checklist-seiscomp/station_list_view")


def statistic_view(request):
    from django.db.models import Q
    from plotly.offline import plot
    import plotly.graph_objs as go
    from datetime import datetime
    import ast

    station_count = StationListModel.objects.count()
    last_data = ChecklistSeiscompModel.objects.all().last()

    x_data = list(ChecklistSeiscompModel.objects.filter(Q(jam='12:00 WIB')).values_list('tanggal', flat=True))
    x_datetime = []
    for x in x_data:
        x = datetime.strptime(x.strftime('%Y-%m-%d')+' 12:00', '%Y-%m-%d %H:%M')
        x_datetime.append(x)

    y_slmon_12 = list(ChecklistSeiscompModel.objects.filter(Q(jam='12:00 WIB')).values_list('slmon', flat=True))
    # y_slmon_0 = list(ChecklistSeiscompModel.objects.filter(Q(jam='00:00 WIB')).values_list('slmon', flat=True))
    y_blanks_12 = list(ChecklistSeiscompModel.objects.filter(Q(jam='12:00 WIB')).values_list('blanks', flat=True))
    # y_blanks_0 = list(ChecklistSeiscompModel.objects.filter(Q(jam='00:00 WIB')).values_list('blanks', flat=True))
    y_blanks_12_len = []

    for y in y_blanks_12:
        if y:
            y = len(ast.literal_eval(y))
            y_blanks_12_len.append(y)
        else:
            y_blanks_12_len.append(0)


    layout12=go.Layout(title="Grafik Slmon vs Blank Pukul 12:00 WIB", xaxis={'title':'Waktu'}, yaxis={'title':'Jumlah'})

    fig12 = go.Figure(data=[
            go.Bar(x=x_datetime, y=y_slmon_12,
                name='slmon 12:00 WIB',
                opacity=0.8, marker_color='red'),
            go.Bar(x=x_datetime, y=y_blanks_12_len,
                name='blanks 12:00 WIB',
                opacity=0.8, marker_color='blue'),
            ],
            layout=layout12)
    
    jam12 = plot(fig12,
               output_type='div', include_plotlyjs=False, show_link=False
               )
    layout00=go.Layout(title="Grafik Slmon vs Blank Pukul 00:00 WIB", xaxis={'title':'Waktu'}, yaxis={'title':'Jumlah'})
    
    fig00 = go.Figure(data=[
        go.Bar(x=x_datetime, y=y_slmon_12,
            name='slmon 12:00 WIB',
            opacity=0.8, marker_color='red'),
        ],
        layout=layout00)
    
    jam00 = plot(fig00,
               output_type='div', include_plotlyjs=False, show_link=False
               )
    
    # percentage of on and off of last record
    last_record = ChecklistSeiscompModel.objects.order_by('-tanggal')[:1]
    last_slmon = last_record.values('slmon')[0]['slmon'] or 0
    last_blanks = last_record.values('blanks')[0]['blanks']
    if last_blanks:
        last_blanks = len(ast.literal_eval(last_blanks))
    else:
        last_blanks = 0
    
    last_gaps = last_record.values('gaps')[0]['gaps']
    if last_gaps:
        last_gaps = len(ast.literal_eval(last_gaps))
    else:
        last_gaps = 0
    
    last_spikes = last_record.values('spikes')[0]['spikes']
    if last_spikes:
        last_spikes = len(ast.literal_eval(last_spikes))
    else:
        last_spikes = 0
    
    context = {'jam12': jam12,
               'jam00': jam00,
               'last_gaps': last_gaps,
               'last_spikes': last_spikes,
               'last_blanks': last_blanks,
               'last_slmon': last_slmon,
               'percent_gaps': round(last_gaps / station_count * 100, 2),
               'percent_spikes': round(last_spikes / station_count * 100, 2),
               'percent_blanks': round(last_blanks / station_count * 100, 2),
               'percent_slmon': round(last_slmon / station_count * 100, 2),
               'last_data': last_data
               }
    
    return render(request, "statistic_view.html", context=context)
