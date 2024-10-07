extends Node2D

const speed = 20

var dir = 1


@onready var ray_castright = $RayCastright
@onready var ray_castleft = $RayCastleft
@onready var animated_sprite_2d = $AnimatedSprite2D



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if ray_castleft.is_colliding():
		dir = 1
		animated_sprite_2d.flip_h = false
	if ray_castright.is_colliding():
		dir = -1
		animated_sprite_2d.flip_h = true
	position.x += dir * speed * delta
