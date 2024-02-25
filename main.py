from get_series_chapters import GetSeriesChapters
from ....app.data_manager import RecordManager

serie_data = GetSeriesChapters('https://es.novelcool.com/novel/Madan-No-Ou-To-Michelia.html').call()
print(RecordManager().save(serie_data))

print(serie_data)