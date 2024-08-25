import requests
import json


class NFLRoster:
    """An interface to pull and minupulate football player data from ESPN api
    
    Attributes
    __________
    player_dict: dict
        a dictionary that contains the player information that is pulled from ESPN API on instantiation

    Methods
    _________
    set_age(key, age):
        overwrite the players age in player_dict for a given key

    delete_player(key):
        remove a player from the player_dict for a given key
    
    
    write_roster():
        write player_dict to a file ./player_roster.txt
    """
    
    #class attributes
    base_url = " https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes"

    def __init__(self, x:int=5):
        """
            Parameters
            ----------
            x: int. optional
                total number of players to fetch from ESPN API, if not provided defaults to 5
        """
        
        if x > 1 :
            parameters = {'limit': x,}

            response = requests.get(type(self).base_url, params= parameters)

            if response.status_code == 200:  # Code is okay
                self.player_dict = {}
                json_rsp = response.json()
                for item in json_rsp['items']:
                    player_response = requests.get(item['$ref']).json()
                    self.player_dict[player_response['id']] = player_response  #To Doreview this data model
            else: 
                raise RuntimeError("API call failed")

        else:
            raise ValueError("x must be greater than 0 to run")


      
    def set_age(self,key, age):
        try:
            self.player_dict[key]['age'] = age
        except KeyError:
            print(f"The key: {key}, is not found in the dictionary, the age has not been udpated")

    def delete_player(self, key):
        try:
            self.player_dict.pop(key)
        except KeyError:
            print(f"The key: {key}, is not found in the dictionary, nothing has been deleted")

    def print_roster(self):
        for items in self.player_dict:
            print(items)
        
    def write_roster(self):
        file_name = "./player_roster.json"

        with open(file_name, 'w', encoding="utf-8")  as file:
            json.dump(self.player_dict, file)
        

    
    
if __name__ == "__main__":
    roster = NFLRoster(7)
    print("stop here")
    player_id_list = list(roster.player_dict.keys())
    roster.set_age(player_id_list[4], 99)  #To Do: Array index out of bound?
    
    roster.delete_player(player_id_list[0]) #To Do: Array index out of bound?
    roster.write_roster()
    print("next stop")