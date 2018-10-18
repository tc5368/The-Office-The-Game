north = 'north'
///



elevator_corridor = {
	'name'        :  'Elevators',
	'exits'       :  {'east':'reception'},
	'description' :  'You are standing at the Elevators'
}

reception = {
	'name'        : 'Reception',
	'exits'       : {'east':'main_office','north':'michaels_office'},
	'description' : 'Your standing by Reception'
}

main_office = {
	'name'        : 'Bullpen',
	'exits'       : {'north':'conference_room','east':'kitchen_area'},
	'description' : 'You are in the main Bullpen'
}

michaels_office = {
	'name'        : 'Michaels Office',
	'exits'       : {'south':'reception'},
	'description' : 'Oh god your in the Bosses Office, good luck'
}

conference_room = {
	'name'        : 'Conference Room',
	'exits'       : {'south':'main_office'},
	'description' : 'You were supposed to be in the conference room 5 minutes ago'
}

kitchen_area = {
	'name'        : 'Kitchen',
	'exits'       : {'east':'annex','west':'main_office'},
	'description' : 'Your in the Kitchen, Kevin is making Chilli'
}

annex = {
	'name'        : 'The Annex',
	'exits'       : {'north':'break_room','west':'kitchen_area'},
	'description' : 'Escape as quickly as possible! This is where Toby is...'
}

break_room = { 
	'name'        : 'The Breakroom',
	'exits'       : {'south':'break_room'},
	'description' : 'Realx in the breakroom'
}


rooms = {
	'Elevators'        :elevator_corridor,
	'Reception'        :reception,
	'Bullpen'          :main_office,
	'Michaels Office'  :michaels_office, 
	'Conference Room'  :conference_room,
	'Kitchen'          :kitchen_area,
	'The Annex'        :annex,
	'The Breakroom'    :break_room
}