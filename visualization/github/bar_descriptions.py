import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style=LS('#333366', base_style=LCS)

chart=pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title='Javascript Projects'
chart.x_labels=['httpie', 'django', 'flask']
plot_dicts=[
	{'value': 16101, 'label': 'Description of Httpie'},
	{'value': 15028, 'label': 'Description of Django'},
	{'value': 14798, 'label': 'Description of Flask'}
]
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')