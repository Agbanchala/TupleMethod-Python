nested_dict = {
    "MobileDev": {
        "Student1": "Amaka Disappoint",
        "Student2": "Nedu Japan",
        "Student3": "Pretty Cynthia",
        "Score": {
            "Student1": 65,
            "Student2": 98,
            "Student3": 74
        }
    },
    "DataTrack": {
        "StudentA": "Jon Bellion",
        "StudentB": "Jon Bellcat",
        "StudentC": "Jon Doe",
        "Score": {
            "StudentA": 123,
            "StudentB": 145,
            "StudentC": 100
        }
    },
    "DesignTrack": {
        "Tag1": "Ada Ada",
        "Tag2": "Phyno Ezege",
        "Tag3": "Dog Catcher",
        "Tag4": "Bitrus Beetroot",
        "Tag5": "Doja Cat",
        "Tag6": "Beja Rat"
        "Score": {
            "Tag1": 79,
            "Tag2": 87,
            "Tag3": 91,
            "Tag4": 114,
            "Tag5": 90,
            "Tag6": 91
        }
    }
}

MobileDev = {
    'Amaka Disappiont': 65,
     'Nedu Japan': 98,
      'Pretty Cynthia': 74
}
maximum_score = max(MobileDev.values())
maximum_score_names = [ name for name, score in MobileDev.items() if score == maximum_score]
print(" The maximum score is", maximum_score, "and it was achieved by", ', '.join(maximum_score_names)) 

DataTrack = {
    'Jon Bellion': 123,
     'Jon Bellcat': 145,
      'Jon Doe': 100
}
maximum_score = max(DataTrack.values())
maximum_score_names = [ name for name, score in DataTrack.items() if score == maximum_score]
print(" The maximum score is", maximum_score, "and it was achieved by", ', '.join(maximum_score_names)) 


DesignTrack = {
    'Ada Ada': 79,
     'Phyno Ezege': 87,
     'Dog Catcher': 91,
     'Bitrus Beetroot': 114,
     'Doja Cat': 90,
      'Beja Rat': 91
}
maximum_score = max(DesignTrack.values())
maximum_score_names = [ name for name, score in DesignTrack.items() if score == maximum_score]
print(" The maximum score is", maximum_score, "and it was achieved by", ', '.join(maximum_score_names)) 



