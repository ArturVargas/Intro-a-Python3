
#Hacer peticiones desde python
import urllib.request, json

def main():
  url = "https://jsonplaceholder.typicode.com/posts"
  data = urllib.request.urlopen(url).read()
  jsonData = json.loads(data.decode("utf-8"))
  print(jsonData)

if __name__ == '__main__':main()