from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game

class GameView(ViewSet):
    """ Level Up game view"""
    
    def retrieve(self, request, pk):
        """handels get requests for single game
        Returns:
            Response -- JSON serialized game
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """hnadles get requests for all games
        Returns:
            Response -- JSON serialized list of all games 
        """
        games = Game.objects.all()
        # game_type = request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type_id=game_type)     
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    class Meta:
        model = Game
        fields = ('id', 'title', 'maker', 'number_of_players', 'skill_level', 'game_type_id', 'gamer_id')
        depth = 1

        
        