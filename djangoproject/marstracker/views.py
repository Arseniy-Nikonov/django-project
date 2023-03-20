from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404
from .models import Game,Player,GameResults

def index(request):
    player_list = Player.objects.order_by('-reg_date')
    template = loader.get_template('marstracker/index.html')
    context = {'player_list':player_list}
    return HttpResponse(template.render(context,request))
       #return render(request, 'marstracker/index.html', context)
    # latest_game_list = GameStatistics.objects.order_by('-pub_date')
    # template = loader.get_template('marstracker/index.html')
    # context = {'latest_gamer_list':latest_game_list}
    # return HttpResponse(template.render(context,request))
    #return render(request, 'marstracker/index.html', context)

def detail(request, game_id):
    try:
        games = Game.objects.all()
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    return render(request, 'marstracker/detail.html', {'games': games})
    #def detail(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})

def gamestatistics(request, game_id):
    return HttpResponse("You're looking at the results of game %s." % game_id)

def addgame(request):
    if request.method == 'POST':
        # Get the post data from the form
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        final_score = request.POST.get('finalscore')

        # Create a new object with the acquired data
        player = Player(first_name=first_name,last_name=last_name )
        player.save()
        game_results = GameResults(final_score=final_score)
        game_results.save()
        game = Game(game_results=game_results)
        game.save()

        game.players.add(player)
 


        # Redirect to a success page
        return HttpResponse('Success!')
    
    return render(request, 'marstracker/addgame.html')