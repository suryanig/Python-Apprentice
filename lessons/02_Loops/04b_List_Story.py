"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = []
story.append(words[0:3:2])
story.append(words[7:10:2])
story.append(words[7])
story.append(words[1])
story.append(words[14])
story.append(words[13])
story.append(words[16])
story.append(words[10])
story.append(words[8])
story.append(words[4])
story.append(words[14])
story.append(words[5])
story.append(words[7])
story.append(words[3])
story.append(words[14])
story.append(words[12])
story.append(words[10])
story.append(words[17])
story.append(words[18])

# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))