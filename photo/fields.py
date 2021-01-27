import os
from PIL import Image # 이미지 처리 라이브러리 (pillow)
from django.db.models.fields.files import ImageField, ImageFieldFile


# 커스텀 필드는, 기존의 비슷한 필드를 상속받아 작성하는 것이 보통.
# 이미지 커스텀 필드는, ImageField 클래스를 상속받아 작성.
# 이미지 필드는, 시스템에 파일을 읽고 쓰는 작업이 필요하여, ImageFieldFile 클래스가 필요함
# ImageField와 ImageFieldFile 필드를 연계시켜주는 코드도 필요

# 파일 시스템에 이미지를 직접 쓰고 지우는 작업을 하는 클래스
class ThumbnailImageFieldFile(ImageFieldFile):
    # 썸네일 이미지 파일명 생성
    def _add_thumb(self, s):
        parts = s.split('.')
        parts.insert(-1, 'thumb')
        if parts[-1].lower() not in ['jpeg', 'jpg']:
            parts[-1] = 'jpg'
        return '.'.join(parts)

    # 썸네일의 path를 만들어 줌
    # @property는, 메소드를 속성처럼 사용할 수 있도록 해주는 데코레이터
    @property
    def thumb_path(self):
        return self._add_thumb(self.path)

    # 썸네일의 url을 만들어 줌
    @property
    def thumb_url(self):
        return self._add_thumb(self.url)

    # 파일 시스템에 파일을 저장하고 생성하는 메소드
    def save(self, name, content, save=True):
        # 원본이미지 저장
        super().save(name, content, save)
        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        # PIL의 image.thumbnail 을 이용하여, 썸네일 생성
        img.thumbnail(size)
        # 백그라운드 이미지 생성
        background = Image.new('RGB', size, (255, 255, 255))
        box = (int((size[0] - img.size[0])/2), int((size[1] - img.size[1])/2))
        # 썸네일과 백그라운드 이미지를 합쳐서 정사각형의 썸네일 이미지 생성
        background.paste(img, box)
        # 합쳐진 최종 이미지를 thumb_path에 저장
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField):
    # 새로운 파일필드를 정의 할 때는, 그에 상응하는 File처리 클래스를 attr_class 에 지정하는 것이 필수.
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)

