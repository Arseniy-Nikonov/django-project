from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponseRedirect,HttpResponse,Http404,HttpResponseNotFound
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView,FormView
from .models import Game,Player,GameResults
from .forms import PlayerForm

class IndexView(generic.ListView):
    template_name = 'marstracker/index.html'
    context_object_name = 'latest_game_list'
    
    def get_queryset(self):
        "Return the last five games"
        return Game.objects.order_by('-pub_date')[:50]

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
    try:
        game = Game.objects.latest('pk')
        game_id = game.pk + 1
        game = Game()
        game.save()
    except:
        game_id = 1
        game = Game()
        game.save()
    return HttpResponseRedirect(reverse('marstracker:detail',kwargs={'pk': game_id}))

def addplayer(request,game_id):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            player = Player(first_name = form.cleaned_data['first_name'], last_name = form.cleaned_data['last_name'])
            game = Game()
            player.save()
            game_results = GameResults(final_score = form.cleaned_data['final_score'], milestones_score = form.cleaned_data['milestones_score'], awards_score = form.cleaned_data['awards_score'], tr_score = form.cleaned_data['tr_score'],card_score = form.cleaned_data['card_score'],board_score = form.cleaned_data['board_score'],player=player)
            game_results.save()
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

# class PlayerCreateView(FormView):
#     form_class = PlayerForm
#     template_name = 'marstracker/player_add.html'
#     success_url = reverse_lazy('marstracker:player-list')

class PlayerCreateView(CreateView):
    model = Player
    template_name = 'marstracker/player_add.html'
    fields = ['first_name','last_name']
    success_url = reverse_lazy('marstracker:player-list')

class PlayerUpdateView(UpdateView):
    model = Player
    fields = ['first_name','last_name']
    template_name = 'marstracker/player_add.html'

class PlayerDeleteView(DeleteView):
    model = Player
    success_url = reverse_lazy('marstracker:player-list')
    template_name = 'marstracker/player_confirm_delete.html'


class PlayerList(generic.ListView):
    template_name = 'marstracker/player_list.html'
    context_object_name = 'player_list'
    
    def get_queryset(self):
        "Return the last fifty registered plaers"
        return Player.objects.order_by('-reg_date')[:50]

class GameList(generic.ListView):
    template_name = 'marstracker/game_list.html'
    context_object_name = 'game_list'
    
    def get_queryset(self):
        "Return all games"
        return Game.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        players = Player.objects.all()
        game_results = GameResults.objects.all()
        context['game_results'] = game_results
        context['players'] = players
        return context
    
class GameCreateView(CreateView):
    model = Game
    fields = ['map_type']
    template_name = 'marstracker/game_add.html'
    success_url = reverse_lazy('marstracker:game-list')

class GameDetailView(generic.DetailView):
    pass
class GameUpdateView(UpdateView):
    pass

class GameDeleteView(DeleteView):
    pass