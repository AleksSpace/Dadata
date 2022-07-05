from dadata import Dadata
from django.contrib.admin import AdminSite
from django.shortcuts import render

TOKEN = "5972803ddb5251f578cd38d1848d415ba68a3cfd"
SECRET = "90de7249acd8fb10e29cc0dea2233b266555a3ba"


class MyAdminSite(AdminSite):

    site_header = 'Мой сайт администратора'

    def index(self, request, extra_context=None):
        result = []
        super().index(request, extra_context)
        app_list = super().get_app_list(request)

        if request.method == 'POST':
            address = request.POST.get('address')
            dadata = Dadata(TOKEN, SECRET)
            result = dadata.clean("address", address)
        context = {
            **self.each_context(request),
            "title": self.index_title,
            "subtitle": None,
            "app_list": app_list,
            **(extra_context or {}),
            "enable_data": True,
            "data": result,
        }
        return render(request, 'admin/index.html', context)


admin_site = MyAdminSite(name="my_admin")
