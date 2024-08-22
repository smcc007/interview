import requests
import json


def nfl_test():
    base_url = " https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes"

    parameters = {
    'limit': 5,
    }

    response = requests.get(base_url, params= parameters)

    player_dict = {}
    if response.status_code == 200:  # Code is okay
        json_rsp = response.json()
        for item in json_rsp['items']:
            player_response = requests.get(item['$ref']).json()
            player_dict[player_response['id']] = player_response
        
        print("stop here")
    else:
        print("bad request")

    player_dict['3728305']['age'] = 99

    #player_dict.pop('4035487')

    file_name = "./player_roster.txt"

    with open(file_name, 'wb') as file:
        file.write(json(player_dict))



    return response

if __name__ == "__main__":
   print(nfl_test())