from django.http import HttpResponse
from django.template import loader, RequestContext
from lista.models import Contatos


def index(request):
    contatos = Contatos.objects.order_by('codigo')
    template = loader.get_template('lista/index.html')
    context = RequestContext(request, {
        'contatos': contatos,
    })
    return HttpResponse(template.render(context))


def gravar(request):
    contato = Contatos()
    contato.nome = request.POST['nome']
    contato.email = request.POST['email']
    contato.save()

    return index(request)


def excluir(request):
    if request.method == 'POST':
        contato = Contatos.objects.get(codigo=request.POST['codigo'])
        contato.delete()

    return index(request)
