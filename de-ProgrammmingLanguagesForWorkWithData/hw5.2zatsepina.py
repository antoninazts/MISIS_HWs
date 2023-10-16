class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        self.order_list = []

    @property
    def cache(self):
        if not self.order_list:
            return None
        key_to_get = self.order_list[-1]
        return key_to_get, self.cache_dict[key_to_get]

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            self.order_list.remove(key)
            del self.cache_dict[key]
        if len(self.cache_dict) >= self.capacity:
            oldest_key = self.order_list.pop(0)
            del self.cache_dict[oldest_key]
        self.cache_dict[key] = value
        self.order_list.append(key)

    def get(self, key):
        if key in self.cache_dict:
            self.order_list.remove(key)
            self.order_list.append(key)
            return self.cache_dict[key]
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key in self.order_list:
            print(f"{key} : {self.cache_dict[key]}")



# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)


# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")


# # Выводим текущий кэш
cache.print_cache() # key1 : value1, key2 : value2, key3 : value3


# Получаем значение по ключу
print(cache.get("key2")) # value2


# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")


# Выводим обновлённый кэш
cache.print_cache() # key2 : value2, key3 : value3, key4 : value4