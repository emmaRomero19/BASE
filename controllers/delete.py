import web
from pymongo import MongoClient
from bson.objectid import ObjectId
render=web.template.render('views/')

class Op:
    def GET(self):
        try:
            data=web.input()
            a=str(data['id'])
            b=a[8:-2]
            #conectar a mongodb
            client = MongoClient("mongodb://admin:admin@basededatos-shard-00-00.usvse.mongodb.net:27017,basededatos-shard-00-01.usvse.mongodb.net:27017,basededatos-shard-00-02.usvse.mongodb.net:27017/BaseDeDatos?ssl=true&replicaSet=atlas-vr1i5f-shard-0&authSource=admin&retryWrites=true&w=majority")
            #nombre de la base de datos
            db = client.BaseDeDatos 
            #nombre de la coleccin
            people = db.automovil
            a3=people.find_one_and_delete({"id":b})
            a1=people.find({})
            a2=people.find({}, {"_id":0, "id":1})
            return render.view(a1,a2)
        except expression as identifier:
            result=[]    
            result.append('error'+ str(e.args))
            return result
        
