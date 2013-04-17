from django.core.cache import get_cache
from django.conf import settings

from sorl.thumbnail.kvstores.base import KVStoreBase

SORL_CACHE = getattr(settings, 'SORL_CACHE', 'default')

class KVStore (KVStoreBase):
  def __init__ (self, *args, **kwargs):
    super(KVStore, self).__init__(*args, **kwargs)
    self.connection = get_cache(SORL_CACHE)
    
  def _get_raw (self, key):
    return self.connection.get(key)
    
  def _set_raw (self, key, value):
    return self.connection.set(key, value)
    
  def _delete_raw (self, *keys):
    return self.connection.delete_many(*keys)
    
  def _find_keys_raw (self, prefix):
    #pattern = prefix + '*'
    #return self.connection.keys(pattern=pattern)
    raise NotImplementedError('Not supported in memcache, just flush your cache.')
    