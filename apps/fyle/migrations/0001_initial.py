import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_email', models.EmailField(help_text='Email id of the Fyle employee', max_length=255)),
                ('category', models.CharField(blank=True, help_text='Fyle Expense Category', \
                    max_length=255, null=True)),
                ('sub_category', models.CharField(blank=True, help_text='Fyle Expense Sub-Category', \
                    max_length=255, null=True)),
                ('project', models.CharField(blank=True, help_text='Project', max_length=255, null=True)),
                ('expense_id', models.CharField(help_text='Expense ID', max_length=255, unique=True)),
                ('expense_number', models.CharField(help_text='Expense Number', max_length=255)),
                ('claim_number', models.CharField(help_text='Claim Number', max_length=255, null=True)),
                ('amount', models.FloatField(help_text='Home Amount')),
                ('currency', models.CharField(help_text='Home Currency', max_length=5)),
                ('foreign_amount', models.FloatField(help_text='Foreign Amount', null=True)),
                ('foreign_currency', models.CharField(help_text='Foreign Currency', max_length=5, null=True)),
                ('settlement_id', models.CharField(help_text='Settlement ID', max_length=255)),
                ('reimbursable', models.BooleanField(default=False, help_text='Expense reimbursable or not')),
                ('exported', models.BooleanField(default=False, help_text='Expense exported or not')),
                ('state', models.CharField(help_text='Expense state', max_length=255)),
                ('vendor', models.CharField(blank=True, help_text='Vendor', max_length=255, null=True)),
                ('cost_center', models.CharField(blank=True, help_text='Fyle Expense Cost Center', \
                    max_length=255, null=True)),
                ('purpose', models.TextField(blank=True, help_text='Purpose', null=True)),
                ('report_id', models.CharField(help_text='Report ID', max_length=255)),
                ('spent_at', models.DateTimeField(help_text='Expense spent at', null=True)),
                ('approved_at', models.DateTimeField(help_text='Expense approved at', null=True)),
                ('expense_created_at', models.DateTimeField(help_text='Expense created at')),
                ('expense_updated_at', models.DateTimeField(help_text='Expense created at')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at')),
                ('fund_source', models.CharField(help_text='Expense fund source', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fyle_group_id', models.CharField(help_text='fyle expense group id report id, etc', \
                    max_length=255, unique=True)),
                ('description', django.contrib.postgres.fields.jsonb.JSONField(help_text='Description', \
                    max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at')),
                ('expenses', models.ManyToManyField(help_text='Expenses under this Expense Group', to='fyle.Expense')),
                ('workspace', models.ForeignKey(help_text='To which workspace this expense group belongs to', \
                    on_delete=django.db.models.deletion.PROTECT, to='workspaces.Workspace')),
            ],
        ),
        migrations.AlterModelTable(
            name='Expense',
            table='expenses',
        ),
        migrations.AlterModelTable(
            name='ExpenseGroup',
            table='expense_groups',
        ),
    ]
