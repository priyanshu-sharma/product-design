from django.db import connections
from django.http import JsonResponse


def database_check():
    db_connection = connections["default"]
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT 1;")
        return cursor.fetchall()


def health_check_view(request):
    database_check()

    return JsonResponse({"health": "ok"})
