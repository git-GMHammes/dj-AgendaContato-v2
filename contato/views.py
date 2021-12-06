from django.shortcuts import render, get_object_or_404
# ↑ get_object_or_404 - Para tratamento do erro 404
# ↓ Http404 - Para tratar registros que não devem ser apresentados
from django.http import Http404
# ↓ Importado do models
from .models import ContatoDj
# ↓ paginando o resultado exibido
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    # → recebeDbContatos - Variável que recebe os dados do DB
    # → HtmlContatos - Variável que recebe o a variável em um dicionário {'':''}
    # → Para exibir no arquivo [APP]/templates/index.html
    # → paginator - Variável de paginação
    recebeDbContatos = ContatoDj.objects.all()
    # ↓ Dados de paginação
    paginator = Paginator(recebeDbContatos, 7)
    page = request.GET.get('p')
    recebeDbContatos = paginator.get_page(page)
    return render(request, 'contato/index.html', {
        'HtmlContatos' : recebeDbContatos
    })

def exibeContato(request, contato_id):
    # var - descricao
    # recebeDbContato = ContatoDj.objects.get(id=contato_id)
    # ↓ → Substitui a linha acima para tratar o erro 404
    recebeDbContato = get_object_or_404(ContatoDj, id=contato_id)
    # ↓ Http404 - Para tratar registros que não devem ser apresentados
    if not recebeDbContato.exibir:
        raise Http404()
    return render(request, 'contato/exibeContato.html', {
        'HtmlContato' : recebeDbContato
    })