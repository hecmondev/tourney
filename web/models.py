from django.db import models

# Create your models here.
class Gamer(models.Model):
  name = models.CharField(verbose_name="Name", null=False, max_length=25)
  active = models.BooleanField(verbose_name="Active", null=False)

  class Meta:
    db_table = "gamers"
    verbose_name = "Gamer"
    verbose_name_plural = "Gamers"

  def __str__(self) -> str:
    return self.name

class Game(models.Model):
  name = models.CharField(verbose_name="Name", null=False, max_length=50)
  active = models.BooleanField(verbose_name="Active", null=False)

  class Meta:
    db_table = "games"
    verbose_name = "Game"
    verbose_name_plural = "Games"

  def __str__(self) -> str:
    return self.name

class Playing(models.Model):
  gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
  game = models.ForeignKey(Game, on_delete=models.CASCADE)
  active = models.BooleanField(verbose_name="Active", null=False)

  class Meta:
    db_table = "playing"
    verbose_name = "Playing"
    verbose_name_plural = "Playing"

  def __str__(self) -> str:
    return f"{self.gamer.name} is playing {self.game.name}"