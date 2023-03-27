from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import openpyxl

# relative import of forms
from .models import ChecklistSeiscompModel, OperatorModel
from .forms import InputForm, OperatorForm


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
    context["dataset"] = ChecklistSeiscompModel.objects.all()

    return render(request, "list_view.html", context)

# pass id attribute from urls


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = ChecklistSeiscompModel.objects.get(id=id)

    return render(request, "detail_view.html", context)

# update view for details


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

# delete view for details


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

def export_data(request):
    from django.conf import settings
    # Get the path of the Excel file in your static folder
    file_path = str(settings.STATIC_ROOT) + '/ChecklistSeiscomp/template.xlsx'
    # Create a workbook object
    wb = openpyxl.load_workbook(file_path)

    # Save the workbook to a byte stream
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    wb.save(response)
    # Set the file name and attachment header
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
    # Return the response
    return response