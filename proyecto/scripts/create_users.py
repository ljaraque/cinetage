from django.contrib.auth import get_user_model
User = get_user_model()

def create_initial_users():
    if len(User.objects.filter(username="admin"))==0:
        User.objects.create_superuser(username="admin", password="admin", rol="superadmin")
    if len(User.objects.filter(username="operador_1"))==0:
        User.objects.create_user(username="operador_1", password="1234", rol="operador")    
    if len(User.objects.filter(username="cliente_1"))==0:
        cliente_1 = User.objects.create_user(username="cliente_1", password="1234", rol="cliente")
    if len(User.objects.filter(username="subcliente_1"))==0:
        User.objects.create_user(username="subcliente_1", password="1234", rol="subcliente", principal=cliente_1)
    if len(User.objects.filter(username="subcliente_2"))==0:
        User.objects.create_user(username="subcliente_2", password="1234", rol="subcliente", principal=cliente_1)
    if len(User.objects.filter(username="subcliente_3"))==0:
        User.objects.create_user(username="subcliente_3", password="1234", rol="subcliente", principal=cliente_1)
    if len(User.objects.filter(username="subcliente_4"))==0:
        User.objects.create_user(username="subcliente_4", password="1234", rol="subcliente", principal=cliente_1)