from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404
from .models import GameStatistics,PlayerStatistics,Player

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

def detail(request, player_id):
    try:
        games = GameStatistics.objects.all()
    except GameStatistics.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'marstracker/detail.html', {'games': games})
    #def detail(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})


def results(request, player_id):
    response = "You're looking at the results of player statistics %s."
    return HttpResponse(response % player_id)

def vote(request, player_id):
    return HttpResponse("You're voting on question %s." % player_id)