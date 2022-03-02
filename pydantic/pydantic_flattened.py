import typing as T
from scalpl import Cut
from pydantic import BaseModel, Field
from pydantic.utils import GetterDict


class ProxyGetterDict(GetterDict):
    def __getitem__(self, key: str) -> T.Any:
        try:
            return self._obj.get(key)
        except AttributeError as e:
            raise KeyError(key) from e
            
    def get(self, key: T.Any, default: T.Any = None) -> T.Any:
        return self._obj.get(key, default)


class Person(BaseModel):
    id: int
    name: str
    friend: str
    some_dict: dict = Field(alias='some_dictek')
    wiek: int = Field(alias='dupa.Wieku')

    class Config:
        orm_mode = True
        getter_dict = ProxyGetterDict


response_json = {
    'id': '7',
    'name': 'John',
    'friend': 'Maila',
    'some_dictek': {'a': 1, 'b': 2},
    'dupa': {
        'Wieku': 9
    }
}


proxy = Cut(response_json)
person = Person.from_orm(proxy)


print(person.id)
print(person.name)
print(person.friend)
print(person.some_dict)
