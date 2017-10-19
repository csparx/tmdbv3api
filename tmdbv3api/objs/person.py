from tmdbv3api.tmdb import TMDb
from tmdbv3api.as_obj import AsObj

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote


class Person(TMDb):
    URLS = {
        'details': '/person/%s',
        'search_people': '/search/person'
    }

    def details(self, id):
        """
        Get the primary person details by id.
        :param id:
        :return:
        """
        return AsObj(**self._call(self.URLS['details'] % str(id), ''))

    def search(self, term, page=1):
        """
        Search for people.
        :param term:
        :param page:
        :return:
        """
        return self._get_obj(self._call(self.URLS['search_people'], 'query=' + quote(term) + '&page=' + str(page)))