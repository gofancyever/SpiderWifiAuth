
import os
DEBUG = True
# BCRYPT_LEVEL = 13 # 配置Flask-Bcrypt拓展
# MAIL_FROM_EMAIL = "robert@example.com" # 设置邮件来源

UPLOADED_PHOTOS_DEST = os.getcwd() + '/tmp/images'
UPLOADED_PHOTO_ALLOW = 'IMAGES'