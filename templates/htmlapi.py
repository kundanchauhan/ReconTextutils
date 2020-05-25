# import requests
# url = "http://hilite.me/api?code="
# code =input("Enter your code here :")
# payload = {}
# headers = {}
# response = requests.request("GET", url+code, headers=headers, data = payload)
# pretty=response.text# print(pretty)
# foundAt=pretty.find('>')
# pretty=pretty[foundAt+1:]
# print("<!-- HTML generated using textutils -->"+pretty)



# import http.client
# import mimetypes
# import ssl
# ssl.match_hostname = lambda cert, hostname: True



# conn = http.client.HTTPSConnection("hilite.me")
# payload = ''
# headers = {}
# conn.request("GET", "/api?code=def&lexer=python", payload, headers)
# res = conn.getresponse()
# data = res.read()
# my = data.decode("utf-8")
# pretty = str(my)
# foundAt=pretty.find('>')
# pretty=pretty[foundAt+1:]
# print("<!-- HTML generated using textutils -->"+pretty)




from pylovepdf.ilovepdf import ILovePdf
ilovepdf = ILovePdf('project_public_770e56f3152d401d6476b9be1800d6c4_4byne2d937ca7d5ea33974126f444d2c1166e', verify_ssl=True)
task = ilovepdf.new_task('compress')
task.add_file('/home/kundan/Downloads/PDF/Cellular_biology/01Cell_English_1561800100_English_1577785538.pdf')
task.set_output_folder('/home/kundan/Downloads/download_pdffile')
task.execute()
task.download()
task.delete_current_task()
                               



