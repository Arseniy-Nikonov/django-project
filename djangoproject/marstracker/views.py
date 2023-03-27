from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponseRedirect,HttpResponse,Http404,HttpResponseNotFound
from django.urls import reverse,reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView,FormView
from .models import Game,Player,GameResults
from .forms import GameForm,PlayerForm,GamesForm
from django.forms import formset_factory

class IndexView(generic.ListView):
    template_name = 'marstracker/index.html'
    context_object_name = 'latest_game_list'
    
    def get_queryset(self):
        "Return the last five games"
        return Game.objects.order_by('-pub_date')[:50]

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
    form_class = GamesForm
    template_name = 'marstracker/game_add.html'

    number_of_players = 0

    def form_valid(self,form):
        self.number_of_players = form.cleaned_data['number_of_players']
        return super().form_valid(form)
    def get_success_url(self) -> str:
        success_url = reverse_lazy('marstracker:game-add-all',kwargs={'numberofplayers': self.number_of_players,'pk': Game.objects.latest('id').id})
        return success_url

def add_all_players_view(request,pk,numberofplayers):
    print(numberofplayers,pk)
    MyFormSet = formset_factory(PlayerForm,extra = numberofplayers)
    success_url = reverse_lazy('marstracker:game-list')
    error_url = reverse_lazy('marstracker:form-error')
    if request.method == "POST":
        formset = MyFormSet(request.POST)
        if formset.is_valid():
            form_error = False
            for subform in formset:
                print(subform.cleaned_data)
                game = Game.objects.get(pk = pk)
                player = subform.cleaned_data['player'][0]
                if not GameResults.objects.filter(player = player,game=game).exists():
                    game_results = GameResults(player = player,game = game)
                    game_results.final_score = subform.cleaned_data['final_score']
                    game_results.milestones_score = subform.cleaned_data['milestones_score']
                    game_results.awards_score = subform.cleaned_data['awards_score']
                    game_results.tr_score = subform.cleaned_data['tr_score']
                    game_results.card_score = subform.cleaned_data['card_score']
                    game_results.board_score = subform.cleaned_data['board_score']
                    game_results.save()
                else: 
                    form_error = True
            if form_error:
                return redirect(error_url)                       
            else:
                return redirect(success_url)
    else:
            formset = MyFormSet()

    return render(request, 'marstracker/game_add_all.html', {'formset':MyFormSet})

def form_error(request):
    return render(request,'marstracker/form_error')

class GameDetailView(generic.DetailView):
    model = Game
    template_name = 'marstracker/game_detail.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        players = Player.objects.all()
        game_id = self.kwargs['pk']
        game_results = GameResults.objects.all().filter(game = game_id)
        context['game_results'] = game_results
        context['players'] = players
        return context


class GameUpdateView(FormView):

    form_class = GameForm
    template_name = 'marstracker/game_update.html'
    success_url = reverse_lazy('marstracker:game-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player_id = self.kwargs['player']
        game_id = self.kwargs['game']
        game_results = GameResults.objects.get(game = game_id, player = player_id)
        context['game_result'] = game_results
        return context
    
    def get_initial(self):
        game_id = self.kwargs['game']
        player_id = self.kwargs['player']
        game = Game.objects.get(pk = game_id)
        player = Player.objects.get(pk = player_id)
        game_results = GameResults.objects.get(player = player_id,game = game_id)
        # Return the initial data for the form
        return {'final_score': game_results.final_score,
                'milestones_score': game_results.milestones_score,
                'awards_score': game_results.awards_score,
                'tr_score': game_results.tr_score,
                'card_score': game_results.card_score,
                'board_score': game_results.board_score
                }

    def form_valid(self, form, *args, **kwargs):
        game_id = self.kwargs['game']
        player_id = self.kwargs['player']
        game = Game.objects.get(pk = game_id)
        player = Player.objects.get(pk = player_id)
        game_results = GameResults.objects.get(player = player,game = game)
        player = form.cleaned_data['player'][0]
        game_results.final_score = form.cleaned_data['final_score']
        game_results.milestones_score = form.cleaned_data['milestones_score']
        game_results.awards_score = form.cleaned_data['awards_score']
        game_results.tr_score = form.cleaned_data['tr_score']
        game_results.card_score = form.cleaned_data['card_score']
        game_results.board_score = form.cleaned_data['board_score']
        # game_results.player = player
        game_results.save()
        return super().form_valid(form)
    
class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('marstracker:game-list')
    template_name = 'marstracker/game_confirm_delete.html'

class GameResultCreateView(CreateView):
    model = GameResults
    fields = ['final_score','milestones_score','awards_score','tr_score','card_score','board_score','player','game']
    template_name = 'marstracker/game_result_add.html'
    success_url = reverse_lazy('marstracker:game-list')


class GameResultsDeleteView(DeleteView):
    model = GameResults
    success_url = reverse_lazy('marstracker:game-list')
    template_name = 'marstracker/game_confirm_delete.html'