import os
from modelscope.hub.snapshot_download import snapshot_download

# ��������ģ��Ŀ¼
os.system("mkdir /root/models")

# save_dir��ģ�ͱ��浽���ص�Ŀ¼
save_dir="/root/models"

snapshot_download("Shanghai_AI_Laboratory/internlm2-chat-1_8b",
                  cache_dir=save_dir,
                  revision='v1.1.0')
