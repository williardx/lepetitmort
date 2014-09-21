"""
Options for Messages. Each one looks like:
{type:<'death'|'life'|...>, body:'The world is a teapot and you are the tea.'}
"""

ty_enum = {'death':0, 'hope':1, 'intro':2}
d = ty_enum.get('death')
h = ty_enum.get('hope')
i = ty_enum.get('intro')

options = [
    {'type':i, 'body':"Hi there. We're so glad to send you hints of hope. We don't send them every day, more like every one to two weeks. And if at any time you decide you no longer need hope, send HOPE to this number and we'll promptly stop delivering them to your doorstep."},
    {'type':d, 'body':'Remember that you are going to die.'},
    {'type':d, 'body':'Death is the destination we all share.'},
    {'type':d, 'body':'Death is very likely the single best invention of life. It clears out the old to make way for the new.'},
    {'type':d, 'body':'Let everything fall away in the face of death. Leave only what is truly important.'},
    {'type':d, 'body':'Let us beware of saying that death is the opposite of life. The living being is only a species of the dead, and a very rare species.'},
    {'type':d, 'body':'All that you see will soon perish; those who witness this perishing will soon perish themselves. Die in extreme old age or die before your time - it will all be the same.'},
    {'type':d, 'body':'Whenever someone tells me he dreamed, I wonder if he realizes that he has never done anything but dream.'},
    {'type':d, 'body':'Regardless, the outcome is the same: we are all going to die.'},
    {'type':d, 'body':"This is your life and it's ending one moment at a time."},
    {'type':d, 'body':'You are the music while the music lasts.'},
    {'type':h, 'body':'You are the master of your fate, the captain of your soul.'},
    {'type':h, 'body':'Dare to name the sky your own.'},
    {'type':h, 'body':"For you the flag is flung, for you the bugle trills. For you bouquets and ribbon'd wreaths, for you the shores a-crowding."},
    {'type':h, 'body':'So we beat on, boats against the current, borne back ceaselessly into the past.'},
    {'type':h, 'body':"That is part of the beauty of all literature. You discover that your longings are universal longings, that you're not lonely and isolated from anyone. You belong."},
    {'type':h, 'body':'Let us learn to show our friendship for a man when he is alive and not after he is dead.'}
    ]
