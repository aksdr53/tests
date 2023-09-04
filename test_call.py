import neurovoicelibrary as nv
import neuronetlibrary as nn


def hello_main():
    nv.say('hello')
    nn.log('Проигрывается промпт hello')
    with nv.listen(
        ('wrong_time, repeat', 500, 'OR'),
        entities=['confirm', 'wrong_time', 'repeat'],
        no_input_timeout=4000,
        recognition_timeout=60000,
        speech_complete_timeout=1500,
    ) as r:
        r.utterance()
        r.entities()
        if r.has_entities:
            if r.entity('wrong_time'):
                hangup_wrong_time()
                return
            if r.entity('repeat'):
                nn.log('Абонент просит повторить')
                hello_repeat()
                return
            if r.entity('confirm') is not None:
                if r.entity('confirm'):
                    recommend_main()
                    return
                else:
                    hangup_wrong_time()
                    return
            recommend_main()
        else:
            nn.log('Абонент молчит')
            hello_null() 
        return


def hello_repeat():
    nv.say('hello_repeat')
    nn.log('Проигрывается промпт hello_repeat')
    with nv.listen(
        ('wrong_time, repeat', 500, 'OR'),
        entities=['confirm', 'wrong_time', 'repeat'],
        no_input_timeout=4000,
        recognition_timeout=60000,
        speech_complete_timeout=1500,
    ) as r:
        r.utterance()
        r.entities()
        if r.has_entities:
            if r.entity('wrong_time'):
                hangup_wrong_time()
                return
            if r.entity('repeat'):
                nn.log('Абонент просит повторить')
                hello_repeat()
                return
            if r.entity('confirm') is not None:
                if r.entity('confirm'):
                    recommend_main()
                    return
                else:
                    hangup_wrong_time()
                    return
            recommend_main()
        else:
            nn.log('Абонент молчит')
            hello_null() 
        return


def hello_null():
    nv.say('hello_null')
    nn.log('Проигрывается промпт hello_null')
    with nv.listen(
        ('wrong_time, repeat', 500, 'OR'),
        entities=['confirm', 'wrong_time', 'repeat'],
        no_input_timeout=4000,
        recognition_timeout=60000,
        speech_complete_timeout=1500,
    ) as r:
        r.utterance()
        r.entities()
        if r.has_entities:
            if r.entity('wrong_time'):
                hangup_wrong_time()
                return
            if r.entity('repeat'):
                nn.log('Абонент просит повторить')
                hello_repeat()
                return
            if r.entity('confirm') is not None:
                if r.entity('confirm'):
                    recommend_main()
                    return
                else:
                    hangup_wrong_time()
                    return
            recommend_main()
        else:
            nn.log('Абонент молчит')
            hangup_null() 
        return


nn.call(msisdn='1234567890',
        entry_point='hello_logic', on_success_call='after_call_success',
        on_failed_call='after_call_failed',
        on_failed_call_system='after_call_failed')
