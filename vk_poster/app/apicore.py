import vk_api
import settings
import requests
from vk_api import VkUpload


class VkPoster:

    def __init__(self):
        vk_session = vk_api.VkApi(settings.LOGIN, settings.PASSWORD)
        self.upload = VkUpload(vk_session)
        vk_session.auth()
        self.vk = vk_session.get_api()

    def make_post(self, text, file_path):
        attach = self.upload_pic(file_path)
        self.vk.wall.post(owner_id=settings.GROUP_ID, from_group=1, message=text, attachments=attach)

    def upload_pic(self, file_path):
        photos = [file_path]
        photo_list = self.upload.photo_wall(photos)
        attachment = ','.join('photo{owner_id}_{id}'.format(**item) for item in photo_list)
        return attachment

