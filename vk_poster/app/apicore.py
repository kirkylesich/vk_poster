import vk_api
import settings


class VkPoster:

    def __init__(self):
        vk_session = vk_api.VkApi(settings.LOGIN, settings.PASSWORD)
        vk_session.auth()
        self.vk = vk_session.get_api()

    def make_post(self, text):
        self.vk.wall.post(owner_id=settings.GROUP_ID, from_group=1, message=text)


