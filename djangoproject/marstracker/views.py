from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponseRedirect,HttpResponse,Http404,HttpResponseNotFound
from django.urls import reverse
from django.views import generic
from .models import Game,Player,GameResults
from .forms import PlayerForm

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
    model = Game
    game = Game()
    game.save()

    return render(request, 'marstracker/detail.html')

def addplayer(request,game_id):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            game_results = GameResults(final_score = form.cleaned_data['final_score'], milestones_score = form.cleaned_data['milestones_score'], awards_score = form.cleaned_data['awards_score'], tr_score = form.cleaned_data['tr_score'],card_score = form.cleaned_data['card_score'],board_score = form.cleaned_data['board_score'])
            game_results.save()
            player = Player(first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])
            game = Game()
            player.save()
            try:
                Game.objects.get(pk = game_id)
                game = Game.objects.get(pk = game_id)
                game.players.add(player)
                game.save()
            except:
                game = Game()
                game_id = game.id
                game.players.add(player)
                game.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('marstracker:index'))

# if a GET (or any other method) we'll create a blank form
    else:
        form = PlayerForm()

    return render(request, 'marstracker/addplayer.html', {'form': form,'id': game_id} )
