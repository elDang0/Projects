extends Node2D
@onready var color_rect = $ColorRect
@onready var button = $Button




func _on_button_pressed():
	color_rect.visible = not color_rect.visible
