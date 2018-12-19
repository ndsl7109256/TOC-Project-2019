from bottle import route, run, request, abort, static_file

from fsm import TocMachine
import os

PORT = os.environ['PORT']
VERIFY_TOKEN = "1234567890987654321"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        
        'TaipeiMayor',
        
        'TaipeiRepresentative',
        'TaipeiRepresentative1',
        'TaipeiRepresentative2',
        'TaipeiRepresentative3',
        'KaohsiungRepresentative',
        'KaohsiungRepresentative1',
        'KaohsiungRepresentative2',
        'KaohsiungRepresentative3',
        'Referendum14',
        'Referendum14Agree',
        'Referendum14Oppose',
        'Referendum15',
        'Referendum15Agree',
        'Referendum15Oppose',
        'NotState'
    ],
    transitions=[
        
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'TaipeiRepresentative',
            'conditions': 'is_going_to_TaipeiRepresentative'
        },
        {
            'trigger': 'advance',
            'source': 'TaipeiRepresentative',
            'dest': 'TaipeiRepresentative1',
            'conditions': 'is_going_to_TaipeiRepresentative1'
        },
        {
            'trigger': 'advance',
            'source': 'TaipeiRepresentative',
            'dest': 'TaipeiRepresentative2',
            'conditions': 'is_going_to_TaipeiRepresentative2'
        },
        {
            'trigger': 'advance',
            'source': 'TaipeiRepresentative',
            'dest': 'TaipeiRepresentative3',
            'conditions': 'is_going_to_TaipeiRepresentative3'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'KaohsiungRepresentative',
            'conditions': 'is_going_to_KaohsiungRepresentative'
        },
        {
            'trigger': 'advance',
            'source': 'KaohsiungRepresentative',
            'dest': 'KaohsiungRepresentative1',
            'conditions': 'is_going_to_KaohsiungRepresentative1'
        },
        {
            'trigger': 'advance',
            'source': 'KaohsiungRepresentative',
            'dest': 'KaohsiungRepresentative2',
            'conditions': 'is_going_to_KaohsiungRepresentative2'
        },
        {
            'trigger': 'advance',
            'source': 'KaohsiungRepresentative',
            'dest': 'KaohsiungRepresentative3',
            'conditions': 'is_going_to_KaohsiungRepresentative3'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'TaipeiMayor',
            'conditions': 'is_going_to_TaipeiMayor'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'Referendum14',
            'conditions': 'is_going_to_Referendum14'
        },
        {
            'trigger': 'advance',
            'source': 'Referendum14',
            'dest': 'Referendum14Agree',
            'conditions': 'is_going_to_Referendum14Agree'
        },
        {
            'trigger': 'advance',
            'source': 'Referendum14',
            'dest': 'Referendum14Oppose',
            'conditions': 'is_going_to_Referendum14Oppose'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'Referendum15',
            'conditions': 'is_going_to_Referendum15'
        },
        {
            'trigger': 'advance',
            'source': 'Referendum15',
            'dest': 'Referendum15Agree',
            'conditions': 'is_going_to_Referendum15Agree'
        },
        {
            'trigger': 'advance',
            'source': 'Referendum15',
            'dest': 'Referendum15Oppose',
            'conditions': 'is_going_to_Referendum15Oppose'
        },
        {
            'trigger': 'go_back',
            'source': [
                'TaipeiMayor',
                'KaohsiungRepresentative1',
                'KaohsiungRepresentative2',
                'KaohsiungRepresentative3',
                'TaipeiRepresentative1',
                'TaipeiRepresentative2',
                'TaipeiRepresentative3',
                'Referendum14Agree',
                'Referendum14Oppose',
                'Referendum15Agree',
                'Referendum15Oppose'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    print('teset')
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
