import requests, json, sys
from dewiki import parser

def ft_parse_wiki(str_to_search):
	r = requests.get("https://en.wikipedia.org/w/api.php?action=query&titles=" + str_to_search + "&prop=revisions&rvprop=content&format=json")
	if r.status_code != 200:
		raise Exception("Error occured!")
	data = r.json()
	# print (data['query']['pages'])
	
	# print (name)

if __name__ == '__main__':
	try:
		if len(sys.argv) != 2:
			raise Exception("Error! One argument need to be passed")
		ft_parse_wiki(sys.argv[1])
	except Exception as e:
		print (e)