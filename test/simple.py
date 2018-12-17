from pygraphviz import *
import pygraphviz as pgv

A=pgv.AGraph(strict=False,directed=True)


A.add_node('user')

A.add_node('Representative')
A.add_node('TaipeiRepresentative')
A.add_node('TaipeiRepresentative1')
A.add_node('TaipeiRepresentative2')
A.add_node('TaipeiRepresentative3')
A.add_node('KaohsiungRepresentative')
A.add_node('KaohsiungRepresentative1')
A.add_node('KaohsiungRepresentative2')
A.add_node('KaohsiungRepresentative3')

A.add_node('Mayor')
A.add_node('TaipeiMayor')
A.add_node('KaohsiungMayor')

A.add_node('Referendum')
A.add_node('Referendum14')
A.add_node('Referendum14Agree')
A.add_node('Referendum14Oppose')
A.add_node('NotState')


A.add_edge('user','Representative',label = 'Advance [is_going_to_Representative]')
A.add_edge('user','Mayor',label = 'Advance [is_going_to_Mayor')
A.add_edge('user','Referendum',label = 'Advance [is_going_to_Referendum')

A.add_edge('Representative','TaipeiRepresentative',label = 'Advance [is_going_to_TaipeiRepresentative]')

A.add_edge('TaipeiRepresentative','TaipeiRepresentative1',label = 'Advance [is_going_to_TaipeiRepresentative1]')
A.add_edge('TaipeiRepresentative1','user',label = 'go_back',color = 'red')
A.add_edge('TaipeiRepresentative','TaipeiRepresentative2',label = 'Advance [is_going_to_TaipeiRepresentative2]')
A.add_edge('TaipeiRepresentative2','user',label = 'go_back',color = 'red')
A.add_edge('TaipeiRepresentative','TaipeiRepresentative3',label = 'Advance [is_going_to_TaipeiRepresentative3]')
A.add_edge('TaipeiRepresentative3','user',label = 'go_back',color = 'red')


A.add_edge('Representative','KaohsiungRepresentative',label = 'Advance [is_going_to_KaohsiungRepresentative]')
A.add_edge('KaohsiungRepresentative','KaohsiungRepresentative1',label = 'Advance [is_going_to_KaohsiungRepresentative1]')
A.add_edge('KaohsiungRepresentative1','user',label = 'go_back',color = 'red')
A.add_edge('KaohsiungRepresentative','KaohsiungRepresentative2',label = 'Advance [is_going_to_KaohsiungRepresentative2]')
A.add_edge('KaohsiungRepresentative2','user',label = 'go_back',color = 'red')
A.add_edge('KaohsiungRepresentative','KaohsiungRepresentative3',label = 'Advance [is_going_to_KaohsiungRepresentative3]')
A.add_edge('KaohsiungRepresentative3','user',label = 'go_back',color = 'red')

A.add_edge('Mayor','TaipeiMayor',label = 'Advance [is_going_to_TaipeiMayor]')
A.add_edge('TaipeiMayor','user',label = 'go_back',color = 'red')
A.add_edge('Mayor','KaohsiungMayor',label = 'Advance [is_going_to_KaohsiungMayor]')
A.add_edge('KaohsiungMayor','user',label = 'go_back',color = 'red')


A.add_edge('Referendum','Referendum14',label = 'Advance [is_going_to_Referendum14]')

A.add_edge('Referendum14','Referendum14Agree',label = 'Advance [is_going_to_Referendum14Agree]')
A.add_edge('Referendum14Agree','user',label = 'go_back',color = 'red')
A.add_edge('Referendum14','Referendum14Oppose',label = 'Advance [is_going_to_Referendum14Oppose]')
A.add_edge('Referendum14Oppose','user',label = 'go_back',color = 'red')
A.add_edge('Referendum14','NotState',label = 'Advance [is_going_to_NotState]')
A.add_edge('NotState','user',label = 'go_back',color = 'red')


A.node_attr['shape'] = 'circle'
A.edge_attr['color']='black'
A.edge_attr['arrowType']='normal'
A.edge_attr['dirType'] = 'forward'


A.layout(prog='dot')
A.draw('simple.png') # draw png
print("Wrote simple.png")
