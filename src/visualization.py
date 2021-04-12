def player_choice():
    """
    Ask the user to choose a player, then we'll check if the player has been in the NBA between 1996-2021. 
    If has been, we'll create a plot when we'll ask the user again to choose an stat. The result will be a line plot during the years.

    """
    
    election = input(f"Choose your player: ")
    if election in list(nba_dataset["PLAYER_NAME"]):
        player = nba_dataset[nba_dataset["PLAYER_NAME"] == election]
        plt.figure(figsize=(16,8))
        sns.lineplot(data = player, x = "SEASON", y = input(f"Choose your stat: "), markers = True, dashes = False)
        plt.tight_layout()
        plt.show()
        return plt.show
    else:
        return election



def zion_effect():
    """
    In this function, we filter the dataframe by the columns PTS, AGE, GP, REB and TS_PCT to obtain the only players with awesome stats.

    """

    zion_effect = nba_dataset.loc[(nba_dataset["PTS"] >= 25) & (nba_dataset["AGE"] < 26) & 
                (nba_dataset["GP"] >= 30) & (nba_dataset["REB"] >= 6) & 
                (nba_dataset["TS_PCT"] >= 0.60)]
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=zion_effect, x="SEASON", y="AGE", hue="PLAYER_NAME")       
    plt.tight_layout()
    plt.show()
    return plt.show()
