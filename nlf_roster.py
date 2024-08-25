import requests
import json


class NFLRoster:
    
    #class attributes
    base_url = " https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes"

    def __init__(self, x:int):
        
        parameters = {'limit': x,}

        response = requests.get(type(self).base_url, params= parameters)

        self.player_dict = {}
        if response.status_code == 200:  # Code is okay
            json_rsp = response.json()
            for item in json_rsp['items']:
                player_response = requests.get(item['$ref']).json()
                self.player_dict[player_response['id']] = player_response  #review this data model
        else: #TO DO: try a different assertion or key value error response.
            print("bad request")

      
    def set_age(self,key, age):
        self.player_dict[key]['age'] = age

    def delete_player(self, key):
        self.player_dict.pop(key)

    def print_roster(self):
        for items in self.player_dict:
            print(items)
        
    def write_roster(self, file_name: str):
        file_name = "./player_roster.txt"

        with open(file_name, 'wb')  as file:
            file.write(json(player_dict))

    
    
if __name__ == "__main__":
    roster = NFLRoster(6)
    print("stop here")