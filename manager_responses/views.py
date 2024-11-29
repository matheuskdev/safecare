from django.contrib import messages
from typing import Any
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from manager_responses.forms import ManagerResponseForm
from .models import ManagerResponse
from responses.models import ResponseOcurrence
from .common import GenericResponseFormView, MessageDescription


class ManagerResponseListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView
):
    """
    View to list all manager responses.
    """
    model = ResponseOcurrence
    template_name = 'manager_responses/list.html'
    context_object_name = "response"
    permission_required = "manager_responses.view_manager_response"

    def get_queryset(self):
        return ResponseOcurrence.objects.filter(send_manager=True)


class ManagerResponseFormView(GenericResponseFormView):
    """
    View to create manager responses.
    """
    model = ManagerResponse
    form_class = ManagerResponseForm
    template_name: str = "manager_responses/form.html"
    success_url = "manager_responses:sucess"
    permission_required = "manager_response.add_manager_response"
    context_responses_model = ResponseOcurrence
    response_ocurrence_id = None

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        
        try:
            response: HttpResponse = super().dispatch(request, *args, **kwargs)
            """             self.response_ocurrence: ResponseOcurrence = get_object_or_404(
                ResponseOcurrence, ocurrence=self.ocurrence_id
            ) """
        except Exception:
            messages.add_message(
                request,
                messages.ERROR,
                MessageDescription().get_message_description("ERROR")
            )
            return redirect(reverse_lazy("events:eventocurrence_create"))
        return response

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        Adds additional context for rendering the template.
        """
        context: dict[str, Any] = super().get_context_data(**kwargs)
        

        return context
