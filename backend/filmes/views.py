from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404, JsonResponse, HttpResponse
from .models import Filme, FunFacts, Anuncio
from .serializers import FilmeSerializer, FactSerializer, AnuncioSerializer

@api_view(['GET', 'POST'])
def api_filme(request, titulo): 
    if request.method == 'POST':
        nova_palavra = request.data

        if nova_palavra != None:
        
            try:
                filme = Filme.objects.get(title=titulo)
                filme.palavras += "," + nova_palavra
                filme.save()
            except Filme.DoesNotExist:
                Filme.objects.create(title=titulo, palavras=nova_palavra)
                filme = Filme.objects.get(title=titulo)

            serialized_filme = FilmeSerializer(filme)
            return Response(serialized_filme.data)

    else:
        try:
            filme = Filme.objects.get(title=titulo)
            serialized_filme = FilmeSerializer(filme)
            return Response(serialized_filme.data)
        except Filme.DoesNotExist:
            return HttpResponse(status=204)

@api_view(['GET', 'DELETE'])
def delete_word(request, titulo, palavra):
    try:
        filme = Filme.objects.get(title = titulo)
    except Filme.DoesNotExist:
        raise Http404()
    
    if request.method == 'DELETE':
        if palavra == None or palavra == '':
            return JsonResponse({'reload': True})
        palavras_f = filme.palavras.split(",")
        print("===============================================================")
        print(palavras_f)

        for p in palavras_f:
            if p == '':
                palavras_f.remove(p)
        
        print(palavras_f)

        for p in palavras_f:
            if p == palavra:
                palavras_f.remove(palavra)
                break
        print(palavras_f)
        
        if len(palavras_f) > 0:
            if palavras_f[0] != '':
                new_palavras = palavras_f[0]
            else:
                palavras_f.remove('')
                new_palavras = palavras_f[0]
            for new_p in palavras_f[1:]:
                if new_p != '' and new_p != None:
                    new_palavras += "," + new_p
            filme.palavras = new_palavras
        else:
            filme.palavras = ''
            
        filme.save()

        return JsonResponse({'reload': True})

    serialized_filme = FilmeSerializer(filme)
    return Response(serialized_filme.data)

@api_view(['GET', 'POST'])
def facts(request):
    try:
        if request.method == 'POST':
            fact = request.data['fact']
            FunFacts.objects.create(fact=fact)

        facts = FunFacts.objects.all()
        print(facts)
        serialized_facts = FactSerializer(facts, many=True)
        return Response(serialized_facts.data)
    
    except:
        return HttpResponse(status=204)

@api_view(['DELETE'])
def deletefact(request, id):
    fact = FunFacts.objects.get(id=id)
    fact.delete()
    return HttpResponse(status=204)

@api_view(['GET', 'POST'])
def anuncios(request):
    try:
        if request.method == 'POST':
            headline = request.data['headline']
            img = request.data['img']
            link = request.data['link']
            Anuncio.objects.create(headline=headline, img=img, link=link)

        anuncios = Anuncio.objects.all()
        print(anuncios)
        serialized_anuncios = AnuncioSerializer(anuncios, many=True)
        return Response(serialized_anuncios.data)
    
    except:
        return HttpResponse(status=204)

@api_view(['GET', 'POST', 'DELETE'])  
def update_anuncio(request, id):
    try:
        anuncio = Anuncio.objects.get(id=id)

        if request.method == 'POST':
            anuncio.headline = request.data['headline']
            anuncio.img = request.data['img']
            anuncio.link = request.data['link']
            anuncio.save()
        
            serialized_anuncio = AnuncioSerializer(anuncio)
            return Response(serialized_anuncio.data)
        
        elif request.method == 'DELETE':
            anuncio.delete()
            return HttpResponse(status=204)

    except:
        return HttpResponse(status=204)
