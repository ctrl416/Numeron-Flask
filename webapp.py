from flask import Flask,render_template,request
import os
import random

app = Flask(__name__)#Flaskクラスのインスタンス生成

num_list=[0,1,2,3,4,5,6,7,8,9]
target_num = random.sample(num_list,3)
num_log=[]
eat_log=[] 
bite_log=[]
length=0


@app.route('/',methods=['GET','POST'])
def start():
   if request.method=="GET":
      global target_num
      target_num= random.sample(num_list,3)
      global num_log
      num_log=[]
      global eat_log
      eat_log=[] 
      global bite_log
      bite_log=[]
      global length
      length=0
   return render_template('start.html')
@app.route('/first_declare/',methods=['GET','POST'])
def first_declare():
   return render_template('first_declare.html',title='コンピュータが数字を設定しました。',target_num=target_num)
   

@app.route('/main_declare',methods=['GET','POST'])
def main_declare():
   user_num=request.form['user']
   eat=0
   bite=0
   if not user_num.isdecimal():
      return render_template('main_declare.html',title='整数を入力してよ',num_log='/',eat_log='/',bite_log='/',eat=0,length=0)
   elif len(user_num) !=3:
      return render_template('main_declare.html',title='3桁の数字で入力してよ',num_log='/',eat_log='/',bite_log='/',eat=0,length=0)
   elif user_num.count(user_num[0])!=1 or user_num.count(user_num[1])!=1 or user_num.count(user_num[2])!=1:
      return render_template('main_declare.html',title='重複は論外だよ！しっかりやってね',num_log='/',eat_log='/',bite_log='/',eat=0,length=0)
   num_log.append(user_num)
   length=len(num_log)
   for index,i_tar in enumerate(target_num):
      for cnt in range(3):
         if str(target_num[index])==user_num[index]:
            eat+=1
            break
         elif str(i_tar) in user_num:
            bite+=1
            break
   eat_log.append(eat)
   bite_log.append(bite)
 
   if eat!=3:
      return render_template('main_declare.html',title='残念！　ハズレだドン！！！',num_log=num_log,eat_log=eat_log,bite_log=bite_log,eat=eat,length=length)
   elif eat==3:
      return render_template('main_declare.html',title='クリア！！おめでとドン！！！！',num_log=num_log,eat_log=eat_log,bite_log=bite_log,eat=eat,length=length)



app.run(debug=True,host='0.0.0.0',port=8888,threaded=True)#Webアプリの起動（Flaskサーバの起動）
