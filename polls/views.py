from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages

from polls.models import LGA, PollUnit
from polls.forms import AddPollUnitForm


class AddPollUnitView(View):
    def get(self, request):
        add_poll_unit_form = AddPollUnitForm()

        context = {"add_poll_unit_form": add_poll_unit_form}

        return render(request, "add-poll-unit.html", context)

    def post(self, request):
        add_poll_unit_form = AddPollUnitForm(request.POST)

        if add_poll_unit_form.is_valid():
            add_poll_unit_form.save()

            messages.success(request, "Poll unit has been added")

            return redirect("polls-new")

        add_poll_unit_form = AddPollUnitForm()

        context = {"add_poll_unit_form": add_poll_unit_form}

        return render(request, "add-poll-unit.html", context)


class PollUnitListView(View):
    def get(self, request):
        poll_unit_list = PollUnit.objects.order_by("-date_entered")

        context = {"poll_units": poll_unit_list}

        return render(request, "polls-unit-list.html", context)


class PollUnitDetailView(View):
    def get(self, request, unit_number):
        poll_unit = PollUnit.objects.filter(polling_unit_number=unit_number).first()

        context = {"poll_unit": poll_unit}

        return render(request, "polls-unit-detail.html", context)


class LGAListView(View):
    def get(self, request):
        lgas = LGA.objects.order_by("-date_entered")

        context = {"lgas": list(set(lgas))}

        return render(request, "lga-list.html", context)


class LGAPollUnitList(View):
    def get(self, request, lga_id):
        poll_units = PollUnit.objects.filter(lga_id_id=lga_id).order_by("-date_entered")

        if not poll_units.exists():
            messages.error(request, f"Polling unit(s) with id {lga_id} not found")
            return redirect("lga-list")

        lgas = LGA.objects.order_by("-date_entered")
        lga = PollUnit.objects.filter(lga_id=lga_id).first()

        context = {"poll_units": poll_units, "lga": lga, "lgas": list(set(lgas))}

        return render(request, "polls-unit-list.html", context)
