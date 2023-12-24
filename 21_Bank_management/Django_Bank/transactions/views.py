# from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
# from django.views import View
# from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSIT, WITHDRAWAL,LOAN, LOAN_PAID
# from datetime import datetime
# from django.db.models import Sum
# from transactions.forms import (
#     DepositForm,
#     WithdrawForm,
#     LoanRequestForm,
# )
from transactions.models import Transaction

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    # template_name = 'transactions/transaction_form.html'
    template_name = ''
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # template e context data pass kora
        context.update({
            'title': self.title
        })

        return context

