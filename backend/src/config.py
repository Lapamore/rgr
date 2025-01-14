from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Обновляем пути для статических файлов и медиа
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Убираем неиспользуемые пути
# TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
# STATIC_DIR = os.path.join(BASE_DIR, "static")
# ... 