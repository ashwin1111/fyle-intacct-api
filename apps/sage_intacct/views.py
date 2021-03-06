from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import generics

from fyle_accounting_mappings.models import DestinationAttribute
from fyle_accounting_mappings.serializers import DestinationAttributeSerializer

from fyle_intacct_api.utils import assert_valid

from apps.fyle.models import ExpenseGroup
from apps.tasks.models import TaskLog
from apps.workspaces.models import SageIntacctCredential

from .utils import SageIntacctConnector
from .tasks import create_expense_report, schedule_expense_reports_creation, create_bill, schedule_bills_creation
from .models import ExpenseReport
from .serializers import ExpenseReportSerializer


class EmployeeView(generics.ListCreateAPIView):
    """
    Employee view
    """
    serializer_class = DestinationAttributeSerializer
    pagination_class = None

    def get_queryset(self):
        return DestinationAttribute.objects.filter(
            attribute_type='EMPLOYEE', workspace_id=self.kwargs['workspace_id']).order_by('value')

    def post(self, request, *args, **kwargs):
        """
        Get employees from Sage Intacct
        """
        try:
            sage_intacct_credentials = SageIntacctCredential.objects.get(workspace_id=kwargs['workspace_id'])
            sage_intacct_connector = SageIntacctConnector(sage_intacct_credentials, workspace_id=kwargs['workspace_id'])

            employees = sage_intacct_connector.sync_employees()

            return Response(
                data=self.serializer_class(employees, many=True).data,
                status=status.HTTP_200_OK
            )
        except SageIntacctCredential.DoesNotExist:
            return Response(
                data={
                    'message': 'Sage Intacct credentials not found in workspace'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class VendorView(generics.ListCreateAPIView):
    """
    Vendor view
    """
    serializer_class = DestinationAttributeSerializer
    pagination_class = None

    def get_queryset(self):
        return DestinationAttribute.objects.filter(
            attribute_type='VENDOR', workspace_id=self.kwargs['workspace_id']).order_by('value')

    def post(self, request, *args, **kwargs):
        """
        Get vendors from Sage Intacct
        """
        try:
            sage_intacct_credentials = SageIntacctCredential.objects.get(workspace_id=kwargs['workspace_id'])
            sage_intacct_connector = SageIntacctConnector(sage_intacct_credentials, workspace_id=kwargs['workspace_id'])

            vendors = sage_intacct_connector.sync_vendors()

            return Response(
                data=self.serializer_class(vendors, many=True).data,
                status=status.HTTP_200_OK
            )
        except SageIntacctCredential.DoesNotExist:
            return Response(
                data={
                    'message': 'Sage Intacct credentials not found in workspace'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class AccountView(generics.ListCreateAPIView):
    """
    Account view
    """
    serializer_class = DestinationAttributeSerializer
    pagination_class = None

    def get_queryset(self):
        return DestinationAttribute.objects.filter(
            attribute_type='ACCOUNT', workspace_id=self.kwargs['workspace_id']).order_by('value')

    def post(self, request, *args, **kwargs):
        """
        Get accounts from Sage Intacct
        """
        try:
            sage_intacct_credentials = SageIntacctCredential.objects.get(workspace_id=kwargs['workspace_id'])
            sage_intacct_connector = SageIntacctConnector(sage_intacct_credentials, workspace_id=kwargs['workspace_id'])

            accounts = sage_intacct_connector.sync_accounts()

            return Response(
                data=self.serializer_class(accounts, many=True).data,
                status=status.HTTP_200_OK
            )
        except SageIntacctCredential.DoesNotExist:
            return Response(
                data={
                    'message': 'Sage Intacct credentials not found in workspace'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class DepartmentView(generics.ListCreateAPIView):
    """
    Department view
    """
    serializer_class = DestinationAttributeSerializer
    pagination_class = None

    def get_queryset(self):
        return DestinationAttribute.objects.filter(
            attribute_type='DEPARTMENT', workspace_id=self.kwargs['workspace_id']).order_by('value')

    def post(self, request, *args, **kwargs):
        """
        Get departments from Sage Intacct
        """
        try:
            sage_intacct_credentials = SageIntacctCredential.objects.get(workspace_id=kwargs['workspace_id'])
            sage_intacct_connector = SageIntacctConnector(sage_intacct_credentials, workspace_id=kwargs['workspace_id'])

            departments = sage_intacct_connector.sync_departments()

            return Response(
                data=self.serializer_class(departments, many=True).data,
                status=status.HTTP_200_OK
            )
        except SageIntacctCredential.DoesNotExist:
            return Response(
                data={
                    'message': 'Sage Intacct credentials not found in workspace'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class ExpenseTypeView(generics.ListCreateAPIView):
    """
    Expense Type view
    """
    serializer_class = DestinationAttributeSerializer
    pagination_class = None

    def get_queryset(self):
        return DestinationAttribute.objects.filter(
            attribute_type='EXPENSE_TYPE', workspace_id=self.kwargs['workspace_id']).order_by('value')

    def post(self, request, *args, **kwargs):
        """
        Get expense type from Sage Intacct
        """
        try:
            sage_intacct_credentials = SageIntacctCredential.objects.get(workspace_id=kwargs['workspace_id'])
            sage_intacct_connector = SageIntacctConnector(sage_intacct_credentials, workspace_id=kwargs['workspace_id'])

            expense_types = sage_intacct_connector.sync_expense_types()

            return Response(
                data=self.serializer_class(expense_types, many=True).data,
                status=status.HTTP_200_OK
            )
        except SageIntacctCredential.DoesNotExist:
            return Response(
                data={
                    'message': 'Sage Intacct credentials not found in workspace'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class ProjectView(generics.ListCreateAPIView):
    """
    Project view
    """
    serializer_class = DestinationAttributeSerializer
    pagination_class = None

    def get_queryset(self):
        return DestinationAttribute.objects.filter(
            attribute_type='PROJECT', workspace_id=self.kwargs['workspace_id']).order_by('value')

    def post(self, request, *args, **kwargs):
        """
        Get projects from Sage Intacct
        """
        try:
            sage_intacct_credentials = SageIntacctCredential.objects.get(workspace_id=kwargs['workspace_id'])
            sage_intacct_connector = SageIntacctConnector(sage_intacct_credentials, workspace_id=kwargs['workspace_id'])

            projects = sage_intacct_connector.sync_projects()

            return Response(
                data=self.serializer_class(projects, many=True).data,
                status=status.HTTP_200_OK
            )
        except SageIntacctCredential.DoesNotExist:
            return Response(
                data={
                    'message': 'Sage Intacct credentials not found in workspace'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class LocationView(generics.ListCreateAPIView):
    """
    Location view
    """
    serializer_class = DestinationAttributeSerializer
    pagination_class = None

    def get_queryset(self):
        return DestinationAttribute.objects.filter(
            attribute_type='LOCATION', workspace_id=self.kwargs['workspace_id']).order_by('value')

    def post(self, request, *args, **kwargs):
        """
        Get locations from Sage Intacct
        """
        try:
            sage_intacct_credentials = SageIntacctCredential.objects.get(workspace_id=kwargs['workspace_id'])
            sage_intacct_connector = SageIntacctConnector(sage_intacct_credentials, workspace_id=kwargs['workspace_id'])

            locations = sage_intacct_connector.sync_locations()

            return Response(
                data=self.serializer_class(locations, many=True).data,
                status=status.HTTP_200_OK
            )
        except SageIntacctCredential.DoesNotExist:
            return Response(
                data={
                    'message': 'Sage Intacct credentials not found in workspace'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class ExpenseReportView(generics.ListCreateAPIView):
    """
    Create Expense Report
    """
    serializer_class = ExpenseReportSerializer

    def get_queryset(self):
        return ExpenseReport.objects.filter(expense_group__workspace_id=self.kwargs['workspace_id'])\
            .order_by('-updated_at')

    def post(self, request, *args, **kwargs):
        """
        Create expense report from expense group
        """
        expense_group_id = request.data.get('expense_group_id')
        task_log_id = request.data.get('task_log_id')

        assert_valid(expense_group_id is not None, 'expense group id not found')
        assert_valid(task_log_id is not None, 'Task Log id not found')

        expense_group = ExpenseGroup.objects.get(pk=expense_group_id)
        task_log = TaskLog.objects.get(pk=task_log_id)

        create_expense_report(expense_group, task_log)

        return Response(
            data={},
            status=status.HTTP_200_OK
        )


class ExpenseReportScheduleView(generics.CreateAPIView):
    """
    Schedule expense reports create
    """

    def post(self, request, *args, **kwargs):
        expense_group_ids = request.data.get('expense_group_ids', [])

        schedule_expense_reports_creation(
            kwargs['workspace_id'], expense_group_ids, request.user)

        return Response(
            status=status.HTTP_200_OK
        )


class BillView(generics.ListCreateAPIView):
    """
    Create Bill
    """
    serializer_class = ExpenseReportSerializer

    def get_queryset(self):
        return ExpenseReport.objects.filter(expense_group__workspace_id=self.kwargs['workspace_id'])\
            .order_by('-updated_at')

    def post(self, request, *args, **kwargs):
        """
        Create bill from expense group
        """
        expense_group_id = request.data.get('expense_group_id')
        task_log_id = request.data.get('task_log_id')

        assert_valid(expense_group_id is not None, 'expense group id not found')
        assert_valid(task_log_id is not None, 'Task Log id not found')

        expense_group = ExpenseGroup.objects.get(pk=expense_group_id)
        task_log = TaskLog.objects.get(pk=task_log_id)

        create_bill(expense_group, task_log)

        return Response(
            data={},
            status=status.HTTP_200_OK
        )


class BillScheduleView(generics.CreateAPIView):
    """
    Schedule bill create
    """

    def post(self, request, *args, **kwargs):
        expense_group_ids = request.data.get('expense_group_ids', [])

        schedule_bills_creation(
            kwargs['workspace_id'], expense_group_ids, request.user)

        return Response(
            status=status.HTTP_200_OK
        )
