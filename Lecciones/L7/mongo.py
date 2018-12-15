import pymongo

data = [{'url': '/m/black_panther_2018', 'name': 'Black Panther', 'Rating': 'PG-13 (for prolonged sequences of action violence, and a brief rude gesture)', 'Genre': ['Action & Adventure', 'Drama', 'Science Fiction & Fantasy'], 'Directed By': 'Ryan Coogler', 'Written By': ['Joe Robert Cole', 'Ryan Coogler'], 'In Theaters': 'Feb 16, 2018\xa0wide', 'On Disc/Streaming': 'May 15, 2018', 'Box Office': '$501,105,037', 'Runtime': '135 minutes', 'Studio': 'Marvel Studios', 'Rotten Tomatoes Score': '97%', 'Audience Score': '79%'}, {'url': '/m/mission_impossible_fallout', 'name': 'Mission: Impossible - Fallout', 'Rating': 'PG-13 (for violence and intense sequences of action, and for brief strong language)', 'Genre': ['Action & Adventure', 'Drama', 'Mystery & Suspense'], 'Directed By': 'Christopher McQuarrie', 'Written By': ['Christopher McQuarrie'], 'In Theaters': 'Jul 27, 2018\xa0wide', 'On Disc/Streaming': 'Dec 4, 2018', 'Runtime': '147 minutes', 'Studio': 'Paramount Pictures', 'Rotten Tomatoes Score': '97%', 'Audience Score': '89%'}, {'url': '/m/blackkklansman', 'name': 'BlacKkKlansman', 'Rating': 'R (for language throughout, including racial epithets, and for disturbing/violent material and some sexual references)', 'Genre': ['Comedy', 'Drama'], 'Directed By': 'Spike Lee', 'Written By': ['Charlie Wachtel', 'David Rabinowitz', 'Kevin Willmott', 'Spike Lee'], 'In Theaters': 'Aug 10, 2018\xa0wide', 'On Disc/Streaming': 'Nov 6, 2018', 'Runtime': '135 minutes', 'Studio': 'Focus Features', 'Rotten Tomatoes Score': '95%', 'Audience Score': '81%'}, {'url': '/m/a_star_is_born_2018', 'name': 'A Star Is Born', 'Rating': 'R (for language throughout, some sexuality/nudity and substance abuse)', 'Genre': ['Drama'], 'Directed By': 'Bradley Cooper', 'Written By': ['Will Fetters', 'Eric Roth', 'Bradley Cooper'], 'In Theaters': 'Oct 5, 2018\xa0wide', 'Runtime': '135 minutes', 'Studio': 'Warner Bros. Pictures', 'Rotten Tomatoes Score': '90%', 'Audience Score': '81%'}, {'url': '/m/a_quiet_place_2018', 'name': 'A Quiet Place', 'Rating': 'PG-13 (for terror and some bloody images)', 'Genre': ['Drama', 'Horror', 'Mystery & Suspense'], 'Directed By': 'John Krasinski', 'Written By': ['Bryan Woods', 'Scott Beck', 'John Krasinski'], 'In Theaters': 'Apr 6, 2018\xa0wide', 'On Disc/Streaming': 'Jul 10, 2018', 'Runtime': '90 minutes', 'Studio': 'Paramount Pictures', 'Rotten Tomatoes Score': '95%', 'Audience Score': '83%'}, {'url': '/m/paddington_2', 'name': 'Paddington 2', 'Rating': 'PG (for some action and mild rude humor)', 'Genre': ['Animation', 'Comedy', 'Kids & Family'], 'Directed By': 'Paul King (VII)', 'Written By': ['Paul King (VII)', 'Simon Farnaby'], 'In Theaters': 'Jan 12, 2018\xa0wide', 'On Disc/Streaming': 'Apr 24, 2018', 'Runtime': '105 minutes', 'Studio': 'Warner Bros. Pictures', 'Rotten Tomatoes Score': '100%', 'Audience Score': '88%'}, {'url': '/m/incredibles_2', 'name': 'Incredibles 2', 'Rating': 'PG (for action sequences and some brief mild language)', 'Genre': ['Action & Adventure', 'Animation', 'Kids & Family'], 'Directed By': 'Brad Bird', 'Written By': ['Brad Bird'], 'In Theaters': 'Jun 15, 2018\xa0wide', 'On Disc/Streaming': 'Oct 23, 2018', 'Runtime': '118 minutes', 'Studio': 'Disney/Pixar', 'Rotten Tomatoes Score': '94%', 'Audience Score': '87%'}, {'url': '/m/eighth_grade', 'name': 'Eighth Grade', 'Rating': 'R (for language and some sexual material)', 'Genre': ['Comedy'], 'Directed By': 'Bo Burnham', 'Written By': ['Bo Burnham'], 'In Theaters': 'Aug 3, 2018\xa0wide', 'On Disc/Streaming': 'Sep 25, 2018', 'Runtime': '94 minutes', 'Studio': 'A24', 'Rotten Tomatoes Score': '99%', 'Audience Score': '84%'}, {'url': '/m/leave_no_trace', 'name': 'Leave No Trace', 'Rating': 'PG (for thematic material throughout)', 'Genre': ['Drama'], 'Directed By': 'Debra Granik', 'Written By': ['Debra Granik', 'Anne Rosellini'], 'In Theaters': 'Jun 29, 2018\xa0limited', 'On Disc/Streaming': 'Sep 25, 2018', 'Runtime': '109 minutes', 'Studio': 'Bleecker Street', 'Rotten Tomatoes Score': '100%', 'Audience Score': '82%'}, {'url': '/m/call_me_by_your_name', 'name': 'Call Me by Your Name', 'Rating': 'R (for sexual content, nudity and some language)', 'Genre': ['Drama', 'Romance'], 'Directed By': 'Luca Guadagnino', 'Written By': ['James Ivory'], 'In Theaters': 'Jan 19, 2018\xa0wide', 'On Disc/Streaming': 'Mar 13, 2018', 'Runtime': '130 minutes', 'Studio': 'Sony Pictures Classics', 'Rotten Tomatoes Score': '94%', 'Audience Score': '85%'}]

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['ejemplos']
col = db['peliculas']

for x in range(0, len(data)):
    data[x]['_id'] = x
    document = col.insert_one(data[x])
    print(document)