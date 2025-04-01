from django.contrib.admin.sites import AdminSite


def get_app_list(self, request):
    """
    Return a sorted list of all the installed apps that have been
    registered in this site.
    """
    app_dict = self._build_app_dict(request)
    ordering = {"Reben": 1, "Kulturpflanzen": 2}
    # Sort the apps alphabetically.
    app_list = sorted(app_dict.values(), key=lambda x: ordering.get(x["name"], 3))

    # Sort the models alphabetically within each app.
    for app in app_list:
        app["models"].sort(key=lambda x: x["name"])

    return app_list
