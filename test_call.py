import neurovoicelibrary as nv


def hello_logic():
    nv.say('hello')
    with nv.listen(
        ('wrong_time, repeat', 500, 'OR'),
        entities=['confirm', 'wrong_time', 'repeat'],
        no_input_timeout=4000,
        recognition_timeout=60000,
        speech_complete_timeout=1500,
    ) as r:
        r.utterance()
        r.entities()
