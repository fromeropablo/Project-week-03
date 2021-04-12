def scrapping():
    url = "https://www.acb.com/club/estadisticas/id/"
    headers = res.findAll("thead")[0].findAll("tr")[1].text.replace("\n", ",").split(",")
    headers = ['NADA','PLAYER_NAME', 'GP','MIN/G','5i','PPG','3FGM','3FGA','3FG%','2FGM','2FGA','2FG%','FTM','FTA','FT%',
           'DREB','OREB','TREB','ASIST','ST','TO','BLK','RBLK','DUNKS','PF','RPF','+/-','VAL']

    stats_list = []
    for year in range(2000, 2021):
        for team in range(1,20):
            html = requests.get(url+"{}".format(team)+"/temporada_id/"+"{}".format(year))
            res = BeautifulSoup(html.content,"html.parser")
            table = res.find("tbody")
            rows = table.findAll("tr")
            for r in rows:
                elements = r.findAll("td")
                jugador = [e.getText().strip() for e in elements]
                stats_list.append(jugador)  

            return stats_list



    def acb_data(stats_list):
        acb_dataset = pd.DataFrame(stats_list, columns = headers)
        index = acb_dataset[acb_dataset["PLAYER_NAME"] == "Totales"].index
        acb_dataset.drop(index, inplace=True)

        return acb_dataset     