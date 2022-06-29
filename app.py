import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

col = ['Analytics',
 'Finance',
 'HR',
 'Legal',
 'Operations',
 'Procurement',
 'R&D',
 'Sales & Marketing',
 'Technology',
 'region_1',
 'region_10',
 'region_11',
 'region_12',
 'region_13',
 'region_14',
 'region_15',
 'region_16',
 'region_17',
 'region_18',
 'region_19',
 'region_2',
 'region_20',
 'region_21',
 'region_22',
 'region_23',
 'region_24',
 'region_25',
 'region_26',
 'region_27',
 'region_28',
 'region_29',
 'region_3',
 'region_30',
 'region_31',
 'region_32',
 'region_33',
 'region_34',
 'region_4',
 'region_5',
 'region_6',
 'region_7',
 'region_8',
 'region_9',
 "Bachelor's",
 'Below Secondary',
 "Master's & above",
 'f',
 'm',
 'other',
 'referred',
 'sourcing',
 '1',
 '2',
 '3',
 '4',
 '5',
 '6',
 '7',
 '8',
 '9',
 '20',
 '21',
 '22',
 '23',
 '24',
 '25',
 '26',
 '27',
 '28',
 '29',
 '30',
 '31',
 '32',
 '33',
 '34',
 '35',
 '36',
 '37',
 '38',
 '39',
 '40',
 '41',
 '42',
 '43',
 '44',
 '45',
 '46',
 '47',
 '48',
 '49',
 '50',
 '51',
 '52',
 '53',
 '54',
 '55',
 '56',
 '57',
 '58',
 '59',
 '60',
 '1.0',
 '2.0',
 '3.0',
 '4.0',
 '5.0',
 '1.1',
 '2.1',
 '3.1',
 '4.1',
 '5.1',
 '6.1',
 '7.1',
 '8.1',
 '9.1',
 '10',
 '11',
 '12',
 '13',
 '14',
 '15',
 '16',
 '17',
 '18',
 '19',
 '20.1',
 '21.1',
 '22.1',
 '23.1',
 '24.1',
 '25.1',
 '26.1',
 '27.1',
 '28.1',
 '29.1',
 '30.1',
 '31.1',
 '32.1',
 '33.1',
 '34.1',
 '0',
 '1.2',
 '0.1',
 '1.3',
 'avg_training_score']

def func(department,region,education,gender,recruitment,training,age,prev_rating,lservice,kpi,awards,avg_train_score):

    department_list = [0,0,0,0,0,0,0,0,0]
    department_dict = {'Analytics':0,'Finance':1,'HR':2,'Legal':3,'Operations':4,'Procurement':5,'R&D':6,'Sales & Marketing':7,'Technology':8}
    department_list[department_dict[department]] = 1

    region_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    region_dict = {'region_1':0,'region_10':1,'region_11':2,'region_12':3,'region_13':4,'region_14':5,'region_15':6,'region_16':7,'region_17':8,'region_18':9,'region_19':10,'region_2':11,'region_20':12,'region_21':13,'region_22':14,'region_23':15,'region_24':16,'region_25':17,'region_26':18,'region_27':19,'region_28':20,'region_29':21,'region_3':22,'region_30':23,'region_31':24,'region_32':25,'region_33':26,'region_34':27,'region_4':28,'region_5':29,'region_6':30,'region_7':31,'region_8':32,'region_9':33}
    region_list[region_dict[region]] = 1

    education_list = [0,0,0]
    education_dict = {"Bachelor's":0,"Master's & above":2,"Below Secondary":1}
    education_list[education_dict[education]] = 1

    gender_list = [0,0]
    gender_dict = {"f":0,"m":1}
    gender_list[gender_dict[gender]] = 1

    recruitment_list = [0,0,0]
    recruitment_dict = {"other":0,"referred":1,"sourcing":2}
    recruitment_list[recruitment_dict[recruitment]] = 1

    training_list = [0,0,0,0,0,0,0,0,0]
    training_dict = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8}
    training_list[training_dict[training]] = 1

    age_list = [0]*41
    age_dict = {'20':0,'21':1,'22':2,'23':3,'24':4,'25':5,'26':6,'27':7,'28':8,'29':9,'30':10,'31':11,'32':12,'33':13,'34':14,'35':15,'36':16,'37':17,'38':18,'39':19,'40':20,'41':21,'42':22,'43':23,'44':24,'45':25,'46':26,'47':27,'48':28,'49':29,'50':30,'51':31,'52':32,'53':33,'54':34,'55':35,'56':36,'57':37,'58':38,'59':39,'60':40}
    age_list[age_dict[age]] = 1

    prev_rating_list = [0]*5
    prev_rating_dict = {'1.0':0,'2.0':1,'3.0':2,'4.0':3,'5.0':4}
    prev_rating_list[prev_rating_dict[prev_rating]] = 1

    lservice_list = [0]*34
    lservice_dict = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'10':9,'11':10,'12':11,'13':12,'14':13,'15':14,'16':15,'17':16,'18':17,'19':18,'20':19,'21':20,'22':21,'23':22,'24':23,'25':24,'26':25,'27':26,'28':27,'29':28,'30':29,'31':30,'32':31,'33':32,'34':33}
    lservice_list[lservice_dict[lservice]] = 1

    kpi_list = [0,0]
    kpi_dict = {'0':0,'1':1}
    kpi_list[kpi_dict[kpi]] = 1

    awards_list = [0,0]
    awards_dict = {'0':0,'1':1}
    awards_list[awards_dict[awards]] = 1
    
    final_list = department_list + region_list + education_list + gender_list + recruitment_list + training_list + age_list + prev_rating_list + lservice_list + kpi_list + awards_list + [int(avg_train_score)]
    final_list = [final_list]
    final_list = pd.DataFrame(final_list,columns=col)
    
    return final_list
    
app = Flask(__name__)
model = pickle.load(open('HR_analytics_model_Random_forest.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    features = []
    for x in request.form.values():
        features.append(x)
        
    final_features = func(features[0],features[1],features[2],features[3],features[4],features[5],features[6],features[7],features[8],features[9],features[10],features[11])
    prediction = int(model.predict(final_features))
    
    if prediction == 1:
        output = 'promoted'
    else:
        output = 'not promoted'
    
    return render_template('index.html',prediction_text='You will be {}'.format(output))
    
if __name__ == '__main__':
    app.run(debug=True)