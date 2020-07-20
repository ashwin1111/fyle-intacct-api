"""fyle_intacct_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from .views import WorkspaceView, ConnectFyleView, ConnectSageIntacctView

urlpatterns = [
    path('', WorkspaceView.as_view({'get': 'get', 'post': 'post'})),
    path('<int:workspace_id>/', WorkspaceView.as_view({'get': 'get_by_id'})),
    path('<int:workspace_id>/connect_fyle/authorization_code/', ConnectFyleView.as_view({'post': 'post'})),
    path('<int:workspace_id>/credentials/fyle/', ConnectFyleView.as_view({'get': 'get'})),
    path('<int:workspace_id>/credentials/fyle/delete/', ConnectFyleView.as_view({'post': 'delete'})),
    path('<int:workspace_id>/credentials/sage_intacct/delete/', ConnectSageIntacctView.as_view({'post': 'delete'})),
    path('<int:workspace_id>/credentials/sage_intacct/', ConnectSageIntacctView.as_view({'post': 'post', 'get': 'get'})),
    path('<int:workspace_id>/fyle/', include('apps.fyle.urls')),
    path('<int:workspace_id>/sage_intacct/', include('apps.sage_intacct.urls')),
    path('<int:workspace_id>/mappings/', include('fyle_accounting_mappings.urls')),
    path('<int:workspace_id>/tasks/', include('apps.tasks.urls'))
]