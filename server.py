import uvicorn

from fastapi import FastAPI
from fastapi.responses import FileResponse

from database_main import show_all, specific_data_lookup, username_lookup, get_score_stats

app = FastAPI()



@app.get("/")   # MAIN  index  PAGE     
async def root():
    return FileResponse('index.html', media_type='text/html')
    


@app.get("/login")   # LOGIN 
async def login(user: str = "",
                password: str = ""):
    if(username_lookup("database_1", str(user))):
        if(user == specific_data_lookup("database_1","username",1,user)  and  password == specific_data_lookup("database_1","username",2,user)):
            return FileResponse('game_stats.html', media_type='text/html')
        else:
            return FileResponse('index.html', media_type='text/html')
    else:
        return FileResponse('index.html', media_type='text/html')
   


@app.get("/fetch_scores")  # FETCH PLAYER SCORES
async def load_stats():  

    scores = get_score_stats("database_1")   #get a python list of players with scores ...
    


    return {"STATUS": "File upload successfully and download URL sent to recepients EMAIL adress"}




@app.get("/game")  # STATS PAGE
async def load_stats():  
    return {"STATUS": "File upload successfully and download URL sent to recepients EMAIL adress"}



@app.delete("/delete")
async def delete():
    return


@app.put("/put")
async def put():
    return



if __name__ == "__main__":
    uvicorn.run(app, host="192.168.0.22", port=5000)
    app.run(debug = True)
