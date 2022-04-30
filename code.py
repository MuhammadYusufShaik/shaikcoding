accesstoken='sl.BGtoy9ocR4R7uutkcNPw3Kn0T5Yeu_t_6ZynQ6EK4ohx_iKhzGKC6UzPfY6Q5H5eutbsnXVRtCpNoGjd11yD6CLoNH75zLpM1ZoTaGYPLOOZY77DWiMEgSyDLMu7OPpQ7ZJCXy17wFs'
import dropbox
dbx=dropbox.Dropbox(accesstoken)
f=open('download.png','rb')
dbx.files_upload(f.read(),'/shaikCoding/download.png')