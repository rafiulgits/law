from django import template

register = template.Library()


def input_class(value):
	print(type(value))
	print(help(value))
	value = str(value)
	tag = value.split('<input ')
	print(tag)
	attribute = 'class="form-input" '
	return '<input '+attribute+tag[1]

register.filter('input_class', input_class)