extends Area2D

@onready var player = $"../../player"
@onready var animation_player = $AnimationPlayer


func _on_body_entered(body):
	player.add_point()
	animation_player.play("pickup")
