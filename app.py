from flask import Flask,jsonify,request
import json
import statistics

with open("data.json", "r") as read_file:
	data = json.load(read_file)

app = Flask(__name__)

#### 'home' endpoint - contains the whole JSON data ####
@app.route('/')
def home():
	print(data)
	return jsonify(data)

################################################
#
#	"get index" endpoint
#	input : list of counties
#	output : index values of the list of given counties
#
################################################
@app.route('/happiness')
def get_happiness():
	county_list = request.args.getlist('county')
	if not county_list:
		print("{'message' : 'No county value was received' }")
		return jsonify({'message' : 'No county value was received' })

	new_data = {}
	for c in county_list:
		if c in data:
			new_data[c] = data[c]
		else:
			print("{'message' : 'county not found'}")
			return jsonify({'message' : 'county not found'})

	print(new_data)
	return jsonify(new_data)

################################################
#
#	"get average" endpoint
#	input : list of counties
#	output : average index value of the list of given counties
#
################################################
@app.route('/happiness/average')
def get_average():
	county_list = request.args.getlist('county')
	if not county_list:
		print("{'message' : 'No county value was received' }")
		return jsonify({'message' : 'No county value was received' })
	val = 0
	num = 0
	for c in county_list:
		if c not in data:
			print("{'message' : 'county not found'}")
			return jsonify({'message' : 'county not found'})
		val += data[c]
		num += 1

	if num > 0:
		val = val / num
		new_data = {
			'average' : val
		}
		print(new_data)
		return jsonify(new_data)
	else:
		print("{'message' : 'county not found'}")
		return jsonify({'message' : 'county not found'})

################################################
#
#	"get median" endpoint
#	input : list of counties
#	output : median index value of the list of given counties
#
################################################
@app.route('/happiness/median')
def get_median():
	county_list = request.args.getlist('county')
	#### if no county value was received, emit error ####
	if not county_list:
		print("{'message' : 'No county value was received' }")
		return jsonify({'message' : 'No county value was received' })

	val_list = []
	for c in county_list:
		if c not in data:
			print("{'message' : 'county not found' }")
			return jsonify({'message' : 'county not found'})
		val_list.append(data[c])

	val_list.sort()
	length = len(val_list)
	if length == 0:
		print("{'message' : 'No county value was received' }")
		return jsonify({'message' : 'No county value was received' })

	if length % 2 == 0:
		med = (val_list[int((length-1)/2)] + val_list[int((length+1)/2)]) / 2.0
		new_data = {
			'median' : med
		}
		print(new_data)
		return jsonify(new_data)
	else:
		med = val_list[int(length/2)]
		new_data = {
			'median' : med
		}
		print(new_data)
		return jsonify(new_data)

################################################
#
#	"get counties in range" endpoint
#	input : range of index value
#	output : list of counties with index that is 
#			within the given range
#
################################################
@app.route('/happiness/range')
def get_county_in_range():
	index_startRange = request.args.get('from',None)
	index_endRange = request.args.get('to',None)
	#### if no start/end range was received, emit error ####
	if index_startRange == None or index_endRange == None \
	or not index_startRange or not index_endRange:
		print("{'message' : 'Invalid Range' }")
		return jsonify({'message' : 'Invalid Range' })

	index_startRange, index_endRange = float(index_startRange), float(index_endRange)
	#### if end range value is less than start, swap ####
	if index_endRange < index_startRange:
		index_startRange, index_endRange = index_endRange, index_startRange

	new_data = {}
	for d in data:
		if index_startRange <= data[d] <= index_endRange:
			new_data[d] = data[d]

	#### if new dictionary is empty, emit error ####
	if not new_data:
		print("{'message' : 'No county found within the given index range' }")
		return jsonify({'message' : 'No county found within the given index range' })

	print(new_data)
	return jsonify(new_data)

################################################
#
#	"get standard deviation in range" endpoint
#	input : range of county value
#	output : standard deviation of the list of counties 
#			that are within the given county range
#
################################################
@app.route('/happiness/stdev')
def get_stdev():
	county_startRange = request.args.get('from',None)
	county_endRange = request.args.get('to',None)
	#### if no start/end range was received, emit error ####
	if county_startRange == None or county_endRange == None \
	or not county_endRange or not county_startRange:
		print("{'message' : 'Invalid Range' }")
		return jsonify({'message' : 'Invalid Range' })

	county_startRange, county_endRange = float(county_startRange), float(county_endRange)
	#### if end range value is less than start, swap ####
	if county_endRange < county_startRange: 
		county_startRange, county_endRange = county_endRange, county_startRange

	new_data = {}
	val_list = []
	for d in data:
		county = float(d)
		if county_startRange <= county <= county_endRange:
			new_data[d] = data[d]
			val_list.append(data[d])

	#### if new dictionary is empty, emit error ####
	if not new_data:
		print("{'message' : 'No county found within the given county range' }")
		return jsonify({'message' : 'No county found within the given county range' })

	val_list.sort()
	new_data.update( {'stdev' : statistics.stdev(val_list) })

	print(new_data)
	return jsonify(new_data)


app.run()


















