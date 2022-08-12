import pandas as pd

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


upload_file_list = ['comment_202002.csv', 'post_201912.csv']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1dZXmRPPr6Z8C9OqixmLxW-pcMIW4p7FA'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.