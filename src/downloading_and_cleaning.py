def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded csv
    '''
    
    #Gets the name of the dataset.zip
    url = input("Introduce la url: ")
    
    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}; say -v Monica 'descargando'"
    decompress = f"tar -xzvf {endopint}.zip; say -v Monica 'descomprimiendo'"
    delete = f"rm -rf {endopint}.zip; say -v Monica 'borrando el zip'"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Gets the name of the csv (you should only have one csv when running this code)
    lista_archivos = open('archivos.txt').read()
    nueva = lista_archivos.split("\n")
    
    #Moves the .csv into the data directory
    for i in nueva:
        if i.endswith(".csv"):
            move_and_delete = f"mv {i} nba_data/dataset.csv; rm archivos.txt; say -v Monica 'moviendo el dataset'"
            return os.system(move_and_delete)



def cleaning_data():
    """
    Here we drop the first column, which is useless and rename the columns with uppercase.
    """

    data.drop(["Unnamed: 0"], axis = 1, inplace = True)
    data.columns = map(str.upper, data.columns)
    return data


#From here, we will start doing API's stuff. Enjoy!


def calling_api():
    """
    In this function, we call the API of NBA Stats thanks to the inspecting console to update our original dataset from Kaggle. The cool point here is
    that we are gonna update this dataset with info from the current season. Although is not ended yet, it's fine in order to enrich our data.  

    """

    url_bio = "https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&Season=2020-21&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true"
    }

    response_bio = requests.get(url_bio, headers=headers).json()

    return response_bio

    def updating_api(response_bio):
        """
        We just set the columns and the rows from our call and do some modifications in the resulting columns of our DataFrame. 
        """

        frame_bio = pd.DataFrame(response_bio['resultSets'][0]['rowSet'])
        frame_bio.columns = response_bio['resultSets'][0]['headers']
        frame_bio.drop(["PLAYER_ID", "TEAM_ID", "PLAYER_HEIGHT_INCHES"], axis=1, inplace=True)
        frame_bio["SEASON"] = "2020-21"

        return frame_bio

    