# How to find element in dictionary nested in a list:
# Data:
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    }]


for key in data:
  for i in key:
    print(i)
    print(key["name"],key['follower_count'])
    break
    
  # i => keys in the data list
  # key[value] => key["name"] = value of 'name' in the data's list
  # key[value] => key['follower_count'] = value of  'follower_count' number in the data's list
  
