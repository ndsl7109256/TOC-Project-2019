from bottle import route, run, request, abort, static_file

from fsm import TocMachine



VERIFY_TOKEN = "1234567890987654321"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        
        'TaipeiMayor',
        'KaohsiungMayor',
        'TaipeiRepresentative',
        'TaipeiRepresentative1',
        'TaipeiRepresentative2',
        'TaipeiRepresentative3',
        'KaohsiungRepresentative',
        'KaohsiungRepresentative1',
        'KaohsiungRepresentative2',
        'KaohsiungRepresentative3'
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
            'source': 'state1',
            'dest': 'KaohsiungMayor',
            'conditions': 'is_going_to_KaohsiungMayor'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'go_back',
            'source': [
                'KaohsiungMayor',
                'TaipeiMayor',
                'KaohsiungRepresentative1',
                'KaohsiungRepresentative2',
                'KaohsiungRepresentative3',
                'TaipeiRepresentative1',
                'TaipeiRepresentative2',
                'TaipeiRepresentative3',
                'state3'
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
    run(host="localhost", port=5000, debug=True, reloader=True)
