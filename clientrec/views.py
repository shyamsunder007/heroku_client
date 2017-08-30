from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import urllib.request, json 

@csrf_exempt
def index(request,question_id=1):
    print (question_id)
    data={}
    context={}
    if question_id!=1:
        with urllib.request.urlopen("https://sleepy-sands-75184.herokuapp.com/all/"+question_id) as url:
            data = json.loads(url.read().decode())
            print (data)
            member_details=data.get('member_details')
            household_details=data.get('household_details')
            farm_details=data.get('farm_details')
            farm_area=data.get('farm_area')
            crop_details=data.get('crop_details')
            well_details=data.get('well_details')
            waterYield=data.get('waterYield')
            if 'member_details' in data.keys():
                context = {

            'farmer_name': member_details.get('name'),
            'farmer_gender': member_details.get('gender'),
            'farmer_age': member_details.get('age'),
            'farmer_house_lat': household_details.get('lat'),
            'farmer_house_lon': household_details.get('long'),
            'farmer_house_income': household_details.get('income'),
            'farmer_area_lat': farm_area.get('lat'),
            'farmer_area_lon': farm_area.get('long'),
            'farmer_crop': crop_details.get('crop'),
            'farmer_crop_season': crop_details.get('season'),
            'farmer_crop_area': crop_details.get('area'),
            'farmer_well_lat': well_details.get('lat'),
            'farmer_well_lon': well_details.get('long'),
            'farmer_well_depth': well_details.get('depth'),
            'farmer_well_avg_water': well_details.get('avg_water'),
            'farmer_waterdate': waterYield.get('date'),
            'farmer_wellyield': waterYield.get('water_yield'),
            'Data':'Available'
                }
            else:
                context={
                'Data':'Not Available'
                }


    template = loader.get_template('clientrec/index.html')
    
    return HttpResponse(template.render(context, request))