from model.services.themoviedb_service.media_type import MediaType


class Person:
    def __init__(self, person_id, name, profile_path=None, url=None, thumb_url=None, poster_url=None, known_for=None):
        self.id: int = person_id
        self.name: str = name
        self.profile_path: str = profile_path
        self.url: str = url
        self.thumb_url: str = thumb_url
        self.poster_url: str = poster_url
        self.known_for = known_for
        self.media_type = MediaType.PERSON

    @classmethod
    def from_dict(cls, person_dict: dict):
        return cls(
            person_id=person_dict['id'],
            name=person_dict['name'],
            profile_path=person_dict['profile_path'] if 'profile_path' in person_dict else None,
            url=person_dict['url'] if 'url' in person_dict else None,
            thumb_url=person_dict['thumb_url'] if 'thumb_url' in person_dict else None,
            poster_url=person_dict['poster_url'] if 'poster_url' in person_dict else None,
            known_for=person_dict['known_for'] if 'known_for' in person_dict else None
        )
