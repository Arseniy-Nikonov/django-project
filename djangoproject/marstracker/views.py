from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseNotFound
from django.urls import reverse
from django.views import generic
from .models import Game,Player,GameResults


class IndexView(generic.ListView):
    template_name = 'marstracker/index.html'
    context_object_name = 'latest_game_list'
    
    def get_queryset(self):
        "Return the last five games"
        return Game.objects.order_by('-pub_date')[:5]
    

# def detail(request, game_id):
#     try:
#         games = Game.objects.all()
#     except Game.DoesNotExist:
#         raise Http404("Game does not exist")
#     return render(request, 'marstracker/detail.html', {'games': games})

class DetailView(generic.DetailView):
    model = Game
    template_name = 'marstracker/detail.html'
    def get_object(self, queryset=None):
        try:
            response = super().get_object(queryset=queryset)
        except Http404:
            # Redirect to a different page if the object was not found
            # response = self.handle_not_found()
            return "You've attempted to access game index that does not exist in the database"
        return response
    
    # def handle_not_found(self):
    #     # Customize the behavior when the object is not found
    #     # Return an HttpResponse or render a template
    #     return HttpResponseNotFound("The requested object was not found.")


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
        return render(request, 'marstracker/addgame.html')
    
    return render(request, 'marstracker/addgame.html')