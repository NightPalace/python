# 8-7
def make_album(singer, album_name, songs=1):
	""" 描述唱片如何生成 """
	return singer.title() + '的专辑是' + album_name.title() + '， 一共有' + str(songs) + '首歌. '

albums = {};
albums['薛海峰'] = make_album('薛海峰', '海峰之歌')
albums['张雪婷'] = make_album('张雪婷', '雪婷之歌', 2)
albums['杨彬彬'] = make_album('杨彬彬', '彬彬之歌', 5)

for v in albums.values():
	print(v)
	