from flask import Flask
from flask import render_template,request, redirect
import os
import pymysql

app =Flask(__name__)

conn = pymysql.connect(host='localhost',
                             user ='wenlingding',
                             password='',
                             db='CookBookProject')

@app.route('/')
def home():
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country")
    user = cursor.fetchall()
    return render_template('home.html', all_user=user)

#the recipe details page
@app.route('/recipe/<recipe_id>', methods=['GET'])
def see_more(recipe_id):
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT user.id, user.name AS user_name, country.name AS country, recipe.date AS date, recipe.name AS recipe_name, cuisine.name AS cuisine_name, recipe.ingredients AS ingredients FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country INNER JOIN recipe_process ON recipe_process.recipe = recipe.id WHERE recipe.id = " + recipe_id)
    recipe=cursor.fetchall()
    cursor.execute("SELECT  `description` ,  `step` FROM recipe_process WHERE recipe_process.recipe = " + recipe_id)
    process = cursor.fetchall()
    return render_template('recipe.html', recipe=recipe, all_process=process, id=recipe_id)
 
 
@app.route('/add', methods=['GET', 'POST'])
def add_to_do():
    if request.method == 'GET':
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute("SELECT user.id, user.name AS user_name, country.name AS country, recipe.date AS date, recipe.name AS recipe_name, cuisine.id AS cuisine_id, cuisine.name AS cuisine_name, recipe.ingredients AS ingredients, recipe_process.step AS step, recipe_process.description AS description FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country INNER JOIN recipe_process ON recipe_process.recipe = recipe.id")
        recipe = cursor.fetchall()
        cursor.execute("SELECT * FROM cuisine")
        cuisine = cursor.fetchall()
        return render_template('add.html', all_recipe = recipe, all_cuisine=cuisine)
    else:
        print(request.form)
        user = request.form['user_name']
        name = request.form['recipe_name']
        cuisine_id = request.form['cuisine']
        ingredients = request.form['ingredients']
        step = request.form['step']
        description = request.form['description']
        sql = """
            INSERT INTO recipe(`user` ,`name` ,`ingredients`, `cuisine_id`)
            VALUES ("{}", "{}", "{}", {}", "{}")
            INSERT INTO `recipe_process` (`id` ,`recipe` ,`step` ,`description`)   
            VALUES ("{}", "{}", "{}", {}", "{}")
        """.format(user, name, ingredients, cuisine_id, id, recipe, step, description)
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return redirect('/')   
    
    
@app.route('/edit/<recipe_id>', methods=['GET', 'POST'])
def edit(recipe_id):
    if request.method == 'GET':
        recipe_id =request.args.get('recipe_id')
        cursor = pymysql.cursors .DictCursor(conn)
        cursor.execute("SELECT recipe.id AS recipe_id, recipe.name AS recipe_name, cuisine.name AS cuisine_name, recipe.ingredients AS ingredients FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN recipe_process ON recipe_process.recipe = recipe.id WHERE recipe.id = " + recipe_id)
        recipe=cursor.fetchall()
        cursor.execute("SELECT  `description` ,  `step` FROM recipe_process WHERE recipe_proc ess.recipe = " + recipe_id)
        process = cursor.fetchall()
        return render_template('edit.html', recipe=recipe, all_process=process, id=  recipe_id)
    else:
        name = request.form['recipeName']
        cuisine_id = request.form['cuisine']
        ingredients = request.form['ingredients']
        sql = """
            UPDATE recipe SET  
                name = "{}",
                cuisine_id = "{}",
                ingredients = "{}",
            WHERE recipe.id =
        """ + recipe_id.format(name, cuisine_id, ingredients, recipe.id)
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return redirect('/')    
   
@app.route('/delete/<recipe_id>') 
def delete(recipe_id):
    sql = "DELETE FROM recipe WHERE recipe.id =" + recipe_id.format(recipe_id)
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute(sql)
    conn.commit()
    return redirect('/')

   
   
   
   
   
   
   
   
   
   
   
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)